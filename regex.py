import re
string1="load databsename/table8name.csv as (columnname:int,columnname:string);"
string="select * from database/tabelname.csv where columnname = value;"
string2="delete suman;"
string3="select max(tablename) from database/tablename.csv where columnname = 100;"
print(re.search("^select\s([a-z0-9\*]+)(\,[a-z0-9]+)*\sfrom\s([a-z0-9]+)\/([a-z0-9]+)\.csv\swhere\s([a-z0-9]+)\s\=\s([a-z0-9]+);$|^load\s([a-z0-9]+)\/([a-z0-9]+)\.csv\sas\s\(([a-z0-9]+)\:(string|int|float)(\,([a-z0-9]+)\:(string|int|float))*\)\;|^delete\s([a-z0-9]+)\;|^select\s(max\(([a-z0-9]+)\)|cnt\(([a-z0-9]+)\)|sum\(([a-z0-9]+)\)|min\(([a-z0-9]+)\)|avg\(([a-z0-9]+)\))\sfrom\s([a-z0-9]+)\/([a-z0-9]+)\.csv\swhere\s([a-z0-9]+)\s=\s([a-z0-9]+)\;",string1)!=None)









'''while True:
	if not re.search("^select|^load|^delete/s[a-z]*/sFROM/s[a-z]*//[a-z]*/.CSV/swhere/s[a-z]/s=/s[a-z]",string):
		break
	elif not re.search(";?",string):
		break
	
	else:
		print("valid")
print("invalid")'''
