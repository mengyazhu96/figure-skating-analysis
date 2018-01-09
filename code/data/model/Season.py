from Event import Event

class Season:
    def __init__(self, spring_str_rep):
        champ_year = spring_str_rep
        gp_year = str(int(spring_str_rep) - 1)
        two_digit_season = int(spring_str_rep[2:])
        if two_digit_season <= 9:
            twotwo_year = '0' + str(two_digit_season - 1) + '0' + str(two_digit_season)
        elif two_digit_season <= 10:
            twotwo_year = '0' + str(two_digit_season - 1) + str(two_digit_season)
        else:
            twotwo_year = str(two_digit_season - 1) + str(two_digit_season)
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
            if event.name == 'gpfra2015':
                print 'GP France 2015 was cancelled partway through.'
                continue
            event.fetch_info(fetch_files)

    def load_scores(self):
        for event in self.events:
            event.parse_csvs()

    def __repr__(self):
        return '\'' + self.year[:2] + '-\'' + self.year[2:]