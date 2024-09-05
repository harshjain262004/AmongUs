from flask import Flask, render_template,redirect,url_for,flash,request,jsonify,session
from db import *

app = Flask(__name__)
app.secret_key = "MujHackX24"

# base url
@app.route('/')
def index():
    return redirect(url_for("signup"))

# signup
@app.route("/signup",methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        useremail = request.form['useremail']
        password = request.form['password']
        if add_signup(useremail,password,name):
            flash("Account created successfully")
            session['user'] = useremail
            return redirect(url_for("dashboard"))
        else:
            flash("Account already exists, Try logging in")
            return render_template('login.html')
    else:
        return render_template('login.html')

# login
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        useremail = request.form['useremail']
        password = request.form['password']
        if check_login(useremail,password):
            session["user"] = useremail
            flash("Succesful Login")
            return redirect(url_for("dashboard"))
        else:
            flash("Incorrect credentials or account does not exist")
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    if "user" in session:
        pass       
    return f"dashbord for {session['user']}"

if __name__ == '__main__':
    app.run(debug=True)
