from flask import Flask, render_template, request ,url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "iloveyou"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db = SQLAlchemy(app)

class database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable = False)
    data_created =db.Column(db.datetime, default = datetime.utcnow)

@app.route("/",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            return "password not found"
        else:
            return "done"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)