#!/usr/bin/env python

from sys import stdin

separator = ' '
previous_key = None
maxValue = -9999999999999999
for line in stdin:
    (key, value) = line.strip().split(separator)
    if previous_key and previous_key != key:
        print(previous_key + separator + maxValue)
        maxValue = value
    else: #initial branch
        maxValue = str(max(int(maxValue), int(value)))
    previous_key = key
    
if previous_key:
    print(previous_key + separator + maxValue)