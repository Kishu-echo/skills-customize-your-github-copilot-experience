from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool

items: Dict[int, Item] = {}
next_id = 1

@app.get("/items")
def list_items():
    return [ {"id": item_id, **item.dict()} for item_id, item in items.items() ]

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **items[item_id].dict()}

@app.post("/items", status_code=201)
def create_item(item: Item):
    global next_id
    items[next_id] = item
    created_item = {"id": next_id, **item.dict()}
    next_id += 1
    return created_item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"id": item_id, **item.dict()}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"detail": "Item deleted"}
