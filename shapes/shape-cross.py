#!/usr/bin/env python3

n = int(input())
middle = n // 2
i = 0
while i < n:
    if i == middle:
        print('*' * n)
    else:
        print(' ' * middle + '*')
    i = i + 1
