#!/usr/bin/env python

from sys import stdin
from re import match

separator = ' '
MISSING = "9999"
# input comes from STDIN (standard input)
for line in stdin:
    line = line.strip()
    year = line[15:19]
    airTemperature = line[40:45]
    quality = line[45:46]
    if airTemperature != MISSING and match("[01459]", quality):
        print(year + separator + airTemperature)