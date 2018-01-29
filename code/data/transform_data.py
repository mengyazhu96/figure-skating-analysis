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
