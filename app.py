
from flask import Flask, render_template
from datetime import date
import os

app = Flask(__name__)

@app.route("/")
def index():
    today = date.today().isoformat()
    letter_path = os.path.join("letters", f"{today}.txt")
    if os.path.exists(letter_path):
        with open(letter_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = "Heute ist kein Brief da – vielleicht morgen 😊"
    return render_template("index.html", letter=content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3005)
