# **Problem 5: The "Secure Vault" (Basic Dependency)**<br>
# **Goal:** Practice your first **Dependency**.<br>
# **The Mission:** You have a secret piece of data: `"The treasure is buried under the palm tree."`
# 1. **The Dependency:** Create a function called `verify_header`.
# * It should look for a **Header** called `X-Secret-Key`. (Hint: Use `from fastapi import Header`).
# * If the header is exactly `"OpenSesame"`, it returns `True`.
# * If it’s anything else, it raises an `HTTPException(401)`.
# 2. **The Route:** Create a GET route `/vault`.
# * Use `Depends(verify_header)` to protect it.
# * If the dependency passes, return the secret message.

from fastapi import FastAPI

app = FastAPI()

@app.get()
async def 