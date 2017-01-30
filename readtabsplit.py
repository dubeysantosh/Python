#!/usr/bin/python

with open('datafile.tsv') as f:
    for line in f:
        line = line.strip()
        print (line.split('\t'))