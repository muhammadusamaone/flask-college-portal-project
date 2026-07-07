from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "collegeportal123"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")

        flash("Welcome to College Portal")

        return redirect(url_for("dashboard", username=username))

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    username = request.args.get("username", "Student")
    return render_template("dashboard.html", username=username)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)