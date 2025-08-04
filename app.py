
from flask import Flask, render_template
from datetime import date
import os

app = Flask(__name__)

@app.route("/")
def index():
    today = date.today().isoformat()
    question_path = os.path.join("questions", f"{today}.txt")
    if os.path.exists(question_path):
        with open(question_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = "Heute ist keine Frage da – vielleicht morgen 😊"
    return render_template("index.html", question=content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3005, debug=True)
