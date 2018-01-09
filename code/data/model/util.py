import os
import requests
import shutil


def check_and_make_dir(target_dir):
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)

def clear_and_make_dir(target_dir):
    if os.path.isdir(target_dir):
        shutil.rmtree(target_dir)
    os.makedirs(target_dir)

# Convert string to float, allowing for commas.
def float_of(str_float):
    return float(str_float.replace(',', '.'))

def get_fpath(season, event, fname):
    return season.year + '/' + event.name + '/' + fname

def get_page(url, season, event, fname):
    target_dir = season.year + '/' + event.name + '/'
    check_and_make_dir(target_dir)
    page = requests.get(url)
    with open(target_dir + fname, 'w+') as f:
        f.write(page.content)