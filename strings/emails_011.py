#!/usr/bin/env python3

import sys
for line in sys.stdin:
    s = line.strip()
    name = s.split('@')[0]
    parts = name.split('.')
    first = parts[0]
    last = ''.join([c for c in parts[1] if not c.isdigit()])
    print(first.capitalize() + ' ' + last.capitalize())
