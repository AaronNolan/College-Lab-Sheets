#!/usr/bin/env python

s = raw_input()
while s != "end":
    #Create a list of the individual parts of the string
    l = s.split()
    print l[3]
    s = raw_input()
