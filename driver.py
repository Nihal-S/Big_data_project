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
        #print(dict_sch)
        for i in dict_sch: 
            if((inp[3].split("/")[0] == i) and (inp[3].split("/")[1] == dict_sch[i][1])):
                #print(dict_sch[i][1])
                if(inp[1] == "*"):
                    inp[1] = dict_sch[i][0]
                if(inp[1][-1] != ")"):
                    res = os.popen("python3 mapper.py<data/"+dict_sch[i][1]+" "+inp[1]+" "+i + " "+inp[5])
                    output = res.read()
                else:
                    #print(inp[1][4:-1])
                    res = os.popen("python3 mapper.py<data/"+dict_sch[i][1]+" "+inp[1][4:-1]+" "+i + " "+inp[5])
                    output = res.read()
                f = open('output_map.txt', 'w')
                f.write(output)
                f.close()



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
                
                if(inp[1][-1] == ")"):
                    res = os.popen('python3 reducer1.py < output_map.txt '+ inp[-1][:-1] + " " + str(encoded)+ " " + inp[1][0:3])
                    #print(var)
                    output = res.read()
                    print(output)

                else:
                    #var = 'python3 reducer.py < output_map.txt '+ inp[-1][:-1] + " " + str(encoded)
                    res = os.popen('python3 reducer.py < output_map.txt '+ inp[-1][:-1] + " " + str(encoded))
                    #print(var)
                    output = res.read()
                    print(output)
                    f = open("output_red.txt","w")
                    f.write(output)
                    f.close()

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

#except:
    #print("[ERROR]:-Not a valid syntax")