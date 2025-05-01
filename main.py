from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI()

# In-memory "database"
users = []
restaurants = []
orders = []

# Models
class User(BaseModel):
    id: str
    name: str
    email: str

class Restaurant(BaseModel):
    id: str
    name: str

class Order(BaseModel):
    id: str
    user_id: str
    restaurant_id: str
    status: str = "pending"

@app.get("/")
def root():
    return {"message": "Welcome to Kasi Eats!"}

@app.post("/users", response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@app.get("/users", response_model=List[User])
def get_users():
    return users

@app.post("/restaurants", response_model=Restaurant)
def create_restaurant(restaurant: Restaurant):
    restaurants.append(restaurant)
    return restaurant

@app.get("/restaurants", response_model=List[Restaurant])
def get_restaurants():
    return restaurants

@app.post("/orders", response_model=Order)
def create_order(order: Order):
    orders.append(order)
    return order

@app.get("/orders", response_model=List[Order])
def get_orders():
    return orders
