import requests
import os

def get_fpath(season, event, fname):
    return season.year + '/' + event.name + '/' + fname

def get_page(url, season, event, fname):
    target_dir = season.year + '/' + event.name + '/'
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)
    page = requests.get(url)
    with open(target_dir + fname, 'w+') as f:
        f.write(page.content)