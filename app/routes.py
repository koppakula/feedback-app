from flask import render_template, request, redirect
from app import app

# This will store feedback in memory
feedback_list = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        comment = request.form["comment"]
        feedback_list.append({"name": name, "comment": comment})
        return redirect("/feedback")
    return render_template("index.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html", feedback=feedback_list)
