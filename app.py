from flask import Flask, render_template, request, redirect, url_for, session
import os
from ollama import generate

from resume_analyzer import extract_pdf_text, resume_anlz
from review import review_intv_resume

app = Flask(__name__)
app.secret_key = "super_secret_key"
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("resume")
        job_desc = request.form.get("job_desc", "").strip()

        if not file:
            return render_template("index.html", error="No resume uploaded")

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        resume_text = extract_pdf_text(filepath)
        analysis = resume_anlz(resume_text)

        session["resume_analysis"] = analysis
        session["job_desc"] = job_desc
        session["history"] = analysis + "\n\nJOB DETAILS:\n" + job_desc + "\n\n"

        return redirect(url_for("interview"))

    return render_template("index.html")


@app.route("/interview", methods=["GET", "POST"])
def interview():
    history = session.get("history", "")

    if request.method == "POST":
        user_reply = request.form.get("reply", "").strip()
        history += f"CANDIDATE: {user_reply}\n\n"

    response = generate(
        model="mock_intv",
        prompt=history
    ).response.strip()

    history += f"INTERVIEWER: {response}\n\n"
    session["history"] = history

    if response.upper() == "INTERVIEW FINISHED":
        return redirect(url_for("review"))

    return render_template("interview.html", question=response)


@app.route("/review")
def review():
    transcript = session.get("history", "")
    output = review_intv_resume(transcript)
    return render_template("review.html", output=output)


if __name__ == "__main__":
    app.run(debug=True)
