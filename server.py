from flask import Flask, request

app = Flask(__name__)

# simple security key
SECRET_KEY = "12345abc"

@app.route("/save", methods=["POST"])
def save():
    key = request.form.get("key")
    text = request.form.get("text")

    if key != SECRET_KEY:
        return "unauthorized", 403

    with open("log.txt", "a") as f:
        f.write(text + "\n")

    return "saved"

app.run(host="0.0.0.0", port=10000)
