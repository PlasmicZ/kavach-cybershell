from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Infer

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

@app.get("/api/predict/{text}/", response_model=Infer)
async def predict_score(text):
    response = calculate_score(text)

    if response:
        return response
    
    return HTTPException(404, f"Error in fetching score of text: {text}")


# # Create Todo
# @app.post("/api/predict/", response_model=User)
# async def post_todo(todo:Todo):

#     response = await create_todo(todo.dict())

#     if response:
#         return response
#     return HTTPException(400, "Bad Request")

# # Update Todo
# @app.put("/api/todo/{title}/", response_model=Todo)
# async def put_todo(title:str, description:str):

#     response = await update_todo(title=title, desciption=description)

#     if response:
#         return response
#     return HTTPException(404, f"No Todo Title found with title: {title}")


# # Read Todo
# @app.get("/api/todo/")
# async def get_todo():

#     response = await fetch_all_todos()
#     return response


# # Delete Todo
# @app.delete("/api/todo/{title}/")
# async def delete_todo(title):

#     response = await remove_todo(title)

#     if response:
#         return f"Successfully deleted todo item with title: {title}"
    
#     return HTTPException(404, f"No Todo Title found with title: {title}")