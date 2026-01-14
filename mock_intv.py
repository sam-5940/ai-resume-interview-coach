from ollama import generate

def conduct_mock_intv(resume_dets,job_dets):
    history = resume_dets.strip() + "\n\n"
    history += "job_details: " + job_dets
    output = ""
    i = 0

    while output.upper() != "INTERVIEW FINISHED" and i < 20:
        ot1 = generate(model="mock_intv", prompt=history)
        output = ot1.response.strip()

        print(output + "\n")

        # stop immediately if interview ends
        if output.upper() == "INTERVIEW FINISHED":
            history += output + "\n"
            break

        reply = input("reply: ").strip()
        history += output + "\n"
        history += "reply: " + reply + "\n"

        i += 1

    return history
