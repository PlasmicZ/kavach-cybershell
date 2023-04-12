from SpamDetection import spam_model

async def calculate_score(text: str):
    score = await spam_model.predict()
    return score