# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern RESTful web APIs using the FastAPI framework. You will create endpoints to perform CRUD operations on a resource, implement proper HTTP methods and status codes, and validate incoming request data.

## 📝 Tasks

### 🛠️ Create Basic FastAPI Application

#### Description
Set up a FastAPI application with a simple endpoint that demonstrates the basic structure of a FastAPI server.

#### Requirements
Completed program should:

- Import and initialize FastAPI
- Create a root endpoint (`/`) that returns a welcome message
- Include a `GET` endpoint that returns JSON data
- Run the server using `uvicorn` and verify it responds to requests
- Example response:
  ```json
  {
    "message": "Welcome to the FastAPI Server",
    "version": "1.0"
  }
  ```

### 🛠️ Implement CRUD Endpoints

#### Description
Create endpoints that handle Create, Read, Update, and Delete operations for a simple resource (e.g., tasks, books, students).

#### Requirements
Completed program should:

- Implement `GET /items` to retrieve all items
- Implement `GET /items/{id}` to retrieve a specific item by ID
- Implement `POST /items` to create a new item with validation
- Implement `PUT /items/{id}` to update an existing item
- Implement `DELETE /items/{id}` to delete an item
- Return appropriate HTTP status codes (200 for success, 201 for created, 404 for not found, etc.)
- Example POST request body:
  ```json
  {
    "name": "Sample Item",
    "description": "A test item"
  }
  ```

### 🛠️ Add Request and Response Validation

#### Description
Use Pydantic models to validate incoming request data and ensure consistent response formats.

#### Requirements
Completed program should:

- Define a Pydantic model for your resource with appropriate field types
- Include field validation (e.g., string length, numeric ranges)
- Return responses using the model for consistency
- Handle validation errors gracefully with informative error messages
- Example validation:
  ```python
  class Item(BaseModel):
      name: str
      description: str = None
      price: float
  ```
