from ollama import generate

def review_intv_resume(input):
    ot1 = generate(model="resm_intv_rev",prompt=input)
    output = ot1.response.strip()
    return output
