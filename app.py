from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/project/building-design")
def building():
    return render_template("projects/building.html")


if __name__ == "__main__":
    app.run()
