from bs4 import BeautifulSoup
from datetime import date
import re
import requests
import subprocess

from Discipline import Discipline, DisciplineType
from Panel import Panel
from Segment import Segment, SegmentType
from util import get_page


tabula_path = 'tabula-1.0.1-jar-with-dependencies.jar'

class Event:
    date_re = re.compile('(\d\d?).(\d\d?).(20\d\d)')

    def __init__(self, season, name):
        self.name = name      # the abbreviation + year
        self.season = season  # season object
        self.url = season.url + name + '/'
        self.dirpath = season.year + '/' + self.name + '/'
    
    def __repr__(self):
        return self.name

    def pdfs_to_csvs(self):
        subprocess.Popen('java -jar ' + tabula_path + ' -p all -b ' + self.dirpath, shell=True)

    def parse_csvs(self, reparse=False):
        for discipline in self.disciplines:
            for segment in discipline.segments:
                if reparse:
                    segment.write_to_csv()
                else:
                    segment.read_from_csv()

    def load_and_validate_scores(self):
        for discipline in self.disciplines:
            for segment in discipline.segments:
                segment.read_from_csv()
                mistakes = []
                for scorecard in segment.scorecards:
                    mistakes += scorecard.check_total()
                if mistakes:
                    print segment
                    for mistake in mistakes:
                        print mistake
                    print

    def create_results(self):
        for discipline in self.disciplines:
            discipline.create_results()

    def write_results(self):
        for discipline in self.disciplines:
            discipline.create_results()
            discipline.write_results()

    def fetch_info(self, fetch_files=False):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        self.disciplines = []

        if self.name == 'gpjpn2017':
            day = 12
            month = 11
            year = 2017
        elif self.name == 'gpf1718':
            day = 10
            month = 12
            year = 2017
        else:
            date_matches = self.date_re.findall(soup.get_text())
            day = int(date_matches[1][0])
            month = int(date_matches[1][1])
            year = int(date_matches[1][2])
        if month not in (10, 11, 12, 1, 2, 3, 4):
            month_save = month
            month = day
            day = month_save
        self.date = date(year, month, day)

        links = soup.find_all('a')
        num_links = len(links)
        cur_link = 0
        for discipline_type in list(DisciplineType):
            discipline = Discipline(self.season, self, discipline_type)
            while cur_link < num_links:
                link = links[cur_link]
                if not link.text:
                    cur_link += 1
                    continue
                href = link['href']
                if 'Entries' in link.text and discipline.entries_url is not None:
                    break
                elif 'Entries' in link.text:
                    discipline.entries_url = self.url + href
                elif 'Result' in link.text:
                    discipline.results_url = self.url + href
                elif 'Panel' in link.text or 'Officials' in link.text:
                    discipline.panel_urls.append(self.url + href)
                elif 'Scores' in link.text or 'Judges Score' in link.text:
                    discipline.score_urls.append(self.url + href)

                    # Skip over preliminary/qualifying/junior rounds.
                    if 'Preliminary' in href or 'Junior' in href:  # wc2011, gpf0910
                        discipline = Discipline(self.season, self, discipline_type)
                    elif 'QB' in href or 'QA' in href:  # wc2005
                        discipline.panel_urls = []
                        discipline.score_urls = []
                cur_link += 1
            discipline.create_segments()
            if fetch_files:
                discipline.get_page()
            for segment in discipline.segments:
                segment.panel.parse_html()
                segment.num_judges = segment.panel.num_judges

                # fc2005 pairs short is missing the panel page.
                if (segment.event.name == 'fc2006' and
                    segment.discipline == DisciplineType.pairs and
                    segment.type == SegmentType.short):
                    segment.num_judges = 12

            self.disciplines.append(discipline)
        if fetch_files:
            self.pdfs_to_csvs()
