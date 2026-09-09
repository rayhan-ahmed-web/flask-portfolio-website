# Flask Portfolio Website

## Internship Task 6 – Build a Portfolio Website with Flask

A responsive personal portfolio website built with **Python, Flask, HTML5, CSS3, JavaScript, and Jinja2**.

## Features

- Responsive single-page portfolio
- Flask application and routing
- Jinja2 template rendering
- Home / hero section
- About Me section
- Technical skills section
- Projects section with GitHub links
- Education section
- Contact form using POST
- Server-side contact form validation
- Flask flash messages for success/error feedback
- `/health` endpoint for application health checking
- Mobile navigation menu
- Responsive layout for desktop, tablet, and mobile
- Clean project structure with `templates` and `static` directories

## Project Structure

```text
flask-portfolio-website/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## Technologies Used

- **Python** – application logic
- **Flask** – web framework and routing
- **Jinja2** – dynamic HTML templating
- **HTML5** – page structure
- **CSS3** – responsive styling
- **JavaScript** – mobile navigation and form interaction

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/rayhan-ahmed-web/flask-portfolio-website.git
cd flask-portfolio-website
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Flask

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Flask Routes

| Method | Route | Purpose |
|---|---|---|
| GET | `/` | Displays the portfolio |
| POST | `/contact` | Processes the contact form |
| GET | `/health` | Returns application health status |

## Contact Form

The contact form sends data to `/contact` with the HTTP `POST` method. Flask reads submitted values using `request.form`, validates that name, email, and message are present, and uses `flash()` to display feedback before redirecting back to the contact section.

This demo intentionally does not send email or store messages in a database. For a production portfolio, the route could be connected to a database or email service.

## Customization

1. Edit portfolio text in `templates/index.html`.
2. Update the `PROJECTS` list in `app.py`.
3. Update the `SKILLS` list in `app.py`.
4. Modify colors and layout in `static/css/style.css`.
5. Add additional Flask routes if required.

## Flask Concepts Demonstrated

- Flask application creation with `Flask(__name__)`
- URL routing with `@app.route()`
- GET and POST methods
- Jinja2 template rendering with `render_template()`
- Static file handling with `url_for()`
- Form data with `request.form.get()`
- Redirects with `redirect()` and `url_for()`
- User feedback with `flash()`

## Interview Questions Covered

- What is Flask?
- Why use Flask instead of Django?
- What is a route in Flask?
- What does `@app.route()` do?
- What is Jinja2?
- Why are templates stored in a `templates` folder?
- Why are CSS and JavaScript stored in `static`?
- What is the difference between GET and POST?
- How do you receive form data in Flask?
- What does `render_template()` do?
- How can a Flask application be deployed?

## Internship Deliverable

This repository contains the complete Flask portfolio application, HTML template, responsive CSS, JavaScript interaction, Flask contact form, dependencies, documentation, and source structure needed for the portfolio website task.

## License

This project is intended for educational and internship submission purposes.
