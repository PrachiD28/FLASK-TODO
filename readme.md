# 📝 My Todo - Flask Todo Management System

A simple and responsive **Todo Management Web Application** built using **Flask**, **SQLite**, **Flask-SQLAlchemy**, and **Bootstrap 5**. The application allows users to create, view, update, delete, and search todos through a clean and user-friendly interface.

---

## 🚀 Features

* ✅ Create new todos
* 📋 View all todos
* ✏️ Update existing todos
* 🗑️ Delete todos
* 🔍 Search todos by title
* 🕒 Automatically records the creation date and time
* 💾 SQLite database for data storage
* 🎨 Responsive user interface using Bootstrap 5
* 🧩 Jinja2 template inheritance for reusable layouts

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* Flask-SQLAlchemy

### Database

* SQLite

### Frontend

* HTML5
* Bootstrap 5
* Jinja2 Templates

### Deployment

* Gunicorn

---

## 📂 Project Structure

```text
Todo-App/
│
├── app.py
├── requirements.txt
├── Procfile
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   └── update.html
│
├── static/
│   └── js/
│       └── test.js
│
└── todo.db
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. Navigate to the project folder

```bash
cd your-repository
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000/
```

---

## 🗄️ Database

This project uses **SQLite** with **Flask-SQLAlchemy**.

### Todo Model

| Field        | Type     | Description        |
| ------------ | -------- | ------------------ |
| SNo          | Integer  | Primary Key        |
| title        | String   | Todo title         |
| desc         | String   | Todo description   |
| date_created | DateTime | Creation timestamp |

---

## 🌐 Application Routes

| Route           | Method    | Description             |
| --------------- | --------- | ----------------------- |
| `/`             | GET       | Display all todos       |
| `/add`          | GET, POST | Add a new todo          |
| `/update/<SNo>` | GET, POST | Update an existing todo |
| `/delete/<SNo>` | GET       | Delete a todo           |
| `/search`       | GET       | Search todos by title   |

---



The project is deployment-ready using **Gunicorn**.

Example `Procfile`:

```text
web: gunicorn app:app
```

---

## 💡 Future Enhancements

* User authentication and authorization
* Mark todos as completed
* Set due dates and reminders
* Categorize todos
* Add priority levels
* Responsive dark mode
* Pagination for large todo lists
* REST API integration
* Email notifications
* Cloud database support (PostgreSQL/MySQL)

---


