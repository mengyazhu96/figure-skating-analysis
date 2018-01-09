import csv
from enum import Enum
import os
import re

from Panel import Panel
from Scorecard import Element, ProgramComponent, Scorecard
from Skater import Skater
from util import clear_and_make_dir, float_of, get_fpath, get_page

class SegmentType(Enum):
    short = 0
    free = 1
    original_dance = 2

# sorry not sorry
points = '(\d\d?\d?.\d\d)'
skater_re = re.compile('(\d+)\s*' +              # rank
                       '(\D+ \D+?)\s*' +         # skater name
                       '([A-Z][A-Z][A-Z])\s*' +  # country
                       '([123]?\d)\s*' +         # starting number
                       '(\d\d\d?.\d\d)\s*' +     # total score
                       points + '\s*' +          # tes
                       points + '\s*' +          # pcs
                       '(-?\d.\d\d)')            # deductions
tes_re = re.compile('^' + points + '\s*' +       # total base value
                    points + '\s*$')             # total tes
deduction_re = re.compile('[^-\d:]+: -\d.\d\d')
# pcs_re = re.compile('Program\s+Component\D*' + points)


class Segment:
    def __init__(self, url, season, event, discipline, segment, panel_url):
        self.url = url  # url to scores
        self.season = season
        self.event = event
        self.discipline = discipline
        self.type = segment
        self.name = discipline.name + '_' + segment.name
        self.panel = Panel(panel_url, self.season, self.event, self.discipline, self)
        self.scorecards = []
        
        # Associated file names and paths.
        self.fname = discipline.name + '_' + segment.name
        self.pdf_fname = self.fname + '.pdf'
        self.csv_fname = self.fname + '.csv'
        self.parsed_csv_fname = self.fname + '_parsed.csv'
        self.fpath = get_fpath(season, event, self.pdf_fname)
        self.csv_path = get_fpath(season, event, self.csv_fname)
        self.parsed_csv_fpath = get_fpath(season, event, self.parsed_csv_fname)
        self.directory = get_fpath(self.season, self.event, self.name)
        
    def __repr__(self):
        return self.event.name + ' ' + self.name

    def get_page(self):
        get_page(self.url, self.season, self.event, self.pdf_fname)
        self.panel.get_page()

    def get_raw_csv_rows(self):
        rows = []
        with open(self.csv_path, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(' '.join(row))
        return rows
    
    def parse_raw_csv(self):
        assert not self.scorecards

        num_judges = str(self.num_judges)
        elt_re = re.compile('(\d\d?)\s+' +               # element order
                            '(\S+)\s*' +                 # element name
                            '(\D*?)\s*' +                # info (i.e. UR)
                            points + '\s*' +             # base value
                            '(x?)\s*' +                  # bonus marker
                            '(-?\d.\d\d)\s*' +           # goe
                            '((?:-?\d\s*|-){' + num_judges + '})\s*' +  # goes
                            '(?:-\s*)*\s*'               # why on earth is this here
                                                         # see gpusa2010, gpchn2014
                            '(\d?\d.\d\d)')              # element score

        component_re = re.compile('(\D+?)\s*' +          # component name
                                  '(\d.\d\d)\s*' +       # factor
                                  '((?:\d?\d.\d\d\s*){' + num_judges + '})\s*' +  # judges marks
                                  '(?:-\s*)*\s*'         # why on earth is this here
                                                         # see gpusa2010
                                  '(\d?\d.\d\d)')        # aggregated judges marks

        rows = self.get_raw_csv_rows()
        skater = None
        scorecard = None
        self.mistakes = []
        for line in rows:
            line = line.strip()
            
            skater_match = skater_re.match(line)
            elt_match = elt_re.match(line)
            component_match = component_re.match(line)
            
            # Skater + summary info.
            if skater_match:
                if scorecard:
                    self.mistakes += scorecard.check_total()
                    self.scorecards.append(scorecard)
                    scorecard = None
                
                skater_info = {}
                for i, info in enumerate(('rank', 'name', 'country', 'starting_number',
                                          'total_score', 'tes', 'pcs', 'deductions')):
                    skater_info[info] = skater_match.group(i + 1)
                skater = Skater(skater_info['name'], skater_info['country'], self.discipline)
                scorecard = Scorecard(self.url, self.season, self.event, self.discipline, self, skater,
                                      skater_info['rank'], skater_info['starting_number'],
                                      skater_info['total_score'], skater_info['tes'],
                                      skater_info['pcs'], skater_info['deductions'])
            # A technical element.
            elif elt_match:
                scorecard.add_element(elt_match)

            # The TES summary row.
            elif scorecard and scorecard.elements and tes_re.match(line):
                scorecard.aggregate_elements(tes_re.match(line))

            # A PCS line.
            elif component_match:
                scorecard.add_component(component_match)

            # Bottom of the scorecard, either PCS summary or deductions.
            elif scorecard and len(scorecard.components) == 5:
                if 'Program Component' in line:
                    scorecard.aggregate_pcs(line[-5:])
                elif 'Deduction' in line:
                    scorecard.add_deduction(deduction_re.findall(line))

        if scorecard:
            self.mistakes += scorecard.check_total()
            self.scorecards.append(scorecard)

        if self.mistakes:
            print self
            for mistake in self.mistakes:
                print mistake
            print

    def write_to_csv(self):
        if not self.scorecards:
            self.parse_raw_csv()

        clear_and_make_dir(self.directory)

        judge_numbers = list(xrange(1, self.num_judges + 1))
        judge_space = ['' for _ in xrange(self.num_judges)]

        for scorecard in self.scorecards:
            fname = '{0}/{1}_{2}.csv'.format(self.directory, scorecard.rank,
                                             scorecard.skater.name.replace(' / ', '_').replace(' ', '_'))
            with open(fname, 'w') as csvfile:
                writer = csv.writer(csvfile)

                writer.writerow(['Rank', 'Name', 'Nation',
                                 'Starting Number', 'Total Segment Score',
                                 'Total Element Score',
                                 'Total Program Component Score (factored)',
                                 'Total Deductions'])
                writer.writerow([scorecard.rank, scorecard.skater.name, scorecard.skater.country,
                                 scorecard.starting_number, scorecard.total_score,
                                 scorecard.tes,
                                 scorecard.pcs,
                                 scorecard.total_deductions])

                # Write technical scores.
                writer.writerow(['#', 'Executed Elements', 'Info', 'Base Value', 'Bonus', 'GOE'] + 
                                judge_numbers + ['Ref', 'Scores of Panel'])
                for elt in scorecard.elements:
                    writer.writerow([elt.number, elt.name, elt.info, elt.base_value, elt.bonus, elt.goe] +
                                     elt.goes +
                                     ['', elt.points])
                writer.writerow(['', '', '', scorecard.base_value, '', ''] +
                                judge_space + ['', scorecard.tes])

                # Write component scores.
                writer.writerow(['', 'Program Components', '', '', '', 'Factor'])
                for comp in scorecard.components:
                    writer.writerow(['', comp.name, '', '', '', comp.factor] +
                                    comp.scores + ['', comp.points])
                writer.writerow(['', '', '', '', '', ''] + judge_space + ['', scorecard.pcs])

                for reason, value in scorecard.deductions.iteritems():
                    writer.writerow(['Deduction', reason, value])

        # Rank, Name, Nation, Starting Number, Total Score, TES, PCS, Total Deductions
        # Number, Executed Elements, Info, Base Value, Bonus, GOE, 1 - num_judges, ref, score
        # PCS, Component Name, empty, empty, Factor, 1 - num_judges, empty, score
        # Deduction: point value

    def read_from_csv(self):
        if not os.path.isdir(self.directory):
            self.write_to_csv()
            return

        for fname in os.listdir(self.directory):
            with open(self.directory + '/' + fname) as csvfile:
                reader = csv.reader(csvfile)
                reader.next()  # Skip labels row

                rank, name, nation, starting_number, total_score, tes, pcs, total_deductions = reader.next()
                skater = Skater(name, nation, self.discipline)
                scorecard = Scorecard(self.url, self.season, self.event,
                                      self.discipline, self, skater,
                                      rank, starting_number, total_score,
                                      tes, pcs, total_deductions)

                reader.next()  # Skip elements label row
                elt_row = reader.next()
                while elt_row[0].isdigit():
                    number = int(elt_row[0])
                    name = elt_row[1]
                    info = elt_row[2]
                    base_value = float_of(elt_row[3])
                    bonus = bool(elt_row[4])
                    goe = float_of(elt_row[5])
                    goes = map(float_of, elt_row[6:6+self.num_judges])
                    points = float_of(elt_row[-1])
                    scorecard.elements.append(
                        Element(number, name, info, base_value, bonus, goe, goes, points))
                    elt_row = reader.next()
                scorecard.base_value = float_of(elt_row[3])
                scorecard.tes = float_of(elt_row[-1])

                reader.next()  # Skip PCS label row
                comp_row = reader.next()
                while comp_row[1]:
                    name = comp_row[1]
                    factor = float_of(comp_row[5])
                    scores = map(float_of, comp_row[6:6+self.num_judges])
                    points = float_of(comp_row[-1])
                    scorecard.components.append(
                        ProgramComponent(name, factor, scores, points))
                    comp_row = reader.next()
                scorecard.pcs = float_of(comp_row[-1])

                for deduction_row in reader:
                    _, reason, value = deduction_row
                    scorecard.deductions[reason] = float_of(value)

                self.scorecards.append(scorecard)
        self.scorecards.sort(key=lambda scorecard: scorecard.rank)
