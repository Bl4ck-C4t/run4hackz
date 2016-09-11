def upload(table,row,data,file="db.txt"):
    try:
        f = open(file, "r")
        f.close()
    except:
        f = open(file,"w")
        f.close()
    f = open(file, "r")
    database = f.read()
    if database == "":
        database = "{}"
    database = eval(database)
    f.close()
    f = open(file,"w")
    if not(table in database.keys()):
        database[table] = {}
    database[table][row] = data
    f.write(str(database))
    f.close()

def get(table="",row="",file="db.txt"):
    f = open(file,"r")
    database = eval(f.read())
    f.close()
    if table == "":
        return database
    elif row == "":
        return database[table]
    else:
        return database[table][row]
def delete(file="db.txt"):
    f = open(file,"w")
    f.truncate()
    f.close()
def exists(file="db.txt"):
    try:
        f=open(file,"r")
        if f.read() != "":
            return True
        else:
            return False
    except:
        return False
