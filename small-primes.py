#!/usr/bin/env python

n = input()

if n == 1:
    print str(n) + " is not a prime"
elif n == 2 or n == 3:
    print str(n) + " is a prime"
elif n % 2 != 0 and n % 3 != 0:
    print str(n) + " is a prime"
else:
    print str(n) + " is not a prime"
