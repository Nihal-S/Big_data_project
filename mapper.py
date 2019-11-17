#!/usr/bin/python3
import sys
import csv
infile = sys.stdin
#next(infile)
start = 2
columns = sys.argv[1]
columns = columns.split(",")
l=[]
#print(columns)
f = open("schema.txt",'r')
schemas = f.read()
f.close()
schemas = schemas.split("\n")
for i in schemas:
    if(i.split(" ")[0] == sys.argv[2]):
        schema = (i.split(" ")[1]).split(",")
        #print(schema)
        for j in range(len(schema)):
            if(schema[j] in columns):
                l.append(j)
#fuel column index 8
#print(l)
#l = [0,2,3]
for line in infile:
    string = ""
    if(start == 0):
        line = line.strip()
        list = line.split(';')
        #print(list)
        for j in range(len(list)):
            if(j in l):
                if (string != ""):
                    string = string + "," + list[j]
                else:
                    string = list[j]
        print(string)



    else:
        start -= 1