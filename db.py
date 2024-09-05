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
    newpass=hashlib.sha256(password.encode()).hexdigest()
    query={"useremail":useremail,"password":newpass}
    if userdata.find_one(query):
        return True
    return False

def getName(useremail="harsh12345@gmail.com",password="harshgoat12345"):
    newpass=hashlib.sha256(password.encode()).hexdigest()
    query={"useremail":useremail,"password":newpass}
    projection={"name":1,"_id":0}
    result=userdata.find_one(query,projection)
    return result['name']
