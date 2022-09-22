"""
Helps in finding all subsequences of a given string. 
The function combinations() by default gives all possible substrings, but the below modified version gives us subsequences. 

Source: https://stackoverflow.com/a/59419343
"""
import itertools


def get_subsequences(s):
    out = set()
    for r in range(1, len(s) + 1):
        for c in itertools.combinations(s, r):
            out.add(''.join(c))
    return sorted(out, key=lambda x: len(x), reverse=True)
