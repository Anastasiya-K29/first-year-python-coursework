#!/usr/bin/env python3

s = input()
t = ''
i = 0
while i < len(s):
    if 'a' <= s[i] <= 'z':
        t = t + chr(ord(s[i]) - 32)
    else:
        t = t + s[i]
    i = i + 1
print(t)
