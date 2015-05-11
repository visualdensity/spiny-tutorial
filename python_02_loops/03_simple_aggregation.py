#! /usr/bin/python

import csv

totalImpressions = 0;

with open('data.csv', 'rb') as d:
    first  = True
    reader = csv.reader(d)

    for row in reader:
        if first == True:
            first = False
            continue

        totalImpressions += int(row[2])

    print "Total Impressions: %d" % totalImpressions
