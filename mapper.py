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
v = 0
for i in schemas:
    new_schema = []
    if(i.split(" ")[0] == sys.argv[2]):
        schema = ((i.split(" ")[1]).split(","))
        for x in schema:
            new_schema.append(x.split(":")[0])
        #print(new_schema)
        schema = new_schema
        #print(schema)
        for j in range(len(schema)):
            if(schema[j] in columns):
                l.append(j)
            if(sys.argv[3] == schema[j]):
                v = j
            
#fuel column index 8
#print(v)
#l = [0,2,3]
for line in infile:
    string = ""
    if(start == 0):
        line = line.strip()
        list = line.split(',')
        #print(list)
        for j in range(len(list)):
            if(j in l):
                if (string != ""):
                    string = string + "," + list[j]
                else:
                    string = list[j]
            if(j == v):
                value = list[v]

        print(string + "\t" +value)



    else:
        start -= 1