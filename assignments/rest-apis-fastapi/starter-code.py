"""
FastAPI REST API Starter Code
Build your API below following the assignment requirements.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

# Initialize FastAPI app
app = FastAPI()

# TODO: Define a Pydantic model for your resource
# Example:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None


# TODO: Create a root endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to FastAPI"}


# TODO: Implement CRUD endpoints
# GET /items - retrieve all items
# GET /items/{id} - retrieve specific item
# POST /items - create new item
# PUT /items/{id} - update item
# DELETE /items/{id} - delete item


# To run this server:
# 1. Install FastAPI: pip install fastapi uvicorn
# 2. Run: uvicorn starter-code:app --reload
# 3. Visit http://localhost:8000 in your browser
# 4. API documentation available at http://localhost:8000/docs
