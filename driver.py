import os
inp = input()
inp = inp.lower()
inp = inp.split(" ")

if(inp[0] == "load"):
    if(len(inp[1].split("/")) == 2):
        db_name,table = inp[1].split("/")
        res = os.popen('ls data')
        output = res.read()
        output = output.split("\n")
        output = output[:-1]
        if(table in output):
            f = open("schemas.txt",'r')
            schemas = f.read()
            f.close()
            schemas = schemas.split("\n")
            dict_sch = dict()
            for i in schemas:
                dict_sch[i.split(" ")[0]] = i.split(" ")[1]
            
            # f = open('schemas.txt', 'a')
            # f.write("stuff")
            # f.close()
        else:
            print("[ERROR]:- Table NOT FOUND")


    else:
        print("[ERROR]:- Invalid Syntax")


print(inp)