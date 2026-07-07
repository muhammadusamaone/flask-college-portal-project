# Flask College Portal

A beginner-friendly Flask project that simulates a simple **College Portal**. This project demonstrates the core concepts of Flask, including routing, forms, redirects, flash messages, dynamic templates, and custom error pages.

---

## Features

* Home Page
* Login Page
* Dashboard Page
* Form Handling using POST
* Redirects with `redirect()`
* URL Generation using `url_for()`
* Flash Messages
* Dynamic User Greeting
* Custom 404 Error Page
* Jinja2 Template Rendering

---

## Technologies Used

* Python 3
* Flask
* HTML5
* Jinja2

---

## Project Structure

```text
college_portal/
│
├── app.py
│
└── templates/
    ├── home.html
    ├── login.html
    ├── dashboard.html
    └── 404.html
```

---

## Application Workflow

### Home Page

* Displays the College Portal homepage.
* Provides a button to navigate to the Login page.

### Login Page

* Accepts the username from the user.
* Submits the form using the POST method.

### Dashboard

* Displays a personalized welcome message.
* Shows a flash message after successful login.

### Custom 404 Page

* Displays a friendly error page when the requested page does not exist.
* Includes a **Back to Home** button.

---

## Flask Concepts Demonstrated

* Flask Routing (`@app.route`)
* `render_template()`
* `request.form`
* `request.args`
* `redirect()`
* `url_for()`
* `flash()`
* `get_flashed_messages()`
* Custom Error Handling (`@app.errorhandler`)
* Jinja2 Templates

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flask-college-portal.git
```

### 2. Install Flask

```bash
pip install flask
```

### 3. Run the application

```bash
python app.py
```

### 4. Open your browser

```text
http://127.0.0.1:5000/
```

---

## Screens Included

* Home Page
* Login Page
* Dashboard
* Custom 404 Error Page

---

## Learning Outcomes

After completing this project, you will understand:

* Flask application structure
* HTML template rendering
* Form handling
* GET and POST requests
* Redirecting users
* URL generation with `url_for()`
* Flash messaging
* Passing data between pages
* Custom error pages
* Basic web application workflow

---

## Author

Created as part of a Flask learning journey to practice fundamental web development concepts.
