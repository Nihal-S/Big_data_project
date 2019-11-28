#!/usr/bin/python3
import csv
from operator import itemgetter
import sys

list = []

for line in sys.stdin:
    line  = line.strip()
    line = line.split("\t")
    #print(line[1])
    #print(sys.argv[1])
    #print(len(sys.argv))
    if(sys.argv[2] == "1"):
        if(float(line[1]) == float(sys.argv[1])):
            #list = []
            selected = line[0].split(",")
            #print(selected)
            for i in selected:
                list.append(float(i))
                #print(list)
    if(sys.argv[2] == "3"):
        if(float(line[1]) > float(sys.argv[1])):
            #list = []
            selected = line[0].split(",")
            #print(selected)
            for i in selected:
                list.append(float(i))
    if(sys.argv[2] == "2"):
        if(float(line[1]) < float(sys.argv[1])):
            #list = []
            selected = line[0].split(",")
            #print(selected)
            for i in selected:
                list.append(float(i))
    if(sys.argv[2] == "5"):
        if(float(line[1]) >= float(sys.argv[1])):
            #list = []
            selected = line[0].split(",")
            #print(selected)
            for i in selected:
                list.append(float(i))
    if(sys.argv[2] == "4"):
        if(float(line[1]) <= float(sys.argv[1])):
            #list = []
            selected = line[0].split(",")
            #print(selected)
            for i in selected:
                list.append(float(i))
print(list)
print(sys.argv[3])

if(sys.argv[3] == "min"):
    print(min(list))
if(sys.argv[3] == "max"):
    print(max(list))
if(sys.argv[3] == "sum"):
    print(sum(list))
if(sys.argv[3] == "avg"):
    print(sum(list)/float(len(list)))
if(sys.argv[3] == "con"):
    print(len(list))
