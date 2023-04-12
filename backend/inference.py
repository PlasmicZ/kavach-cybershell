from SpamDetection import SpamDetection

def calculate_score(text: str):
    spam_model = SpamDetection() 
    score = spam_model.predict(text)
    response = {"score":score}
    return response