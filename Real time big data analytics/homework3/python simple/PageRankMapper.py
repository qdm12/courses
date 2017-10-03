#!/usr/bin/env python

from sys import stdin

separator = ' '
for line in stdin:
    line = line.strip()
    
    # Source
    indexA = line.find(separator)
    indexB = indexA + 1
    for i in range(indexA+1, len(line)):
        if line[i] != separator:
            indexB = i
            break
    source = line[:indexA]
    line = line[indexB:]
    
    # PR
    PR = float(line[line.rfind(separator)+1:])
    indexB = line.rfind(separator)
    if indexB < 0:
        line = ''
    else:
        line = line[:indexB]
    
    # Outlink targets
    outlink_targets = []
    start = 0
    for i in range(len(line)):
        if line[i] == separator:
            outlink_targets.append(line[start:i])
            start = i+1
        elif i == len(line) - 1:
            outlink_targets.append(line[start:])
            
    # PR per outlink
    PRperLink = PR
    if len(outlink_targets) > 1:
        PRperLink /= len(outlink_targets)
    

    # Writing to reducers
    # Prints (target, source + PRperLink)
    for target in outlink_targets:
        key = target
        value = source + separator + str(PRperLink)
        print(key + separator + value)
    
    key = source
    if len(outlink_targets) > 0:
        # Prints (source, targets) = original data
        value = separator.join(outlink_targets)
        print(key + separator + value)
    else:
        # Prints (source, PR) = original data
        print(key + separator + str(PR))

