from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = "portfolio-secret-key-change-in-production"

PROJECTS = [
    {
        "title": "Calculator CLI App",
        "description": "A Python command-line calculator supporting basic arithmetic operations with input validation.",
        "tech": "Python",
        "link": "https://github.com/rayhan-ahmed-web/calculator-cli-app",
    },
    {
        "title": "To-Do List CLI App",
        "description": "A persistent command-line task manager that lets users add, view, complete, and delete tasks.",
        "tech": "Python",
        "link": "https://github.com/rayhan-ahmed-web/todo-list-cli-app",
    },
    {
        "title": "News Headlines Scraper",
        "description": "A web scraper that collects news headlines using Requests and BeautifulSoup and saves them to a text file.",
        "tech": "Python, BeautifulSoup",
        "link": "https://github.com/rayhan-ahmed-web/news-headlines-scraper",
    },
    {
        "title": "User Management REST API",
        "description": "A Flask REST API implementing GET, POST, PUT, and DELETE operations for user data.",
        "tech": "Python, Flask, REST API",
        "link": "https://github.com/rayhan-ahmed-web/user-management-rest-api",
    },
    {
        "title": "Sales Data Analysis",
        "description": "A Pandas-based CSV analysis project with aggregation, filtering, product analysis, and visualizations.",
        "tech": "Python, Pandas, Matplotlib",
        "link": "https://github.com/rayhan-ahmed-web/data-analysis-on-csv",
    },
]

SKILLS = [
    "Python", "Flask", "HTML5", "CSS3", "JavaScript", "Pandas",
    "REST APIs", "Web Scraping", "Git & GitHub", "Jupyter Notebook"
]

@app.route("/")
def home():
    return render_template("index.html", projects=PROJECTS, skills=SKILLS)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in all contact form fields.", "error")
        return redirect(url_for("home") + "#contact")

    flash(f"Thanks, {name}! Your message has been received.", "success")
    return redirect(url_for("home") + "#contact")

@app.route("/health")
def health():
    return {"status": "ok", "message": "Portfolio Flask application is running"}, 200

if __name__ == "__main__":
    app.run(debug=True)
