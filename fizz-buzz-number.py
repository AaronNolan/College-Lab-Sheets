#!/usr/bin/env python

n = input()

if n % 5 == 0:
    if n % 3 == 0:
        print "fizz-buzz"
    else:
        print "buzz"
elif n % 3 == 0:
    print "fizz"
else:
    print n
