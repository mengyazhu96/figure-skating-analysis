class Result:
    def __init__(self, discipline, skater):
        self.discipline = discipline
        self.skater = skater
        
        self.rank = None
        self.short_rank = None
        self.short_score = None
        self.free_rank = 'DNQ'
        self.free_score = 'DNQ'
        self.original_rank = None
        self.total_score = 0.00

    def add_short(self, short_scorecard):
        self.short_scorecard = short_scorecard
        self.short_rank = self.short_scorecard.rank
        self.short_score = self.short_scorecard.total_score
        self.total_score = self.short_score

    def add_free(self, free_scorecard):
        self.free_scorecard = free_scorecard
        self.free_rank = self.free_scorecard.rank
        self.free_score = self.free_scorecard.total_score
        self.total_score += self.free_score
    
    def add_original(self, original_scorecard):
        self.original_scorecard = original_scorecard
        self.original_rank = self.original_scorecard.rank
        self.original_score = self.original_scorecard.total_score
        self.total_score += self.original_score

    def __gt__(self, result2):
        if self.total_score == result2.total_score:
            return self.free_score < result2.free_score
        return self.total_score < result2.total_score

    def __lt__(self, result2):
        return not self.__gt__(result2)

    def __ge__(self, result2):
        return self.__gt__(result)
    
    def __le__(self, result2):
        return self.__lt__(result)

    def __str__(self):
        rep = '{0}: {1} {2} {3}'.format(self.discipline, self.skater.name, self.skater.country, self.total_score)
        if self.rank:
            rep += str(self.rank)
        rep += '\n  Short {0} {1}'.format(self.short_rank, self.short_score)
        if self.original_rank:
            rep += '\n  OD {0} {1}'.format(self.original_rank, self.original_score)
        rep += '\n  Free {0} {1}'.format(self.free_rank, self.free_score)
        return rep

def create_discipline_results(discipline):
    skater_results = {}
    for scorecard in discipline.segments[0].scorecards:
        skater = scorecard.skater
        skater_results[skater] = Result(discipline, skater)
        skater_results[skater].add_short(scorecard)
    free_index = 1
    if len(discipline.segments) == 3:       # there is an OD segment
        for scorecard in discipline.segments[1].scorecards:
            skater_results[scorecard.skater].add_original(scorecard)
        free_index += 1
    if len(discipline.segments) > free_index:
        for scorecard in discipline.segments[free_index].scorecards:
            skater_results[scorecard.skater].add_free(scorecard)
    return sorted(skater_results.values())