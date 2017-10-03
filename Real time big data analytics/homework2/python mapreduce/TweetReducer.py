#!/usr/bin/env python

from sys import stdin

count = 0
previous_key = None
for line in stdin:
    (key, value) = line.strip().split(' ')
    if previous_key and previous_key != key:
        print(previous_key + ' ' + str(count))
        count = 0
    try:
        value = int(value)
    except TypeError:
        continue # we go to the next line if the value is not an integer
    count += value
    previous_key = key

if previous_key:
    print(previous_key + ' ' + str(count))