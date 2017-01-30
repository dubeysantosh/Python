#!/usr/bin/python

import csv
import sys

data = []

filename = "/tmp/sample.csv"

try:
    with open(filename) as f:
        reader = csv.reader(f)
        c = 0
        for row in reader:
            if c == 0 :
                header = row
            else:
                data.append(row);
            c += 1

except csv.Error as e:
    print("CSV errors on line %s : %s", (reader.line_enum , e))
    sys.exit(-1)

if header:
    print(header)
    print("===========================")

for datarow in data:
    print (datarow)