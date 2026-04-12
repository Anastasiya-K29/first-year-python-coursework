#!/usr/bin/env python3

n = int(input())
middle = n // 2
i = 0
while i < n:
    if i == middle:
        print(' ' * middle + '*')
    else:
        if i < middle:
            leading = i
        else:
            leading = n - 1 - i
        inner = n - 2 - leading * 2
        print(' ' * leading + '*' + ' ' * inner + '*')
    i = i + 1
