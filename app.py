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
        return render_template("dashboard.html",email=session['user'])       
    return redirect(url_for("signup"))

# course page
@app.route("/dashboard/course", methods=["POST","GET"])
def course():
    return render_template("course.html",email=session['user'])

# get Question or video
@app.route("/dashboard/course/<email>",methods = ["POST","GET"])
def getQuestionOrVideo(email):
    state = getState(email)
    questionorVideo = getQuestion(state)
    print(questionorVideo)
    return jsonify(questionorVideo)

@app.route("/dashboard/IncrementState/<email>", methods=["POST","GET"])
def IncrementStateFunc(email):
    IncrementState(email)
    return jsonify({"Sucess":1})

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/courses")
def courses():
    return render_template("Courses.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("signup"))

if __name__ == '__main__':
    app.run(debug=True)
