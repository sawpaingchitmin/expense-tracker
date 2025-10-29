# 💰 Expense Tracker

A simple **expense tracking application** built with **Django**, allowing users to add, view, and analyze their expenses.
You can record expenses with title, category, amount, date, and notes — all managed through a clean, minimal interface.

---

## ✨ Features

- 💵 **Track Expenses**
    - Add expenses with title, category, amount, date, and optional notes
    - View a detailed list of all expenses
    - See total spending at a glance

- 🔍 **Expense Details**
    - View full details for any single expense

- 🗂️ **Categories**
    - Group expenses by category (e.g., Food, Transport, Entertainment, etc.)

- 📱 **Responsive UI**
    - Simple and clean design using pure CSS
    - Fully responsive layout

- ⚙️ **Admin Panel**
    - Manage expenses and categories directly from Django admin
    
- 🔐 **CSRF Protection**
    - Secure form submissions

--- 

## 🛠️ Technologies Used

- [Django](https://www.djangoproject.com/) — Python-based web framework
- [SQLite](https://www.sqlite.org/) — lightweight database (used for development and testing)
- [Whitenoise](https://whitenoise.readthedocs.io/) — serves static files in production
- [dotenv](https://pypi.org/project/python-dotenv/) — environment variable management
- [Gunicorn](https://gunicorn.org/) — WSGI server for production
- **Custom CSS** — simple responsive UI design

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/sawpaingchitmin/expense-tracker.git
cd expense-tracker
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Linux/Mac
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
Create a file named .env in your project root:
```bash
SECRET_KEY=your_secret_key
DEBUG=True
```

### 5. Apply migrations
```bash
python manage.py migrate 
# (If you modify models, run 'python manage.py makemigrations' before migrate)
```

### 6. Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

## 📂 Project Structure
``` bash
expense-tracker/
│── expense_tracker/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│── expenses/
│   ├── templates/expenses/
│   │   ├── add_expense.html
│   │   ├── base.html
│   │   ├── expense_detail.html
│   │   ├── expense_list.html
│   │   └── home.html
│   ├── admin.py
│   ├── forms.py 
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│── static/expenses/
│   └── style.css
│
│── db.sqlite3
│── manage.py
│── requirements.txt
```

## 🌍 Live Demo

You can try the live version here:  
👉 [Expense Tracker on Render](https://expense-tracker-r32n.onrender.com/)