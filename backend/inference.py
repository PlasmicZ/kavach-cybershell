from SpamDetection import SpamDetection

def calculate_score(text: str):
    spam_model = SpamDetection() 
    score = spam_model.predict(text)

    return score