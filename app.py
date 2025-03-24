from flask import Flask, render_template, request ,url_for, flash, session, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
import random

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
    number = db.Column(db.Integer, default=1)
    data_created =db.Column(db.DateTime, default = datetime.utcnow)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    color = db.Column(db.String(7), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

with app.app_context():
    db.create_all()

def generate_random_color(gender):
    male_colors = ["#003399", "#545AA7", "#73C2FB", "#8DA399", "#1ca9c9", "#005f69", "#6A5ACD", "#367588", "#0C2340", "#F0F8FF"]
    female_colors = ["#FF69B4", "#eec0c8", "#800080", "#662d91", "#D8BFD8", "#770737", "#A95C68", "#AA336A", "#9F2B68", "#E30B5C"]
    if gender.lower() == "male":
        return random.choice(male_colors)
    elif gender.lower() == "female":
        return random.choice(female_colors)

@app.route("/",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username").strip()
        password = request.form.get("password")
        if not username or not password:
            flash("Username or Password is Empty!", "error")
            return redirect(url_for("login"))

        user_exist = User.query.filter_by(name = username).first()
        if user_exist:
            if check_password_hash(user_exist.password, password):
                session["username"] = username
                notes = Note.query.filter_by(user_id=user_exist.id).all()
                return render_template("notes.html",user = user_exist,notes=notes, msg = "you are logged in successfully!")
            else:
                flash("Incorrect password!", "error")
                return render_template("login.html")
        else:
            flash("you are not Registered!","error")
            return redirect(url_for("login"))

    return render_template("login.html")
        
@app.route("/register",methods = ["POST","GET"])
def register():
    if request.method == "POST":
        username = request.form.get('name').strip()
        email = request.form.get('email').strip()
        age = request.form.get('age').strip()
        gender = request.form.get('gender')
        dob = request.form.get('dob')
        c_pass = request.form.get('Confirm_password')
        password = request.form.get("password")
        number = random.randint(1,10)
        
        if datetime.strptime(dob, '%Y-%m-%d') > datetime.now():
            return render_template("signup.html",msg = "Invalid DOB")

        if User.query.filter_by(name = username).first():
            return render_template("signup.html", msg = "Username already exist!")

        if c_pass != password:
            return render_template("signup.html", msg = "Password do not match")

        else:
            hashed_password = generate_password_hash(password)
            new_user = User(
                name = username,
                email = email,
                age = age,
                gender = gender,
                dob = dob,
                password = hashed_password,
                number = number
            )
            db.session.add(new_user)
            db.session.commit()
            session["username"] = username
            notes = Note.query.filter_by(user_id=new_user.id).all()
            return render_template("notes.html", msg = "successfully created account!",user = new_user,notes=notes )
      
    return render_template("signup.html")

@app.route("/dashboard",methods=["POST","GET"])
def dashboard():
    if "username" not in session:
        return render_template("login.html",msg = "please log in first")
    user = User.query.filter_by(name=session["username"]).first()
    notes = Note.query.filter_by(user_id=user.id).all()
    return render_template("notes.html",user=user,notes=notes)

@app.route("/add_note", methods=["POST"])
def add_note():
    if "username" not in session:
        flash("Please log in first.", "error")
        return redirect(url_for("login"))

    title = request.form.get("title")
    content = request.form.get("content")
    user = User.query.filter_by(name=session["username"]).first()
    color = generate_random_color(user.gender)
    new_note = Note(title=title, content=content, user_id=user.id, color= color)
    db.session.add(new_note)
    db.session.commit()
    return redirect(url_for("dashboard"))

@app.route("/delete_data", methods=["GET","POST"])
def delete_data():
    user = User.query.filter_by(name=session["username"]).first()
    if user:
        Note.query.filter_by(user_id = user.id).delete()
        db.session.delete(user)
        db.session.commit()
        session.clear()
        flash("Your account has been deleted successfully!", "success")
        return redirect(url_for("login"))
    return redirect(url_for("dashboard"))

@app.route("/logout",methods=["POST","GET"])
def logout():
    user = User.query.filter_by(name = session['username']).first()
    session.clear()
    flash("You have been successfully logged out.")
    return redirect(url_for("login"))

@app.route("/tasks",methods = ["GET","POST"])
def tasks():
    user = User.query.filter_by(name=session["username"]).first()
    events = Event.query.filter_by(user_id=user.id).all()
    return render_template("task.html",events=events)

@app.route("/get_it",methods = ["GET","POST"])
def get_it():
    user = User.query.filter_by(name = session['username']).first()
    return render_template("index.html",user=user)

@app.route("/edit_note/<int:note_id>", methods=["POST"])
def edit_note(note_id):
    note = Note.query.get(note_id)
    note.title = request.form["title"]
    note.content = request.form["content"]
    db.session.commit()
    return redirect(url_for("dashboard"))

@app.route("/delete_note/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    note = Note.query.get(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("dashboard"))

@app.route('/get_events')
def get_events():
    user = User.query.filter_by(name=session["username"]).first()
    events = Event.query.filter_by(user_id=user.id).all()
    event_list = [{"id": event.id, "title": event.title, "start": event.date} for event in events]
    return jsonify(event_list)

@app.route('/add_event', methods=['POST'])
def add_event():
    user = User.query.filter_by(name=session["username"]).first()
    data = request.json
    new_event = Event(title=data['title'], date=data['date'],user_id=user.id)
    db.session.add(new_event)
    db.session.commit()
    return jsonify({"message": "Event added successfully!"})

@app.route('/delete_event', methods=['POST'])
def delete_event():
    user = User.query.filter_by(name=session["username"]).first()
    data = request.json
    event = Event.query.filter_by(id=data['id'], user_id=user.id).first()
    if event:
        db.session.delete(event)
        db.session.commit()
        return jsonify({"message": "Event deleted!"})
    return jsonify({"error": "Event not found!"}), 404

if __name__ == "__main__":
    app.run(debug=True)