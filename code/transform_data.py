# Season -> components data frame

men = []
ladies = []
pairs = []
dance = []
components = [men, ladies, pairs, dance]
for season in seasons.values():
    for event in season.events:
        for dis_ind, discipline in enumerate(event.disciplines):
            for segment in discipline.segments:
                for scorecard in segment.scorecards:
                    for component in scorecard.components:
                        for judge, score in enumerate(component.parsed_scores):
                            judge_name = remove_mr_ms(segment.panel.judges[judge].name) if int(season.champ_year) > 2016 else ''
                            if judge_name in judge_name_fixes:
                                judge_name = judge_name_fixes[judge_name]
                            components[dis_ind].append({
                                'Component Name': component.name,
                                'Factor': float(component.factor),
                                'Score': float(score),
                                'Judge': judge_name,
                                'Judge Nation': segment.panel.judges[judge].nation if int(season.champ_year) > 2016 else '',
                                'Judge Number': judge + 1,
                                'Final Points': float(component.points),
                                'Skater': scorecard.skater.name,
                                'Skater Nation': scorecard.skater.country,
                                'TES': scorecard.tes,
                                'PCS': scorecard.pcs,
                                'Base Value': scorecard.base_value,
                                'Segment Rank': scorecard.rank,
                                'Start': scorecard.starting_number,
                                'Dedutions': scorecard.total_deductions,
                                'Segment': segment.name,
                                'Season': season.champ_year,
                                'Event': event.name,
                                'Discipline': str(discipline.discipline).replace('DisciplineType.','')
                            })

for wrong_name, right_name in (('Performance / Execution', 'Performance'),
                               ('Composition / Choreography', 'Composition'),
                               ('Choreography / Composition', 'Composition'),
                               ('Choreography', 'Composition'),
                               ('Linking Footwork / Movement', 'Transitions'),
                               ('Transitions / Linking Footwork / Movement', 'Transitions'),
                               ('Interpretation of the Music / Timing', 'Interpretation'),
                               ('Interpretation / Timing', 'Interpretation'),
                               ('Interpretation of the Music', 'Interpretation'),
                               ('Transition / Linking Footwork', 'Transitions'),
                               ('Transitions / Linking Footwork', 'Transitions')):
    pairs.loc[pairs['Component Name'] == wrong_name, 'Component Name'] = right_name

for i, (fname, data) in enumerate((('men', men), ('ladies', ladies), ('pairs', pairs), ('dance', dance))):
    df = pd.DataFrame(data)
    df.to_csv('pd_data/components_' + fname + '.csv')
    # plt.figure(i)
    # df.Score.hist()
    # plt.title(fname)


### Fixing names
def ascii_encode_dict(data):
    ascii_encode = lambda x: x.encode('ascii')
    return dict(map(ascii_encode, pair) for pair in data.items())

with open('pd_data/name_fixes_men.json') as f:
    men_name_fixes = f.read()
men_name_fixes = json.loads(men_name_fixes, object_hook=ascii_encode_dict)


#### Removing WDs and gpfra2015
for discipline in skaters:
    skaters[discipline] = skaters[discipline][skaters[discipline].Points != 'WD']
    skaters[discipline] = skaters[discipline][skaters[discipline].Event != 'gpfra2015']

### getting start numbers from row.
events = {}
for season in seasons.values():
    events.update(season.event_dict)

def dance_od_entries(row):
    if row['OD Rank'] == 'WD':
        return None
    elif not pd.isnull((row['OD Rank'])):
        return len(events[row.Event].disciplines[3].segments[1].scorecards)
    else:
        return None

def get_od_start(row):
    if pd.isnull(row['OD Rank']) or row['OD Rank'] in ('WD', 'DNQ'):
        return None
    start = events[row.Event].disciplines[-1].segments[1].scorecards[int(row['OD Rank'])-1].starting_number
    if start == 0:
        return None
    return start

def get_fd_start(row):
    if row['Free Rank'] in ('WD', 'DNQ'):
        return None
    index = 2
    if pd.isnull(row['OD Rank']):
        index = 1
    start = events[row.Event].disciplines[-1].segments[index].scorecards[int(row['Free Rank'])-1].starting_number
    if start == 0:
        return None
    return start
    
def get_start(row, discipline_i, segment_i, segment_rank_name):
    if row[segment_rank_name] == 'WD' or row[segment_rank_name] == 'DNQ':
        return None
    start = events[row.Event].disciplines[discipline_i].segments[segment_i].scorecards[int(row[segment_rank_name])-1].starting_number
    if start == 0:
        return None
    return start

for i, discipline in enumerate(('men', 'ladies', 'pairs', 'dance')):
    print i, discipline
    skaters[discipline]['Short Start'] = skaters[discipline].apply(lambda row: get_start(row, i, 0, 'Short Rank'), axis=1)
    if discipline != 'dance':
#         skaters[discipline]['OD Start'] = skaters[discipline].apply(dance_od_entries, axis=1)
        skaters[discipline]['Free Start'] = skaters[discipline].apply(lambda row: get_start(row, i, 1, 'Free Rank'), axis=1)

# Regenerating results_nowd_..._ladies.csv
all_ladies_results = []
for season in seasons.values():
    for event in season.events:
        if event.name == 'gpfra2015':
            continue
        discipline = event.disciplines[1]
        df = pd.read_csv(discipline.results_csv)
        if df.dtypes['Short Rank'] != np.dtype('int64'):
            df = df[df['Short Rank'] != 'WD']
        num_short = len(df)
        num_free = np.max([int(rank) for rank in df['Free Rank'] if rank not in ('DNQ', 'WD')])
        df['Num Short Scorecards'] = pd.Series([num_short for _ in xrange(num_short)])
        df['Num Free Scorecards'] = pd.Series([num_free for _ in xrange(num_short)])
        df['Season'] = pd.Series([season.champ_year for _ in xrange(num_short)])
        
        df['Short Start'] = df.apply(lambda row: discipline.segments[0].scorecards[int(row['Short Rank']) - 1].starting_number, axis=1)
        df['Free Start'] = df.apply(lambda row:
                             None if str(row['Free Rank']).isalpha() else
                             discipline.segments[1].scorecards[int(row['Free Rank']) - 1].starting_number, 
                             axis=1)
        
        df.Name = df.apply(lambda row: name_fixes_ladies.get(row.Name, row.Name), axis=1)
        
        all_ladies_results.append(df)