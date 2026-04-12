#!/usr/bin/env python3

s = input()
t = ''
is_first = True
i = 0
while i < len(s):
    if s[i].isalpha():
        if is_first is True:
            if ord(s[i]) >= 65 and ord(s[i]) <= 90:
                t = t + chr(ord(s[i]) + 32)
            else:
                t = t + s[i]
        else:
            if ord(s[i]) >= 97 and ord(s[i]) <= 122:
                t = t + chr(ord(s[i]) - 32)
            else:
                t = t + s[i]
        is_first = not is_first
    else:
        t = t + s[i]
    i = i + 1
print(t)
