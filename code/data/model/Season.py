from Event import Event

class Season:
    def __init__(self, spring_str_rep):
        champ_year = spring_str_rep
        two_digit_season = int(spring_str_rep[2:])
        gp_year = '0' + str(two_digit_season - 1)
        if two_digit_season > 10:
            twotwo_year = str(two_digit_season - 1) + str(two_digit_season)
            gp_year = str(int(spring_str_rep) - 1)
        elif two_digit_season <= 9:
            twotwo_year = gp_year + '0' + str(two_digit_season)
        else:
            twotwo_year = gp_year + str(two_digit_season)

        gpf_year = twotwo_year
        
        if int(spring_str_rep) % 4 == 2:
            champs = ['ec', 'fc', 'owg', 'wc']
        else:
            champs = ['ec', 'fc', 'wc']
        gps = ['usa', 'can', 'chn', 'rus', 'fra', 'jpn']
        gps = ['gp' + gp for gp in gps]
        
        self.year = twotwo_year
        
        event_names = [gp + gp_year for gp in gps]
        event_names.append('gpf' + twotwo_year)
        event_names += [champ + champ_year for champ in champs]
        
        self.url = 'http://www.isuresults.com/results/'
        if int(spring_str_rep) >= 2016:
            self.url += 'season'+ twotwo_year + '/'

        self.events = [Event(self, event_name) for event_name in event_names]

    def fetch_info(self, fetch_files=False):
        for event in self.events:
            event.fetch_info(fetch_files)

    def load_scores(self, reparse=False):
        for event in self.events:
            event.parse_csvs(reparse)

    def __repr__(self):
        return '\'' + self.year[:2] + '-\'' + self.year[2:]