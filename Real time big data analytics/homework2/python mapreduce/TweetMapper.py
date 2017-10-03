#!/usr/bin/env python

from sys import stdin

search_terms = ["hackathon", "Dec", "Chicago", "Java"]

for line in stdin:
    line = line.strip()
    line = line.lower() # we make everything lower case
    for term in search_terms:
        if line.find(term.lower()) == -1:
            found = 0
        else:
            found = 1
        print(term + ' ' + str(found))