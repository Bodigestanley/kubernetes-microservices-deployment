from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Microservices Frontend</h1>
    <ul>
    <li>/auth</li>
    <li>/product</li>
    <li>/order</li>
    </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)