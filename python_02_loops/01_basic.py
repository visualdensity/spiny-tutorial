#! /usr/bin/python
import csv

total = 0

with open('data.csv', 'rb') as data:

    isFirstRow = True
    reader = csv.reader(data)

    for row in reader:

        if isFirstRow == True:
            isFirstRow = False
            continue
        
        total += int(row[3])

    print total
