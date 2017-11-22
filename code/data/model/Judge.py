from collections import namedtuple

from util import get_page


Judge = namedtuple('Judge', ['name', 'country'])

class JudgePanel:
    def __init__(self, url, season, event, discipline, segment):
        self.url = url
        self.season = season
        self.event = event
        self.discipline = discipline
        self.segment = segment
        self.fname = segment.name + '_panel.html'
        
    def get_page(self):
        get_page(self.url, self.season, self.event, self.fname)

    # ['referee', 'technical_controller', 'technical_specialist', 'asst_technical_specialist',
    #                          'judges', 'num_judges', 'data_operator', 'replay_operator',
    #                          'file_name', 'url'])  # where this panel info came from
