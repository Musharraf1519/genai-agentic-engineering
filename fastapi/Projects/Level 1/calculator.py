# **Problem 3: The "Simple Calculator"**<br>
# **Goal:** Practice Data Validation and Error Handling.<br>
# **The Mission:**<br>
# Create a GET route called `/calculate`.<br>
# 1. **Query Parameters:** Accept three parameters: `x` (float), `y` (float), and `operation` (string).
# 2. **The Logic:**
# * Support four operations: `add`, `subtract`, `multiply`, and `divide`.
# * Return the result in a JSON object like: `{"result": 10.5}`.
# 3. **The Challenge:**
# * If the user tries to `divide` by `0`, raise a **FastAPI HTTPException** with a `400` status code and the message: `"Cannot divide by zero, math is crying."`
# * If the user types an operation that isn't one of the four listed above, return a `404` error.

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/calculate")
async def calculator(x: float, y: float, operation: str):

    if operation == "add":
        return {"result": x + y}

    elif operation == "subtract":
        return {"result": x - y}

    elif operation == "multiply":
        return {"result": x * y}

    elif operation == "divide":
        if y == 0:
            raise HTTPException(
                status_code=400,
                detail="Cannot divide by zero, math is crying."
            )
        return {"result": x / y}

    else:
        raise HTTPException(
            status_code=404,
            detail="Operation not supported."
        )
    