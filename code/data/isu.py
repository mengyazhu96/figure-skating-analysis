#!/usr/bin/env python

from lxml import html, etree
import requests
import sys


def get_events(seasons):

    # i.e. 10
    two_digit_seasons = [int(season[2:]) for season in seasons]

    # i.e. 0910
    two_to_two_seasons = [str(season - 1) + str(season) for season in two_digit_seasons]

    season_urls = ['season' + season for season in two_to_two_seasons]
    gp_years = [str(int(season) - 1) for season in seasons]
    champ_years = seasons
    gpf_years = two_to_two_seasons

    champs = ['ec', 'fc', 'wc']
    gps = ['usa', 'can', 'chn', 'rus', 'fra', 'jpn']
    gps = ['gp' + gp for gp in gps]

    all_events = []
    for s, season in enumerate(season_urls):  # season_url only used for 15-16, 16-17
        events = [gp + gp_years[s] for gp in gps]
        events.append('gpf' + gpf_years[s])
        events += [champ + champ_years[s] for champ in champs]
        events = map(lambda event_name: event_name, events)
        # events = map(lambda event_name: event_name + '/' + event_name + '_Men_SP_Scores.pdf', events)
        all_events += events
    return all_events

def print_events(events):
    for event in events:
        page = requests.get('http://www.isuresults.com/results/' + event)
        try:
            tree = html.fromstring(page.content)
        except etree.ParserError:
            print 'Event not found: % s' % event
            continue

        if not list(tree.iter('title')):
            print 'Event not found: % s' % event
        else:
            print list(tree.iter('title'))[0].text

if __name__ == '__main__':
    seasons = ['2014', '2015']
    if len(sys.argv) > 1:
        seasons = sys.argv[1:]
    events = get_events(seasons)
    print_events(events)