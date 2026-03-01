# from fastapi import FastAPI

# # 1. Create the app instance
# app = FastAPI()

# # 2. Define a route (Path Operation)
# @app.get("/")
# async def read_root():
#     # 3. Return a JSON response
#     return {"status": "success", "message": "Welcome to my first API"}



from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}