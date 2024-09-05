from pymongo import MongoClient
import hashlib


connection_string="mongodb+srv://hjgoat:hjgoat@technormieshackx.jwvnz.mongodb.net/"
client=MongoClient(connection_string)
db=client["amongus"]
userdata=db["userdata"]





def add_signup(useremail,password,name):
    newpass=hashlib.sha256(password.encode()).hexdigest()
    query={"useremail":useremail}
    if userdata.find_one(query):
        return False
    userdata.insert_one({'useremail':useremail,'password':newpass,'name':name})
    return True

def check_login(useremail,password):
    # useremail already exists and fetch document and check
    pass

def getId(useremail,password):
    #return string of id of useremail
    pass
