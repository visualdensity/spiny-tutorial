#!/usr/bin/python

my_list = range(5,100)

for each_list_item in my_list:
        counter = 0
        string  = ""

        while counter < each_list_item:
            string += "."
            counter += 1;

        print string

print "Done!!"
