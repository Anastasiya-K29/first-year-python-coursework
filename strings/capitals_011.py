#!/usr/bin/env python3

import sys
for line in sys.stdin:
    s = line.strip()
    print(s[0].upper() + s[1:len(s) - 1] + s[len(s) - 1].upper())
