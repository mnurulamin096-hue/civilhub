from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to CivilHub</h1>
    <p>GitHub for Civil Engineering Students</p>
    <p>My Civil Engineering Portfolio</p>
    """

if __name__ == "__main__":
    app.run()
