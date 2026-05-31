from flask import Flask, request
import os

app = Flask(__name__)

SECRET_KEY = "12345abc"

@app.route("/")
def home():
    return """
    <h2>Send Message</h2>
    <form action="/save" method="post">
        <input name="key" placeholder="key"><br><br>
        <input name="text" placeholder="text"><br><br>
        <button type="submit">Send</button>
    </form>
    """

@app.route("/save", methods=["POST"])
def save():
    key = request.form.get("key")
    text = request.form.get("text")

    if key != SECRET_KEY:
        return "unauthorized", 403

    with open("log.txt", "a") as f:
        f.write(text + "\n")

    return "saved", 200


@app.route("/logs")
def logs():
    try:
        with open("log.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No logs yet"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
