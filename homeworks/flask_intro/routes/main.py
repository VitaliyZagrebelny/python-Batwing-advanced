from app import app
from flask import render_template


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/add/<value1>/<value2>")
def adding_value(value1, value2):
    value3 = int(value1) + int(value2)
    value4 = str(value3)
    return render_template("Adding.html", variable=value4)


