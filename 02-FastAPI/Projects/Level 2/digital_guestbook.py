# **Problem 4: The "Digital Guestbook"**<br>
# **Goal:** Practice persistent state (in-memory) and List responses.<br>
# **The Mission:** Create a simple guestbook where people can leave their names and a short note.
# 1. **The Storage:** Create a global Python list: `guestbook = []`.
# 2. **The POST Route (`/sign`):** * Accepts a Pydantic model `Entry` with `name` and `note`.
# * Adds the entry to the `guestbook` list.
# 3. **The GET Route (`/entries`):** * Returns the *entire* list of entries.
# 4. **The Challenge:** Add a Query Parameter to the GET route called `limit`. 
# If the user hits `/entries?limit=2`, only return the last 2 people who signed.


from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

guestbook: List[dict] = []

class Entry(BaseModel):
    name: str
    note: str

@app.post("/sign")
async def add_entry(entry: Entry):
    guestbook.append(entry.model_dump())
    return {"message": "Entry added successfully"}

@app.get("/entries")
async def get_entries(limit: Optional[int] = Query(default=None, ge=1)):
    if limit:
        return guestbook[-limit:]
    return guestbook