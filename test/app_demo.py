from flask import Flask, render_template, request,session ,url_for
import random
import string
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "".join(random.choices(string.ascii_letters,k=256))


@app.route("/")
def top():
    return render_template("a.html")

@app.route("/b")
def b():
    return render_template("b.html")

if __name__ == "__main__":
    app.run(debug=True)
