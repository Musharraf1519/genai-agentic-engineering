from fastapi import FastAPI
from typing import Optional

# Create the app instance
app = FastAPI()

# Define a route with parameters
@app.get("/greet/{name}")
async def read_root(name: str, message: Optional[str]=None):
    # Return a JSON response
    if message:
        return {"message": f"Hello {name}, {message}"}

    return {"message": f"Hello {name}, hope you have a great day!"}