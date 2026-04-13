#!/usr/bin/env python3

import sys
for line in sys.stdin:
    parts = line.strip().split()
    first = parts[0]
    second = parts[1]
    if first.lower() in second.lower():
        print('True')
    else:
        print('False')
