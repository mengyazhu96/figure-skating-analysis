from bs4 import BeautifulSoup
from collections import namedtuple, OrderedDict
import re

from util import get_fpath, get_page


Official = namedtuple('Official', ['function', 'name', 'nation'])

class Panel:
    def __init__(self, url, season, event, discipline, segment):
        self.url = url
        self.season = season
        self.event = event
        self.discipline = discipline
        self.segment = segment
        self.fname = segment.name + '_panel.html'
        self.fpath = get_fpath(season, event, self.fname)

    def parse_html(self):
        with open(self.fpath, 'rb') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        self.officials = OrderedDict()
        self.judges = []
        for tr in soup.find_all(attrs={'class': True}, name='tr'):
            contents = [elt for elt in tr.contents if elt != '\n']
            if len(contents) != 3 or contents[0].name != 'td':
                continue
            function, name, nation = map(lambda x: getattr(x, 'text').strip(), contents)
            if not function or not name or not nation:
                continue

            official = Official(function, name, nation)
            self.officials[function] = official
            if 'Judge' in function:
                self.judges.append(official)
        self.num_judges = len(self.judges)
        
    def get_page(self):
        get_page(self.url, self.season, self.event, self.fname)

    def __repr__(self):
        return '\n'.join(map(str, self.officials.values()))
