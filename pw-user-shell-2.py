#!/usr/bin/env python

s = raw_input()
l = []
while s != "end":
    l.append(s)
    s = raw_input()

i = 0
while i < len(l):
    s = l[i].split(":")
    if s[len(s) - 1] != "/bin/false":
        if s[len(s) - 1] != "/usr/sbin/nologin":
            print(s[0] + " " + "".join(s[len(s) - 1]))
    i += 1
