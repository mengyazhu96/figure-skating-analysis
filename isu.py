from lxml import html, etree
import requests

# seasons = ['season1516', 'season1617']
seasons = ['season1314', 'season1415']
gps = ['usa', 'can', 'chn', 'rus', 'fra', 'jpn']
gps = ['gp' + gp for gp in gps]
# gp_years = ['2015', '2016']
gp_years = ['2009', '2010']
champs = ['ec', 'fc', 'wc']
champ_years = [str(int(year) + 1) for year in gp_years]
gpf_years = ['0809', '0910']

all_events = []
for s, season in enumerate(seasons):
	events = [gp + gp_years[s] for gp in gps]
	events.append('gpf' + gpf_years[s])
	events += [champ + champ_years[s] for champ in champs]
	events = map(lambda event_name: event_name, events)
	# events = map(lambda event_name: event_name + '/' + event_name + '_Men_SP_Scores.pdf', events)
	all_events += events

for event in all_events:
	page = requests.get('http://www.isuresults.com/results/' + event)
	# print len(page.content), 
	# if len(page.content) < 10:
	# 	print event
	try:
		tree = html.fromstring(page.content)
	except etree.ParserError:
		print 'Event not found: % s' % event
		continue

	if not list(tree.iter('title')):
		print 'Event not found: % s' % event
	else:
		print list(tree.iter('title'))[0].text