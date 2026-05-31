from flask import Flask, request
import os

app = Flask(__name__)

# 👇 ADD IT HERE
@app.route("/")
def home():
    return "Server is alive"


SECRET_KEY = "12345abc"

@app.route("/save", methods=["POST"])
def save():
    key = request.form.get("key")
    text = request.form.get("text")

    if key != SECRET_KEY:
        return "unauthorized", 403

    with open("log.txt", "a") as f:
        f.write(text + "\n")

    return "saved", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
