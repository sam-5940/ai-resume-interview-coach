QUESTIONS = [
    "Tell me about yourself.",
    "What are your strengths?",
    "Explain a project you worked on.",
    "What is Python used for?"
]

def evaluate_answer(answer):
    length_score = min(len(answer.split()) * 2, 40)
    keyword_score = 30 if "python" in answer.lower() else 10
    clarity_score = 30 if len(answer) > 50 else 10

    total = length_score + keyword_score + clarity_score

    return {
        "score": total,
        "feedback": "Try to be more clear and include technical details."
    }
