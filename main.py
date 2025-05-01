from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory "database"
db: Dict[int, dict] = {}

# Pydantic model for request/response
class Item(BaseModel):
    name: str
    description: str = None

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in db:
        raise HTTPException(status_code=400, detail="Item already exists")
    db[item_id] = item.dict()
    return {"msg": "Item created", "item": db[item_id]}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]

@app.patch("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    db[item_id].update(item.dict(exclude_unset=True))
    return {"msg": "Item updated", "item": db[item_id]}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted = db.pop(item_id)
    return {"msg": "Item deleted", "item": deleted}
