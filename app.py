from flask import Flask, render_template,redirect,url_for,flash,request,jsonify
from db import *

app = Flask(__name__)

# base url
@app.route('/')
def index():
    return redirect(url_for("signup"))

# signup
@app.route("/signup",methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        data = request.get_json()   
        username = data.get('username')
        password = data.get('password')
        if add_signup(username,password):
            flash("Account created successfully")
            return redirect(url_for("login"))
        else:
            flash("Account already exists, Try logging in")
            return render_template('index.html')
    else:
        return render_template('index.html')

# login
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        useremail = request.form['username']
        password = request.form['password']
        if check_login(useremail,password):
            flash("Succesful Login")
            return redirect(url_for("dashboard"))
        else:
            flash("Incorrect credentials or account does not exist")
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    pass

if __name__ == '__main__':
    app.run(debug=True)
