from enum import Enum

from Segment import SegmentType, Segment
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

        self.panel_urls = []
        self.score_urls = []

    def create_segments(self):
        num_segments = len(self.panel_urls)
        if self.event.name == 'gpfra2015':
            num_segments = 1

        for i in xrange(num_segments):
            segment_type = SegmentType(i)

            # original dance support
            if num_segments == 3:
                if i == 1:
                    segment_type = SegmentType(2)
                elif i == 2:
                    segment_type = SegmentType(1)

            self.segments.append(Segment(self.score_urls[i], self.season, self.event,
                                         self.discipline, segment_type, self.panel_urls[i]))

    def __repr__(self):
        return self.event.name + ' ' + self.discipline.name
    
    def get_page(self):
        assert self.entries_url and self.results_url
        get_page(self.entries_url, self.season, self.event, self.entries_fname)
        get_page(self.results_url, self.season, self.event, self.results_fname)
        for segment in self.segments:
            segment.get_page()