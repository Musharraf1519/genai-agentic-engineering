from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# 1. Path Parameter Example
# This route identifies a specific item in our database by its ID.
@app.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    """
    'item_id' is a Path Parameter. It is MANDATORY.
    If you go to /items/5, item_id becomes 5.
    If you go to /items/abc, FastAPI returns an error because 'abc' is not an 'int'.
    """
    return {
        "item_id": item_id, 
        "location": "Warehouse A",
        "status": "In Stock"
    }

# 2. Query Parameter Example
# This route handles a search. Notice 'q' and 'short_description' are not in the URL path.
@app.get("/items/")
async def search_items(q: str, short_description: bool = False):
    """
    'q' is a REQUIRED Query Parameter because it has no default value.
    'short_description' is an OPTIONAL Query Parameter with a default of False.
    URL Example: /items/?q=hammer&short_description=true
    """
    results = {"search_query": q}
    
    if short_description:
        results.update({"description": "A high-quality tool for construction."})
    else:
        results.update({"description": "Full details are hidden. Set short_description=True to see more."})
        
    return results

# 3. Combined Path and Query Parameters
@app.get("/users/{user_id}/orders")
async def get_user_orders(user_id: int, limit: Optional[int] = None):
    """
    'user_id' is a Path Parameter (Mandatory).
    'limit' is an Optional Query Parameter.
    URL Example: /users/101/orders?limit=5
    """
    orders = [f"Order {i}" for i in range(1, 11)] # Simulating 10 orders
    
    if limit:
        return {"user_id": user_id, "orders": orders[:limit]}
    
    return {"user_id": user_id, "orders": orders}