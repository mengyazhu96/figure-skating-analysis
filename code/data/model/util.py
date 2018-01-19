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

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    s1 = s1.lower()
    s2 = s2.lower()
    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]