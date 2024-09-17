from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Stuff(BaseModel):
    name: str
    price: int

class UpdateStuff(BaseModel):
    name: str
    price: float

@app.get("/")
def read():
    return {"hello": "world"}


@app.get("/sumn/{num}")
async def summing(num: int):
    sum = 0
    for i in range (1, num + 1):
        sum = sum + i
    return {"sum is": sum}


stock = {
    1: {
        "name": "Lays",
        "price": "500"
    },
    2:{
        "name": "Cola",
        "price": "450"
    }, 
    3: {
        "name": "Sandwich",
        "price": "1200"
    }

}

@app.get("/get-stock/{id}")
def get_stock(id: int):
    return stock[id]

@app.get("/get-name")
def get_stock(name: str):
    for id in stock:
        if stock[id]["name"] == name:
            return stock[id]
    return {"not": "found"}

@app.post("/create-stuff/{id}")
def create_stuff(id: int, stuff: Stuff):
    if id in stock:
        return {"stuff": "alredy exists"}
    stock[id] = stuff
    return stock[id]
@app.put("/update-stock/{id}")
def update_stock(id: int, stuff: UpdateStuff):
    if id not in stock:
        return {"id": "not found"}
    if stuff.name != None:
        stock[id].name = stuff.name
    if stuff.price != None:
        stock[id].price = stuff.price
    return stock[id]

