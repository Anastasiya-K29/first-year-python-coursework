#!/usr/bin/env python3

import sys
lines = sys.stdin.read().strip().split('\n')
water = int(lines[0])
buckets = lines[1].split()
count = 0
i = 0
while i < len(buckets):
    bucket = int(buckets[i])
    if water >= bucket:
        water = water - bucket
        count = count + 1
    else:
        break
    i = i + 1
print(count)
