from flask import Flask, render_template
import time

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/time_up", methods=["GET", "POST"])
def time_up():
    return render_template("time_up.html")


if __name__ == "__main__":

    app.run(debug=True)
