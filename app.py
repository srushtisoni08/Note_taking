from flask import Flask, render_template, request ,url_for, flash, session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = "flask 1st project"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE']='filesystem'
db = SQLAlchemy(app)
Session(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable = False, unique = True)
    email = db.Column(db.String(50),nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10),nullable=False)
    dob = db.Column(db.String(20))
    password = db.Column(db.String(100), nullable=False)
    data_created =db.Column(db.DateTime, default = datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route("/",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            return render_template("error.html")

        user_exist = User.query.filter_by(name = username).first()
        if user_exist:
            if check_password_hash(user_exist.password, password):
                session["username"] = username
                flash("Login successful!", "success")
                return render_template("index.html")
            else:
                flash("Incorrect password!", "error")
                return render_template("login.html")
        else:
            return "you are not registered!"

    return render_template("login.html")
        
@app.route("/register",methods = ["POST","GET"])
def register():
    if request.method == "POST":
        username = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')
        gender = request.form.get('gender')
        dob = request.form.get('dob')
        c_pass = request.form.get('Confirm_password')
        password = request.form.get("password")
        
        if datetime.strptime(dob, '%Y-%m-%d') > datetime.now():
            return "Invalid DOB"

        if User.query.filter_by(name = username).first():
            return "Username Already Exist"

        if c_pass != password:
            return "password do not match"
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(
                name = username,
                email = email,
                age = age,
                gender = gender,
                dob = dob,
                password = hashed_password
            )
            db.session.add(new_user)
            db.session.commit()
            flash("successfully created account!","success")
            return redirect(url_for("dashboard"))
      
    return render_template("signup.html")

@app.route("/dashboard",methods=["POST"])
def dashboard():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)