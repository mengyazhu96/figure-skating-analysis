from enum import Enum

from util import get_page

class DisciplineType(Enum):
    men = 0
    ladies = 1
    pairs = 2
    ice_dance = 3


class Discipline:
    def __init__(self, season, event, discipline):
        self.discipline = discipline  # of type DisciplineType
        self.season = season
        self.event = event
        self.segments = []            # list of Segments
        self.entries = []
        self.entries_url = None
        self.entries_fname = self.discipline.name + '_entries.html'
        self.results = []
        self.results_url = None
        self.results_fname = self.discipline.name + '_results.html'
    
    def __repr__(self):
        return self.event.name + ' ' + self.discipline.name
    
    def get_entries_results_pages(self):
        assert self.entries_url and self.results_url
        get_page(self.entries_url, self.season, self.event, self.entries_fname)
        get_page(self.results_url, self.season, self.event, self.results_fname)