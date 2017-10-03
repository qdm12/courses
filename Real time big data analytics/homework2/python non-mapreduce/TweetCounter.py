#!/usr/bin/env python

from sys import stdin

search_terms = ["hackathon", "Dec", "Chicago", "Java"]

counters = dict()
for term in search_terms:
    counters[term] = 0

for line in stdin:
    line = line.strip()
    line = line.lower() # we make everything lower case
    for term in counters:
        if line.find(term.lower()) != -1:
            counters[term] += 1 # increments the right counter

for term in sorted(search_terms):
    print(term + ' ' + str(counters[term]))