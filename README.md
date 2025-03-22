Flask Note-Taking App
Video Demo: https://youtu.be/xfYxMB9kzv8
A minimal note-taking application where users can register, log in, create, read, and delete notes. The app utilizes Flask and persists the data to an SQLite database.

Features
User Registration & Authentication

Secure Password Storage (based on Werkzeug security)

Create, Read, and Delete Notes

Session Management

SQLite Database Integration

Requirements
To execute this application, you have the following dependencies:

Python 3.x

Flask

Flask-SQLAlchemy

Flask-Session

Werkzeug Security

SQLite

database.db: SQLite database containing users and notes.

templates/: Directory of HTML templates for the web interface.

static/: Directory of CSS and JavaScript files.

Usage
Run the application:

Use the web interface to register, log in, make, and administer notes.

Notes will be stored in the database and available on next application launch.

Database Structure
User Table
id: Primary Key

name: Unique Username

email: User Email

age: User Age

gender: User Gender

dob: Date of Birth

password: Hashed Password

number: Randomly Assigned Number
date_created: Timestamp of Account Creation

Notes Table
id: Primary Key

user_id: Foreign Key (References User ID)
title: Note Title

content: Note Content
date_created: Timestamp of Note Creation

API Endpoints
Route Method Description
/ GET/POST Login Page
/register GET/POST User Registration
/dashboard.GET User Dashboard
/add_note.POST Add a New Note
/delete_data.POST Delete User and Notes
/logout.GET Log Out User
/tasks.GET Placeholder Route
/get_it.GET Sample Page
Security Considerations
Passwords are hashed before storage in the database.

User data privacy is ensured by session-based authentication.

CSRF protection and input validation should be implemented for additional security.

Logging
The application writes events (such as user logins and note changes) to a log file, giving a history of the actions performed.
