#!/usr/bin/python3
import csv
from operator import itemgetter
import sys

current_count = 0
current_key = ""
for line in sys.stdin:
    line = line.strip()
    line_val = line.split("\t")
    key, val = line_val[0], line_val[1]
    try:
        count = int(val)
    except ValueError:
        continue
    global current_key
    global current_count
    if current_key == key:
        current_count += count
    else:
    	if (current_key != ""):
        	print('%s\t%s' % (current_key,str(current_count)))
        current_count = 1
        current_key = key

if current_key == key:
    print '%s\t%s' % (current_key, current_count)