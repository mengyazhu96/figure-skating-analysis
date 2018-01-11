from collections import namedtuple
import re

from util import float_of

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
        try:
            self.starting_number = int(starting_number)
        except:
            self.starting_number = 0
        self.tes = float_of(tes)
        self.pcs = float_of(pcs)
        self.total_deductions = float_of(deductions)
        self.total_score = float_of(total_score)

        self.elements = []
        self.components = []
        self.total_deductions = deductions
        self.deductions = {}

        self.mistakes = []
        self.pre10 = int(self.season.champ_year) <= 2010

    def __repr__(self):
        return '{0} {1}: {2}'.format(self.season, self.segment, self.skater)
        
    def add_element(self, elt_match):
        extra_judges = 0

        number, name, info, base_value, bonus, goe, goes, extra, points = elt_match.groups()
        number = int(number)
        base_value = float_of(base_value)
        bonus = bonus == 'x'
        goe = float_of(goe)

        # Split out individual judges' GOEs
        goe_re = re.compile('(-?[0123]\s*|-\s*)')
        goe_match = goe_re.findall(goes)
        if not goe_match:
            raise Exception(goes)

        if self._is_zeroed_element(base_value):
            goes = [0.00 for _ in xrange(len(goe_match))]
        else:
            goes, extra_judges = self._parse_goes(goe_match)

        if extra and self._is_first_elt_of_segment():
            self.mistakes.append('Extra Judges: ' + extra)

        points = float_of(points)
        self.elements.append(Element(number, name, info, base_value, bonus, goe, goes, points))
        return extra_judges

    def add_component(self, component_match):
        name, factor, scores, points = component_match.groups()
        factor = float_of(factor)
        comp_mark_re = re.compile('(\d?\d.\d\d\s*)')
        comp_match = comp_mark_re.findall(scores)
        if not comp_match:
            raise Exception(scores)
        scores = self._parse_components(comp_match)
        
        points = float_of(points)
        self.components.append(ProgramComponent(name, factor, scores, points))

    def add_deduction(self, deductions):
        for deduction in deductions:
            reason, value = deduction.split(':')
            fall_re = re.compile('(-\d.\d\d)\s*(\(\d\))')
            if fall_re.match(value):
                value, num_falls = fall_re.match(value).groups()
                reason += num_falls
            value = float_of(value)
            if value > 0.:      # Sometimes deductions are captured as positive.
                value = -value

            # Ignore deductions of zero value.
            if not self._is_close(0.00, value):
                self.deductions[reason] = value
    
    def aggregate_elements(self, tes_match):
        self.base_value, tes = map(float_of, tes_match.groups())
        self.goe_total = sum([elt.goe for elt in self.elements])
        for (num1, num2, description) in (
            (sum([elt.base_value for elt in self.elements]), self.base_value, 'base value'),
            (self.goe_total, tes - self.base_value, 'base value + goe = tes'),
            (sum([elt.points for elt in self.elements]), tes, 'sum of elts = tes'),
            (tes, self.tes, 'summary tes = computed tes')
            ):
            self._check(num1, num2, description)

        # Check the GOEs for sanity.
        for i, elt in enumerate(self.elements):
            self._check(elt.base_value + elt.goe, elt.points, 
                        'bv + goe = elt points ' + str(i+1))

    def aggregate_pcs(self, pcs):
        self.pcs = float_of(pcs)
        pcs_count = 0.
        for component in self.components:
            points = (sum(component.scores) - min(component.scores) - max(component.scores)) / (len(component.scores) - 2)
            self._check(points, component.points, 'aggregated component: ' + component.name, True)
            pcs_count += round(points, 2) * component.factor
        if self.pre10:
            pcs_count = sum([comp.points * comp.factor for comp in self.components])
        self._check(pcs_count, self.pcs, 'summary pcs = computed pcs')

    def check_total(self):
        self._check(self.tes + self.pcs + sum(self.deductions.values()),
                    self.total_score, 'total score')
        return self.mistakes

    def print_scorecard(self):
        print self.skater, self.rank, 'start:', self.starting_number
        print 'TES: {0}, PCS: {1}, Total: {2}'.format(self.tes, self.pcs, self.total_score)
        print 'Deductions: ' + str(self.deductions)
        for element in self.elements:
            print element
        for component in self.components:
            print component

    def _is_close(self, float1, float2):
        return abs(float1 - float2) < 0.02

    def _check(self, num1, num2, description, no_check_pre10=False):
        if not (self.pre10 and no_check_pre10) and not self._is_close(num1, num2):
            self.mistakes.append('{0}: {1}, {2} != {3}'.format(self.skater, num1, num2, description))

    def _parse_goes(self, goe_match):
        """Sometimes judges are removed, resulting in a - for a GOE."""
        goes = []
        extra_judges = 0
        for goe in goe_match:
            try:
                goes.append(int(goe))
            except:
                if self._is_first_elt_of_segment():
                    extra_judges += 1
                # This guy's scorecard is weird.
                elif self.skater.name == 'Harry Hau Yin LEE' and self.event.name == 'fc2015':
                    goes.append(0)
        return goes, extra_judges

    def _parse_components(self, comp_match):
        """When a judge is removed, the component mark becomes 0.00."""
        scores = []
        for score in map(float_of, comp_match):
            if not self._is_close(0.00, score):
                scores.append(score)
            elif not self.components:
                self.mistakes.append('Zero component mark for {0}: {1}'.format(self, score))
        return scores

    def _is_first_elt_of_segment(self):
        return not self.elements and self.rank == 1

    def _is_zeroed_element(self, base_value):
        """Sometimes a skater receives no credit for an element when it is invalidated."""
        return self._is_close(0.00, base_value)
