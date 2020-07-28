#!/usr/bin/env python

import dictionary

if dictionary.has("duck") is True:
  print "duck: " + dictionary.get("duck") + "."

if dictionary.has("goose") is True:
  print "goose: " + dictionary.get("goose") + "."

dictionary.set("lion", "Big cat")
