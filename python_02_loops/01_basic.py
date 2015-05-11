#! /usr/bin/python

import csv

with open('data.csv', 'rb') as d:
    first  = True
    reader = csv.reader(d)

    for row in reader:
        print row
