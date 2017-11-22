from collections import namedtuple
import re

Element = namedtuple('Element', ['number',       # order in program
                                 'name',         # e.g. 3A
                                 'info',         # e.g. UR
                                 'base_value',   # float
                                 'bonus',
                                 'goe',          # aggregated over judges
                                 'goes',         # list of individual judge GOEs (-3 to 3)
                                 'points'])      # total points for element

ProgramComponent = namedtuple('ProgramComponent', ['name',    # e.g. 'Skating Skills'
                                                   'factor',  # e.g. 1.0 in men's short, 2.0 in men's free
                                                   'scores',  # list of individual judge's scores
                                                   'points']) # aggregated judge's scores multiplied by factor

class Scorecard:
    def __init__(self, url, season, event, discipline, segment, skater,
                 rank, starting_number, total_score, tes, pcs, deductions):
        self.url = url
        self.season = season
        self.event = event
        self.discipline = discipline
        self.segment = segment
        self.skater = skater
        self.rank = int(rank)
        self.starting_number = int(starting_number)
        self.tes = float(tes)
        self.pcs = float(pcs)
        self.total_deductions = float(deductions)
        self.total_score = total_score
        
        self.elements = []
        self.components = []
        self.total_deductions = deductions
        self.deductions = {}
        
    def __repr__(self):
        return '{0} {1}: {2}'.format(self.season, self.segment, self.skater)
        
    def add_element(self, elt_match):
        number, name, info, base_value, bonus, goe, goes, points = elt_match.groups()
        number = int(number)
        base_value = float(base_value)
        bonus = bonus is not None
        goe = float(goe)
        
        # Split out individual judges' GOEs
        goe_re = re.compile('(-?[0123]\s*|-\s*)')
        goe_match = goe_re.findall(goes)
        if not goe_match:
            raise Exception(goes)
        goes = map(int, goe_match)
        
        points = float(points)
        self.elements.append(Element(number, name, info, base_value, bonus, goe, goes, points))

    def add_component(self, component_match):
        name, factor, scores, points = component_match.groups()
        factor = float(factor)
        comp_mark_re = re.compile('(\d?\d.\d\d\s*)')
        comp_match = comp_mark_re.findall(scores)
        if not comp_match:
            raise Exception(scores)
        scores = map(float, comp_match)
        
        points = float(points)
        self.components.append(ProgramComponent(name, factor, scores, points))

    def add_deduction(self, deduction_match):
        deductions = deduction_match.groups()
        for deduction in deductions:
            reason, value = deduction.split(':')
            fall_re = re.compile('(-\d.\d\d)\s*(\(\d\))')
            if fall_re.match(value):
                value, num_falls = fall_re.match(value).groups()
                reason += num_falls
            value = float(value)
            self.deductions[reason] = value
    
    def aggregate_elements(self, tes_match):
        self.base_value, tes = map(float, tes_match.groups())
        self.goe_total = sum([elt.goe for elt in self.elements])
        assert self._is_close(sum([elt.base_value for elt in self.elements]), self.base_value)
        assert self._is_close(self.goe_total, tes - self.base_value)
        assert self._is_close(sum([elt.points for elt in self.elements]), tes)
        assert self._is_close(tes, self.tes)
        
        # Check the GOEs for sanity.
        for elt in self.elements:
            assert self._is_close(elt.base_value + elt.goe, elt.points)

    def aggregate_pcs(self, pcs):
        self.pcs = float(pcs)
        pcs_count = 0.
        for component in self.components:
            points = (sum(component.scores) - min(component.scores) - max(component.scores)) / (len(component.scores) - 2)
            assert self._is_close(points, component.points)
            pcs_count += points * component.factor
        assert self._is_close(pcs_count, self.pcs)
        
    def print_scorecard(self):
        print self.skater, self.rank, 'start:', self.starting_number
        print 'TES: {0}, PCS: {1}, Total: {2}'.format(self.tes, self.pcs, self.total_score)
        print 'Deductions: ' + str(self.deductions)
        for element in self.elements:
            print element
        for component in self.components:
            print component
            
    def _is_close(self, float1, float2):
        return abs(float1 - float2) < 0.01