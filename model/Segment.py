import csv
from enum import Enum
import os
import pickle
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
base_value_re = '(\d\d?\d?\.\d\d?)\s*'

class Segment:

    skater_re = re.compile('(\d+)\s*' +              # rank
                           '(\D+ \D+?)\s*' +         # skater name
                           '([A-Z][A-Z][A-Z])\s*' +  # country
                           '([12345]?\d)?\s+' +      # starting number
                           '(\d\d\d?\.\d\d)\s*' +    # total score
                           points + '\s+' +          # tes
                           points + '\s*' +          # pcs
                           '(-?\d.\d\d)')            # deductions
    tes_re = re.compile('^\s*' + base_value_re +     # total base value
                        points + '\s*$')             # total tes
    deduction_re = re.compile('[^-\d\s:()]+:?\s+-?[1-9]\.\d\d')
    # pcs_re = re.compile('Program\s+Component\D*' + points)


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
        if self._load_gpcan05_pairs_short():
            return

        assert not self.scorecards

        num_judges = str(self.num_judges)
        self.elt_re = re.compile(
                        '(\d\d?)\s+' +               # element order
                        '(\S+)\s+' +                 # element name
                        '(\D*?)\s*' +                # info (i.e. UR)
                        base_value_re +              # base value
                        '((?:x|X)?)\s*' +            # bonus marker
                        '(-?\d.\d\d)\s*' +           # goe
                        '((?:(?:-?\d|-)\s*){' + num_judges + '})\s*' +  # goes
                        '([0-]\s*)*\s*'              # extra judges...?
                        '(\d?\d.\d\d)')              # element score

        self.component_re = re.compile(
                                '(\D+)\s*' +             # component name
                                '(\d.\d\d)\s*' +         # factor
                                '((?:(?:\d?\d.\d\d|-)\s+){' + num_judges + '})\s*' +  # judges marks
                                '(?:(?:-|0.00)\s*)*\s*'  # extra judges...?
                                '(\d?\d.\d\d)')          # aggregated judges marks

        rows = self.get_raw_csv_rows()
        skater = None
        scorecard = None
        self.mistakes = []
        for line in rows:
            line = line.strip()
            line = self._remove_info(line)

            skater_match = self.skater_re.match(line)
            elt_match = self.elt_re.match(line)
            component_match = self.component_re.match(line)

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
                continue

            # A technical element.
            elif elt_match:
                scorecard.add_element(elt_match)

            # The TES summary row.
            elif scorecard and scorecard.elements and self.tes_re.match(line):
                scorecard.aggregate_elements(self.tes_re.match(line))

            # A PCS line.
            elif component_match:
                scorecard.add_component(component_match)

            # Bottom of the scorecard, either PCS summary or deductions.
            elif scorecard and scorecard.components:
                if 'Program Component' in line:
                    scorecard.aggregate_pcs(line[-5:])
                else:
                    scorecard.add_deduction(self.deduction_re.findall(line))

        if scorecard:
            self.mistakes += scorecard.check_total()
            self.scorecards.append(scorecard)

        if self.mistakes:
            print self
            for mistake in self.mistakes:
                print mistake
            print

    def write_to_csv(self):
        if self._load_gpcan05_pairs_short():
            return

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

                writer.writerow([self.num_judges])

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

                num_judges = int(reader.next()[0])

                reader.next()  # Skip labels row

                rank, name, nation, starting_number, total_score, tes, pcs, total_deductions = reader.next()
                skater = Skater(name.strip(), nation, self.discipline)
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
                    if elt_row[4].lower() == 'true':
                        bonus = True
                    elif elt_row[4].lower() == 'false':
                        bonus = False
                    else:
                        print skater, number, self, elt_row[4]
                    goe = float_of(elt_row[5])
                    goes = []
                    parsed_goes = []
                    for mark in elt_row[6:6+self.num_judges]:
                        if mark == '-':
                            goes.append(mark)
                        else:
                            goes.append(float_of(mark))
                            parsed_goes.append(float_of(mark))
                    points = float_of(elt_row[-1])
                    scorecard.elements.append(
                        Element(number, name, info, base_value, bonus, goe, goes, parsed_goes, points))
                    elt_row = reader.next()
                scorecard.base_value = float_of(elt_row[3])
                scorecard.tes = float_of(elt_row[-1])

                reader.next()  # Skip PCS label row
                comp_row = reader.next()
                while comp_row[1]:
                    name = comp_row[1]
                    factor = float_of(comp_row[5])
                    scores = []
                    parsed_scores = []
                    for score in comp_row[6:6+self.num_judges]:
                        if score == '-':
                            scores.append(score)
                        else:
                            scores.append(float_of(score))
                            parsed_scores.append(float_of(score))
                    points = float_of(comp_row[-1])
                    scorecard.components.append(
                        ProgramComponent(name.strip(), factor, scores, parsed_scores, points))
                    comp_row = reader.next()
                scorecard.pcs = float_of(comp_row[-1])

                for deduction_row in reader:
                    _, reason, value = deduction_row
                    scorecard.deductions[reason] = float_of(value)

                self.scorecards.append(scorecard)
        self.scorecards.sort(key=lambda scorecard: scorecard.rank)

    @staticmethod
    def _remove_info(line):
        """In 2008-2010, many events (see gpjpn2007 pairs short) have the
           'Info' keyword in the wrong row (in an element row)."""
        if line[0].isdigit():
            words = line.split()        # Space-delimited 'words'
            new_words = []              # Construct the new line
            for i, word in enumerate(words):
                new_word = word
                if word in 'Info':
                    continue
                if i > 1 and any(char.isdigit() or char == '-' for char in word):
                    new_word = ''.join([char for char in list(word) if char not in 'Info'])
                new_words.append(new_word)
            return ' '.join(new_words)
        return line

    def _load_gpcan05_pairs_short(self):
        if self.event.name == 'gpcan05' and self.name == 'pairs_short':
            with open('0506/gpcan05/pairs_short.pickle') as f:
                self.scorecards = pickle.load(f)
            return True
        return False
