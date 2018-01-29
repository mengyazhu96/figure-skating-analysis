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

def float_of(str_float):
    """Convert string to float, allowing for commas."""
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
    """Edit distance."""
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


def get_similar_names(skaters):
    """Returns similar and first-last swaps of judges or skaters."""
    def get_first_last(single_skater):
        split = single_skater.split()
        if len(split) != 2:
            return None
        return split[0].lower(), split[1].lower()
    similar = []
    first_last = {}
    num_skaters = len(skaters)
    for i in xrange(num_skaters):
        split_i = get_first_last(skaters[i])
        for j in xrange(i + 1, num_skaters):
            added = False
            split_j = get_first_last(skaters[j])
            if split_i and split_j:
                if levenshtein(split_i[0], split_j[1]) < 3 and levenshtein(split_i[1], split_j[0]) < 3:
                    if skaters[j][-1].islower():
                        first_last[skaters[j]] = skaters[i]
                    else:
                        first_last[skaters[i]] = skaters[j]
                    added = True
            if not added and levenshtein(skaters[i], skaters[j]) < 7:
                similar.append((skaters[i], skaters[j]))     
    return similar, first_last


def ascii_encode_dict(data):
    ascii_encode = lambda x: x.encode('ascii')
    return dict(map(ascii_encode, pair) for pair in data.items())


def remove_mr_ms(name):
    name = name.replace('Mr. ', '')
    name = name.replace('Mr ', '')
    name = name.replace('Ms. ', '')
    name = name.replace('Ms ', '')
    name = name.replace('Mrs. ', '')
    return name