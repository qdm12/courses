#!/usr/bin/env python

from sys import stdin

previous_key = None
separator = ' '
value_output = ''
PR = 0.00

for line in stdin:
    
    # Gets the key and value from the line
    (key, value) = line.strip().split(separator, 1)
            
    if previous_key and previous_key != key:
        value_output += str(PR)
        print(previous_key + separator + value_output)
        PR = 0.00
        value_output = ''
        
    if value.count(' ') != 1: # Zero or >1 spaces, then (source, targets)
        # We try for single nodes with only a PR value
        try:
            PR = float(value)
        except:
            value_output = value + ' ' # targets of key (source)
    else:
        source, PRperLink = value.split(' ')
        try:
            PRperLink = float(PRperLink)
        except ValueError: # Two outlinks B C from source A
            value_output = value + ' ' # targets of key (source)
        else:
            PR += PRperLink
    previous_key = key

if previous_key:
    value_output += str(PR)       
    print(previous_key + separator + value_output)