from fastapi import FastAPI
from pydantic import BaseModel

# Create the app instance
app = FastAPI()


#Creating the model
class Fruit(BaseModel):
    name: str
    grams: float
    is_ripe: bool



@app.post("/fruits/")
async def add_fruit(fruit: Fruit):
    message = f"Received {fruit.grams}g of {fruit.name}."
    
    if not fruit.is_ripe:
        return {
            "message": message,
            "warning": "This fruit needs more time!"
        }

    return {"message": message}