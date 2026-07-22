# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build RESTful APIs using FastAPI, Pydantic validation, and standard HTTP methods.

## 📝 Tasks

### 🛠️ Create API endpoints

#### Description

Implement a FastAPI application that exposes a resource collection and supports create, read, update, and delete operations.

#### Requirements
Completed program should:

- Define a FastAPI app in `starter-code.py`
- Create a Pydantic model to validate incoming request data
- Implement these endpoints:
  - `GET /items`
  - `GET /items/{item_id}`
  - `POST /items`
  - `PUT /items/{item_id}`
  - `DELETE /items/{item_id}`
- Return JSON responses and use appropriate HTTP status codes

### 🛠️ Add validation and documentation

#### Description

Use Pydantic models for request validation and confirm the auto-generated API docs.

#### Requirements
Completed program should:

- Validate request data with a Pydantic model
- Return clear error responses for invalid input
- Provide consistent response data for successful requests
- Confirm the API docs work at `/docs` or `/redoc`
