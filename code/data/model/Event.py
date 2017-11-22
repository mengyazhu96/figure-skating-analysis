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
        try:
            tree = html.fromstring(page.content)
        except etree.ParserError:
            print 'Event not found: % s' % event
            return

        if not list(tree.iter('title')):
            print 'Event not found: % s' % event
            return
        else:
            print list(tree.iter('title'))[0].text

        # Drill down to the table part.
        table = tree.getchildren()[1].getchildren()[2].getchildren()
        elts = self._flatten_html_children(table)
        elts = self._flatten_html_children(elts)
        elts = self._flatten_html_children(elts)
        elts = self._flatten_html_children(elts)
        
        # 12 rows of actual table: cut out header and juniors
        rows = elts[2].getchildren()[0].getchildren()[1:13]

        self.disciplines = []
        for i, discipline_type in enumerate(list(DisciplineType)):
            
            discipline = Discipline(self.season, self, discipline_type)
            
            # Get entries and results pages.
            entries, results = self._flatten_html_children(rows[i * 3])
            discipline.entries_url = self.url + entries.attrib['href']
            discipline.results_url = self.url + results.attrib['href']
            if fetch_files:
                discipline.get_entries_results_pages()
            
            # Get segment files.
            for prog in (SegmentType.short, SegmentType.free):
                j = prog.value
                panel, detailed, scorecards = self._flatten_html_children(rows[i * 3 + j + 1])
                segment = Segment(self.url + scorecards.attrib['href'], self.season, self, discipline_type, prog)
                
                if fetch_files:
                    segment.get_page()
                discipline.segments.append(segment)

                panel = JudgePanel(self.url + panel.attrib['href'], self.season, self, discipline_type, segment)                
                if fetch_files:
                    panel.get_page()
            self.disciplines.append(discipline)

    def _flatten_html_children(self, elts):
        children = []
        for elt in elts:
            for child in elt.getchildren():
                children.append(child)
        return children