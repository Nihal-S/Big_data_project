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
                if():
                f = open('schema.txt', 'a')
                f.write("\n"+db_name + " " + inp[-1][1:-2])
                f.close()
                print("DATABASE "+db_name+" IS CREATED")
        else:
            print("[ERROR]:- Table NOT FOUND")


    else:
        print("[ERROR]:- Invalid Syntax")

