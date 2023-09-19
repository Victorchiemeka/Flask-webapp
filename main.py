#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "author": "victor chiemeka",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "September 19, 2023",
    },
    {
        "author": "Sochi mmadu",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "September 20, 2023",
    },
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
