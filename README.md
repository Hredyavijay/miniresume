# Mini Resume Collector API

A simple backend API built with **FastAPI** to collect and manage candidate resume information.
The application allows storing candidate details, uploading resumes, and retrieving candidate data using filters.

## Features

* Add candidate details
* Upload resume files
* Store data in SQLite database
* Retrieve candidate information
* Filter candidates by skills, experience, and graduation year
* Health check endpoint
* Delete candidate records

## Tech Stack

* Python
* FastAPI
* SQLite
* SQLAlchemy
* Uvicorn

## Project Structure

```
project/
│
├── main.py           # FastAPI application
├── models.py         # Database models
├── database.py       # Database connection
├── resumes/          # Uploaded resume files
├── resumes.db        # SQLite database
├── requirements.txt  # Project dependencies
└── README.md
```

## Installation

1. Clone the repository

```
git clone <your-repository-url>
cd project-folder
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the application

```
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

## API Endpoints

### Health Check

```
GET /health
```

### Create Candidate

```
POST /candidates
```

### Get All Candidates

```
GET /candidates
```

Optional filters:

* skill
* min_experience
* graduation_year

Example:

```
GET /candidates?skill=python&min_experience=1&graduation_year=2025
```

### Get Candidate by ID

```
GET /candidates/{candidate_id}
```

### Delete Candidate

```
DELETE /candidates/{candidate_id}
```

## Database

The application uses **SQLite** for storing candidate data.
Database file: `resumes.db`

## Author

Hredya Vijay
