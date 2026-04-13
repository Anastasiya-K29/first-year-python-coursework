#!/usr/bin/env python3

import sys
for line in sys.stdin:
    s = line.strip()
    words = s.split(' ')
    found = False
    i = 0
    while i < len(words):
        if found is False and words[i] and words[i][0] == 'm':
            words[i] = words[i].capitalize()
            found = True
        i = i + 1
    print(' '.join(words))
