from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
# from model import Infer

# Cross Origin Resourse Sharing - When frontend client JS communicates with Backend. They are in diffrent origin. (Protocol, Domain, Port)
# We need permission in the backend to interact 

# App object
app = FastAPI()

from inference import (calculate_score)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get('/')
def read_root():
    return {"Hello":"World"}

@app.get("/api/predict/{text}/")
async def predict_score(text) -> str:
    response = calculate_score(text)

    if response:
        return response
    
    return HTTPException(404, f"Error in fetching score of text: {text}")

