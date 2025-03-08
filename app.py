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
    password = db.Column(db.String(100), nullable=False)
    data_created =db.Column(db.DateTime, default = datetime.utcnow)

@app.before_request
def create_tables():
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
            return render_template("signin.html")

    return render_template("login.html")
        
@app.route("/register",methods = ["POST","GET"])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get("password")
        
        
if __name__ == "__main__":
    app.run(debug=True)