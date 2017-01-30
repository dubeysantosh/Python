#!/usr/bin/python

import sys
import csv

filename = "/tmp/sample.csv"

data = []

try:
   with open(filename) as f:
       reader = csv.reader(f)
       c = 0
       for row in reader:
           if c == 0:
               header = row
           else:
               data.append(row)
           c += 1
except csv.Error as e:
    print("csv.error at line %s : %s" , (reader.line_enum, e))


if header:
   print "header"
   print "==================================="
for datarow in data:
   print datarow
