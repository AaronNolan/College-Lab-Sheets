#!/usr/bin/env python

#Create a list of all the strings
s = raw_input()
l = []
while s != "end":
    l.append(s)
    s = raw_input()

#Get the day we are searching for
day = input()

#go through each string and print if true
i = 0
while i < len(l):
    s = l[i].split()
    if s[0] == str(day):
        print("".join(l[i]))
    i += 1
