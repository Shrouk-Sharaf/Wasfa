# Wasfa (وصفة) - Full-Stack Recipe Platform

Wasfa is a comprehensive web application designed for organizing, managing, and discovering culinary recipes. The platform features a robust backend for handling user data and recipe logic, paired with a clean, responsive frontend for an intuitive user experience.

---

## Project Architecture

This repository is organized as a **monorepo**, ensuring a clean separation between the client-side interface and the server-side logic.

* **`client/`**: The frontend implementation using HTML5, CSS3, and JavaScript.
* **`server/`**: The backend API powered by Django and SQLite.

---

## Getting Started

### Prerequisites
* Python 3.x
* A modern Web Browser

### 1. Backend Setup (Server)
Navigate to the server directory and set up the Django environment:
```bash
cd server
# Create a virtual environment
python -m venv venv
# Activate it (Windows)
venv\Scripts\activate
# Install Django (and any other requirements)
pip install django
# Run migrations
python manage.py migrate
# Start the server
python manage.py runserver
```

### 2. Frontend Setup (Client)
Since the frontend is built with native web technologies, no installation is required. Simply open the entry point in your browser:

```text
Open: client/HTML/index.html (or your main entry file)
```
## Tech Stack

### **Frontend**
* **HTML5/CSS3:** Semantic structure and custom styling for a responsive user interface.
* **JavaScript:** Powering dynamic UI interactions and seamless API integration.
* **Design:** Focused on a **minimalist and professional aesthetic**, emphasizing clarity and user experience.

---

### **Backend**
* **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
* **SQLite:** A lightweight, serverless relational database used for efficient recipe and user data storage.
* **Logic Apps (Modules):**
    * **Users:** Manages secure authentication, registration, and user profile logic.
    * **Recipes:** Handles core CRUD operations (Create, Read, Update, Delete) for the recipe database.

## Directory Structure
```
    Wasfa-Project/
    ├── client/              # Frontend assets
    │   ├── HTML/            # Web pages
    │   ├── CSS/             # Stylesheets
    │   ├── JS/              # Frontend logic
    |   ├── Images/          # UI assets and icons
    │   └── Team Images/     # Project contributor assets
    ├── server/              # Django backend
    │   ├── wasfa_core/      # Project configuration
    │   ├── recipes/         # Recipe management app
    │   ├── users/           # User management app
    │   ├── manage.py        # Django CLI
    │   └── db.sqlite3       # Database file
    └── .gitignore           # Version control exclusions
    └── README.md            # Project documentation
```

## Contributors

This project was developed by a collaborative team from the **Faculty of Computers and Artificial Intelligence, Cairo University**:

* **George Ezat Hosni**
* **Jasmine Mohamed Elsayed**
* **Maria Atef Edward**
* **Mary Magdy Kamal**
* **Shrouk Sayed Ahmed**
* **Verina Antounios Atya**
