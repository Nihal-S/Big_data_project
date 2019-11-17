import os
inp = input()
inp = inp.lower()
inp = inp.split(" ")

#try:
if __name__=="__main__":
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
    

    if(inp[0] == "select"):
        f = open("schema.txt",'r')
        schemas = f.read()
        f.close()
        schemas = schemas.split("\n")
        dict_sch = dict()
        for i in schemas:
            dict_sch[i.split(" ")[0]] = i.split(" ")[1],i.split(" ")[2]
        for i in dict_sch: 
            if((inp[3].split("/")[0] == i) and (inp[3].split("/")[1] == i[2])):

        else:
            print("[ERROR]:- Database not found")


#except:
    #print("[ERROR]:-Not a valid syntax")