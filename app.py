from flask import Flask, render_template, request
import os
from resume_analyzer import analyze_resume
from interview import QUESTIONS, evaluate_answer

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["resume"]
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        result = analyze_resume(path)
        return render_template("result.html", result=result)

    return render_template("index.html")

@app.route("/interview", methods=["GET", "POST"])
def interview():
    if request.method == "POST":
        answer = request.form["answer"]
        evaluation = evaluate_answer(answer)
        return render_template("interview.html",
                               question=QUESTIONS[1],
                               evaluation=evaluation)

    return render_template("interview.html",
                           question=QUESTIONS[0],
                           evaluation=None)

if __name__ == "__main__":
    app.run(debug=True)
