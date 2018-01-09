from bs4 import BeautifulSoup
import requests
import subprocess

from Discipline import Discipline, DisciplineType
from Panel import Panel
from Segment import Segment, SegmentType
from util import get_page


tabula_path = 'tabula-1.0.1-jar-with-dependencies.jar'

class Event:
    def __init__(self, season, name):
        self.name = name      # the abbreviation + year
        self.season = season  # season object
        self.url = season.url + name + '/'
        self.dirpath = season.year + '/' + self.name + '/'
    
    def __repr__(self):
        return self.name

    def pdfs_to_csvs(self):
        subprocess.Popen('java -jar ' + tabula_path + ' -p all -b ' + self.dirpath, shell=True)

    def parse_csvs(self):
        for discipline in self.disciplines:
            for segment in discipline.segments:
                segment.read_from_csv()

    def fetch_info(self, fetch_files=False):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        self.disciplines = []

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
                elif 'Panel' in link.text:
                    discipline.panel_urls.append(self.url + href)
                elif 'Scores' in link.text:
                    discipline.score_urls.append(self.url + href)
                    if 'Preliminary' in href:  # Skip over preliminary rounds.
                        discipline = Discipline(self.season, self, discipline_type)
                cur_link += 1
            discipline.create_segments()
            if fetch_files:
                discipline.get_page()
            for segment in discipline.segments:
                segment.panel.parse_html()
                segment.num_judges = segment.panel.num_judges
            self.disciplines.append(discipline)
        if fetch_files:
            self.pdfs_to_csvs()
