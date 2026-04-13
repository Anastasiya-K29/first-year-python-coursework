#!/usr/bin/env python3

import sys
for line in sys.stdin:
    s = line.strip()
    if len(s) > 2:
        print(s[1:len(s) - 1])
