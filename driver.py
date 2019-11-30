import os
import re
import traceback
from tabulate import tabulate

def print_tabular(string):
    string = string.split("\n")
    list = []
    for i in string:
        list.append(tuple(i.split("\t")))
    list = list[:-1]
    #print(list)
    return list


def check_cloumn(string,inp):
    string = string.split(",")
    #print(string)
    inp = inp.split(",")
    #print(inp)
    if(inp[-1] != ")"):
        for i in inp:
            if(i not in string):
                return 0
    else:
        inp = inp[4:-1]
        for i in inp:
            if(i not in string):
                return 0
    return 1

def check_string(inp,schema):
    #inp = inp.split(",")
    schema = schema.split(",")
    #rint(schema)
    dict_sc = {}
    for i in schema:
        dict_sc[i.split(":")[0]] = i.split(":")[1]
    #print(dict_sc)
    if (inp in dict_sc):
        if (dict_sc[inp] == "string"):
            return 1
    return 0

while(1):
    inp = input()
    inp = inp.lower()
    valid = (re.search("^select\s([a-z0-9\*]+)(\,[a-z0-9]+)*\sfrom\s([a-z0-9]+)\/([a-z0-9]+)\.csv\swhere\s([a-z0-9]+)\s(\=|\>|\<|\>=|\<=)\s([a-z0-9]+);$|^load\s([a-z0-9]+)\/([a-z0-9]+)\.csv\sas\s\(([a-z0-9]+)\:(string|int|float)(\,([a-z0-9]+)\:(string|int|float))*\)\;|^delete\s([a-z0-9]+)\;|^select\s(max\(([a-z0-9]+)\)|cnt\(([a-z0-9]+)\)|sum\(([a-z0-9]+)\)|min\(([a-z0-9]+)\)|avg\(([a-z0-9]+)\))\sfrom\s([a-z0-9]+)\/([a-z0-9]+)\.csv\swhere\s([a-z0-9]+)\s(\=|\>|\<|\>=|\<=)\s([a-z0-9]+)\;",inp)!=None)
    if(inp == "exit;"):
        break
    inp = inp.split(" ")
    if(not valid):
        print("[ERROR]:- NOT A VALID QUERY")

    try:
        if __name__=="__main__":
            if(inp[0] == "load" and valid):
                if(len(inp[1].split("/")) == 2):
                    db_name,table = inp[1].split("/")
                    res = os.popen('ls data')
                    output = res.read()
                    output = output.split("\n")
                    output = output[:-1]
                    if(table in output):
                        f = open("schema.txt",'r')
                        schemas = f.read()
                        f.close()
                        schemas = schemas.split("\n")
                        dict_sch = dict()
                        for i in schemas:
                            dict_sch[i.split(" ")[0]] = i.split(" ")[1]
                        if(db_name in dict_sch):
                            print("[ERROR]:-Schema already exists")
                        else:
                            if(inp[-1][-1] == ";"):
                                f = open('schema.txt', 'a')
                                f.write("\n"+db_name + " " + inp[-1][1:-2] + " " + table)
                                f.close()
                                print("DATABASE "+db_name+" IS CREATED WITH TABLE "+ table)
                            else:
                                print("[ERROR]:-expected ;")
                    else:
                        print("[ERROR]:- Table NOT FOUND")
                else:
                    print("[ERROR]:- Invalid Syntax")
    

            if(inp[0] == "select" and valid):
                f = open("schema.txt",'r')
                schemas = f.read()
                f.close()
                schemas = schemas.split("\n")
                dict_sch = dict()
                for i in schemas:
                    dict_sch[i.split(" ")[0]] = i.split(" ")[1],i.split(" ")[2]
                #print(dict_sch)

                list_headers = []
                inp_for_headers = inp[1].split(",")
                for i in inp_for_headers:
                    list_headers.append(i)

                for i in dict_sch: 
                    if((inp[3].split("/")[0] == i) and (inp[3].split("/")[1] == dict_sch[i][1])):
                        #print(dict_sch[i][1])
                        string = ""
                        count = 1
                        schem = dict_sch[i][0]
                        schem = schem.split(",")
                        for l in schem:
                            if(count != len(schem)):
                                string = string + l.split(":")[0]+","
                            else:
                                string = string + l.split(":")[0]
                                #print(string)
                            count+=1
                        #print(string)
                        if(inp[1] == "*"):
                            inp[1] = dict_sch[i][0]
                            inp[1] = inp[1].split(",")
                            #print(inp[1])
                            inp[1] = string
                            list_headers = []
                            inp_for_headers = inp[1].split(",")
                            for k in inp_for_headers:
                                list_headers.append(k)
                        #print(inp[1])
                        check_c = check_cloumn(string,inp[1])
                        #print(check_c)
                        #print(check_s)
                        if(not check_c and inp[1][-1] != ")"):
                            print("[ERROR]:-COLUMN NAME NOT FOUND OR INVALID STRING OPERATION")
                        if(check_string(inp[5],dict_sch[i][0]) and inp[-2] != "="):
                            print("[ERROR]:-INVALID STRING OPERATION")
                        
                        if(inp[-2] == "="):
                            encoded = 1
                        elif(inp[-2] == "<"):
                            encoded = 2
                        elif(inp[-2] == ">"):
                            encoded = 3
                        elif(inp[-2] == "<="):
                            encoded = 4
                        elif(inp[-2] == ">="):
                            encoded = 5

                        if(inp[1][-1] != ")" and check_c and not check_string(inp[5],dict_sch[i][0])):
                            #print(dict_sch[i][1],inp[1],i,inp[5])
                            res = os.popen("cat data/"+dict_sch[i][1]+" "+"|"+" "+"python3 mapper.py "+inp[1]+ " "+i+" "+inp[5] +" "+"|"+" "+"python3 reducer.py "+inp[-1][:-1] + " " + str(encoded))
                            output = res.read()
                            output_list = print_tabular(output)
                            # print(output_list)
                            # print(list_headers)
                        elif(check_cloumn(string,inp[1][4:-1]) and inp[1][-1] == ")" and not check_string(inp[1][4:-1],dict_sch[i][0])):
                                #print(inp[1][4:-1])
                            res = os.popen("cat data/"+dict_sch[i][1]+" "+"|"+" "+"python3 mapper.py "+inp[1][4:-1]+ " "+i+" "+inp[5] +" "+"|"+" "+"python3 reducer1.py "+inp[-1][:-1] + " " + str(encoded)+ " " + inp[1][0:3])
                            #res = os.popen("python3 mapper.py<data/"+dict_sch[i][1]+" "+inp[1][4:-1]+" "+i + " "+inp[5])
                            output = res.read()
                            output_list = print_tabular(output)
                            #print(tuple(output.split("\t")))
                        elif(inp[-2] == "=" and check_string(inp[5],dict_sch[i][0])):
                            res = os.popen("cat data/"+dict_sch[i][1]+" "+"|"+" "+"python3 mapper.py "+inp[1]+ " "+i+" "+inp[5] +" "+"|"+" "+"python3 reducer2.py "+inp[-1][:-1] + " " + str(encoded))
                            output = res.read()
                            output_list = print_tabular(output)                            

                        else:
                            print("[ERROR]:-INVALID AGGREGATE FUNCTION OPERATION.")

                        print(tabulate(output_list,headers=list_headers,tablefmt="grid"))

                        #print(output_list)
                        #print(list_headers)                        
                        #f = open('output_map.txt', 'w')
                        #f.write(output)
                        #print(output)
                        #f.close()

                        # if(inp[1][-1] == ")" and not check_string(inp[1][4:-1],dict_sch[i][0]) and check_cloumn(string,inp[1][4:-1])):
                        #     #print("in")
                        #     res = os.popen('python3 reducer1.py < output_map.txt '+ inp[-1][:-1] + " " + str(encoded)+ " " + inp[1][0:3])
                        # #print(var)
                        #     output = res.read()
                        #     print(output)

                        # elif(not check_s and check_c):
                        # #var = 'python3 reducer.py < output_map.txt '+ inp[-1][:-1] + " " + str(encoded)
                        #     res = os.popen('python3 reducer.py < output_map.txt '+ inp[-1][:-1] + " " + str(encoded))
                        # #print(var)
                        #     output = res.read()
                        #     print(output)
                        #     f = open("output_red.txt","w")
                        #     f.write(output)
                        #     f.close()
                        # if(check_s and check_c):
                        #     res = os.popen('python3 reducer2.py < output_map.txt '+ inp[-1][:-1] + " " + "=")
                        # #print(var)
                        #     output = res.read()
                        #     print(output)
                        #     f = open("output_red.txt","w")
                        #     f.write(output)
                        #     f.close()


                    elif((inp[3].split("/")[0] != i) and(inp[3].split("/")[1] != dict_sch[i][1])):
                        print("[ERROR]:- Database not found")


            if(inp[0] == "delete" and inp[-1][-1] == ";"):
                f = open("schema.txt",'r')
                schemas = f.read()
                f.close()
                schemas = schemas.split("\n")
                del_schema = inp[1][:-1]
                dict_sch={}
        #print(del_schema)
                for i in schemas:
                    dict_sch[i.split(" ")[0]] = [i.split(" ")[1],i.split(" ")[2]]
        #print(schemas)
        #print(dict_sch)
                f = open("schema.txt","w")
                count = 0
                if(del_schema not in dict_sch):
                    print("[ERROR]:-SCHEMA NOT FOUND")

                for i in dict_sch:
                    if(i != del_schema):
                        if(count != (len(del_schema)+1)):
                            f.write(i+" "+dict_sch[i][0]+" "+dict_sch[i][1]+"\n")
                        else:
                            f.write(i+" "+dict_sch[i][0]+" "+dict_sch[i][1])
            #print(count,i)
                    count+=1

                f.close()

    except Exception:
        print("[ERROR]:-UNUSUAL OPERATION")
        #traceback.print_exc()