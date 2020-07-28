#!/usr/bin/env python

def get():
    l = []
    s = raw_input()
    while s != "end":
        l.append(s)
        s = raw_input()
    return l
