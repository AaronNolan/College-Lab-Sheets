#!/usr/bin/env python

#Create a list of all the strings
s = raw_input()
l = []
while s != "end":
    l.append(s)
    s = raw_input()

# go through each string and print if true
i = 0
a = []
while i < len(l):
    s = l[i]
    start_n = s[2:4]  # Staring Hour
    if start_n == "09":
        start_n = "9"
    end_n = int(start_n) + int(s[5]) - 1  # Ending Hour
    print(s[0:2] + start_n + ":00 " + str(end_n) + ":50" + s[6:])
    i += 1
