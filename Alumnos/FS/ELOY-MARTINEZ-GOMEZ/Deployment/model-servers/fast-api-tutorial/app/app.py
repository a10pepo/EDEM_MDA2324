from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
# Import necessary modules
# Create FastAPI instance
app = FastAPI()

# GET: Root path
@app.get("/")
async def root():
    return "Hola"

# GET: Example of a path parameter
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    a = user_id+10
    return {"user_id": a}

# POST: Example of a request body

class Item(BaseModel):
    name: str
    price: float
    
@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price*2}

# Run the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
# Example of a request
# curl -X GET "http://localhost:8000/users/1" -H "accept: application/json"
# curl -X POST "http://localhost:8000/items/" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"name\": \"tomate\", \"price\": 1.0}"