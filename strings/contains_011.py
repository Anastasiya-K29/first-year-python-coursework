#!/usr/bin/env python3

import sys
for line in sys.stdin:
    parts = line.strip().split()
    first = parts[0].lower()
    second = parts[1].lower()
    result = True
    i = 0
    while i < len(first):
        if first[i] in second:
            second = second.replace(first[i], '', 1)
        else:
            result = False
        i = i + 1
    print(result)
