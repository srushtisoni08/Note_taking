# Flask Note-Taking App

A minimal note-taking application where users can register, log in, create, read, and delete notes. The app utilizes Flask and persists the data to an SQLite database.

## Features

- **User Registration & Authentication**
- **Secure Password Storage** (based on Werkzeug security)
- **Create, Read, and Delete Notes**
- **Session Management**
- **SQLite Database Integration**

## Requirements

To execute this application, ensure you have the following dependencies installed:

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Session
- Werkzeug Security
- SQLite

## Project Structure

```
flask-note-app/
│-- app.py              # Main Flask Application
│-- database.db         # SQLite Database
│-- templates/          # HTML Templates
│-- static/             # CSS & JavaScript Files
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

Notes will be stored in the database and persist across application restarts.

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

- Passwords are securely hashed before storage in the database.
- User data privacy is ensured through session-based authentication.
- CSRF protection and input validation should be implemented for additional security.

## Logging

- The application writes events (such as user logins and note changes) to a log file.
- This provides a history of actions performed.

## Demo

[Video Demonstration](https://www.youtube.com/watch?v=85YrpwPEWb4)

---

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License
This project is licensed under the MIT License.

