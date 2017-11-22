import csv
from enum import Enum
import re

from Judge import JudgePanel
from Scorecard import Scorecard
from Skater import Skater
from util import get_fpath, get_page

class SegmentType(Enum):
    short = 0
    free = 1
    original_dance = 2

# sorry not sorry
points = '(\d\d?\d?.\d\d)'
skater_re = re.compile('(\d+)\s*' +              # rank
                       '(\D+ \D+?)\s*' +         # skater name
                       '([A-Z][A-Z][A-Z])\s*' +  # country
                       '(\d\d?)\s*' +            # starting number
                       '(\d\d\d?.\d\d)\s*' +     # total score
                       points + '\s*' +          # tes
                       points + '\s*' +          # pcs
                       '(-?\d.\d\d)')            # deductions
tes_re = re.compile('^' + points + '\s*' +       # total base value
                    points + '\s*$')             # total tes
deduction_re = re.compile('Deductions:\s+(\S+: -\d.\d\d[^-]*)+')
# pcs_re = re.compile('Program\s+Component\D*' + points)


class Segment:
    def __init__(self, url, season, event, discipline, segment, panel_url):
        self.url = url  # url to scores
        self.season = season
        self.event = event
        self.discipline = discipline
        self.type = segment
        self.name = discipline.name + '_' + segment.name
        
        self.fname = discipline.name + '_' + segment.name
        self.pdf_fname = self.fname + '.pdf'
        self.csv_fname = self.fname + '.csv'
        self.fpath = get_fpath(season, event, self.pdf_fname)
        self.csv_path = get_fpath(season, event, self.csv_fname)
        self.panel = JudgePanel(panel_url, self.season, self.event, self.discipline, self)
        self.scorecards = []
        
        num_judges = '9'
        self.elt_re = re.compile('(\d)\s*' +                  # element order
                                 '(\S+)\s*' +                 # element name
                                 '(\D*?)\s*' +                # info (i.e. UR)
                                 points + '\s*' +             # base value
                                 '(x?)\s*' +                  # bonus marker
                                 '(-?\d.\d\d)\s*' +           # goe
                                 '((?:-?\d\s*|-){' + num_judges + '})\s*' +  # goes
                                 '(\d?\d.\d\d)')              # element score

        self.component_re = re.compile('(\D+?)\s*' +          # component name
                                       '(\d.\d\d)\s*' +       # factor
                                       '((?:\d?\d.\d\d\s*){' + num_judges + '})\s*' +  # judges marks
                                       '(\d?\d.\d\d)')        # aggregated judges marks

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
                rows.append(''.join(row))
        return rows
    
    def parse_raw_csv(self):
        assert not self.scorecards
        rows = self.get_raw_csv_rows()
        skater = None
        scorecard = None
        
        for line in rows:
            line = line.strip()
            
            skater_match = skater_re.match(line)
            elt_match = self.elt_re.match(line)
            component_match = self.component_re.match(line)
            
            # Skater + summary info.
            if skater_match:
                if scorecard:
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
                                      skater_info['pcs'],skater_info['deductions'])
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
                deduction_match = deduction_re.match(line)
                if 'Program Component' in line:
                    scorecard.aggregate_pcs(line[-5:])
                elif deduction_match:
                    scorecard.add_deduction(deduction_match)
        
        if scorecard:
            self.scorecards.append(scorecard)
