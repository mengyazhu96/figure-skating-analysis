from bs4 import BeautifulSoup
from lxml import html, etree
import requests
import subprocess

from Discipline import Discipline, DisciplineType
from Judge import JudgePanel
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

    def get_event_info(self, fetch_files=False):
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
                cur_link += 1
            discipline.create_segments()
            if fetch_files:
                discipline
            self.disciplines.append(discipline)

    def _flatten_html_children(self, elts):
        children = []
        for elt in elts:
            for child in elt.getchildren():
                children.append(child)
        return children