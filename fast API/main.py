from fastapi import FastAPI

# 1. Create the app instance
app = FastAPI()

# 2. Define a route (Path Operation)
@app.get("/")
async def read_root():
    # 3. Return a JSON response
    return {"status": "success", "message": "Welcome to my first API"}