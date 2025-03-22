# Flask Note-Taking App

A simple note-taking app where users can register, log in, create, read, and delete notes. The application uses Flask and stores the data to an SQLite database.

## Features

- **User Registration & Authentication**
- **Secure Password Storage** (based on Werkzeug security)
- **Create, Read, and Delete Notes**
- **Session Management**
- **SQLite Database Integration**

## Requirements

To run this application, make sure you have the following dependencies installed:

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Session
- Werkzeug Security
- SQLite

## Project Structure

```
flask-note-app/
│   app.py               # Main Flask Application
│   database.db         # SQLite Database
│   templates/          # HTML Templates
│   static/             # CSS & JavaScript Files
```

## Usage

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd flask-note-app
   ```
2. **Install dependencies manually:**
   ```sh
   pip install Flask Flask-SQLAlchemy Flask-Session Werkzeug
   ```
3. **Run the application:**
   ```sh
   python app.py
   ```
4. **Use the web interface** to register, log in, create, and manage notes.

Notes will be saved in the database and will remain after the application is restarted.

## Database Structure

### User Table

| Column       | Type      | Description                            |
|-------------|----------|----------------------------------------|
| id          | INTEGER  | Primary Key                            |
| name        | TEXT     | Unique Username                        |
| email       | TEXT     | User Email                             |
| age         | INTEGER  | User Age                               |
| gender      | TEXT     | User Gender                            |
| dob         | TEXT     | Date of Birth                          |
| password    | TEXT     | Hashed Password                        |
| number      | INTEGER  | Randomly Assigned Number               |
| date_created | TIMESTAMP | Timestamp of Account Creation         |

### Notes Table

| Column       | Type      | Description                            |
|-------------|----------|----------------------------------------|
| id          | INTEGER  | Primary Key                            |
| user_id     | INTEGER  | Foreign Key (References User ID)       |
| title       | TEXT     | Note Title                             |
| content     | TEXT     | Note Content                           |
| date_created | TIMESTAMP | Timestamp of Note Creation            |

## API Endpoints

| Route        | Method | Description                         |
|-------------|--------|-------------------------------------|
| `/`         | GET/POST | Login Page                        |
| `/register` | GET/POST | User Registration                 |
| `/dashboard` | GET    | User Dashboard                     |
| `/add_note` | POST   | Add a New Note                     |
| `/delete_data` | POST | Delete User and Notes              |
| `/logout`   | GET    | Log Out User                        |
| `/tasks`    | GET    | Placeholder Route                   |
| `/get_it`   | GET    | Sample Page                         |

## Security Considerations

- Passwords are securely hashed prior to storage in the database.
- User data privacy is maintained using session-based authentication.
- CSRF protection and input validation must be added for further security.

## Logging

- The application logs events (e.g., user logins and note edits) to a log file.
- This allows for a record of things done.

## Demo

[Video Demonstration](https://www.youtube.com/watch?v=85YrpwPEWb4)

---

### Contributing
Pull requests are accepted. For large changes, first open an issue so we can discuss what you want to change.

### License
This project is released under the MIT License.

