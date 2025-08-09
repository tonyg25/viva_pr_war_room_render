def score_statement(text):
    if not text.strip():
        return {"score":0,"notes":["No statement provided."]}
    score = 50 if "investigation" in text.lower() else 0
    return {"score":score,"notes":["Contains investigation" if score else "Missing investigation"]}
