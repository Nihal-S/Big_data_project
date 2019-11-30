#!/usr/bin/python3
import csv
from operator import itemgetter
import sys

for line in sys.stdin:
    line  = line.strip()
    line = line.split("\t")
    #print(line[1])
    #print(sys.argv)
    #print(line)
    #print(len(sys.argv))
    if(sys.argv[2] == "1"):
        #print(str(line[1]))
        #print(str(sys.argv[1]))
        if(str(line[1]) == str(sys.argv[1])):
            string = ""
            selected = line[0].split(",")
            #print(selected)
            for i in selected:
                if(string == ""):
                    string = i
                else:
                    string = string + "\t" + i
            print(string + "")