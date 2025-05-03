# Most Simple API - Books Service

A lightweight, minimalist Books API built with FastAPI for testing and demonstration purposes.

## Overview

This project provides a simple RESTful API for managing a collection of books with basic CRUD operations. The API is built using FastAPI and stores data in-memory.

## Features

- Create, read, update, and delete books
- Input validation using Pydantic models
- Error handling with appropriate HTTP status codes
- Lightweight in-memory storage

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/pavanvamsi3/most-simple-api.git
   cd most-simple-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Starting the server

Run the API server with:

```bash
uvicorn main:app --reload
```

By default, the server will run on `http://127.0.0.1:8000`.

### Endpoints

The API provides the following endpoints for book management:

- `POST /books/{book_id}` - Create a new book
- `GET /books/{book_id}` - Retrieve a book by ID
- `PATCH /books/{book_id}` - Update an existing book
- `DELETE /books/{book_id}` - Delete a book

### Data Model

Each book contains the following fields:

- `title`: String (required)
- `author`: String (required)
- `description`: String (optional)

### Example Requests

#### Create a Book
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "description": "A novel about the American Dream"}' \
  http://localhost:8000/books/1
```

Response:
```json
{
  "msg": "Book created",
  "book": {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "description": "A novel about the American Dream"
  }
}
```

#### Get a Book
```bash
curl http://localhost:8000/books/1
```

Response:
```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "description": "A novel about the American Dream"
}
```

#### Update a Book
```bash
curl -X PATCH -H "Content-Type: application/json" \
  -d '{"description": "A classic novel exploring the American Dream in the 1920s"}' \
  http://localhost:8000/books/1
```

Response:
```json
{
  "msg": "Book updated",
  "book": {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "description": "A classic novel exploring the American Dream in the 1920s"
  }
}
```

#### Delete a Book
```bash
curl -X DELETE http://localhost:8000/books/1
```

Response:
```json
{
  "msg": "Book deleted",
  "book": {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "description": "A classic novel exploring the American Dream in the 1920s"
  }
}
```

## API Documentation

FastAPI automatically generates interactive API documentation. After starting the server, you can access:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Implementation Details

The API uses:
- In-memory dictionary to store books
- Pydantic models for data validation
- FastAPI for routing and HTTP handling
- HTTP exceptions for error handling

## Development

### Structure

```
most-simple-api/
├── main.py          # Main application file with API implementation
├── README.md        # Project documentation
```

### Error Handling

The API returns appropriate HTTP status codes:
- 400: Bad Request (when trying to create a book with an ID that already exists)
- 404: Not Found (when trying to access, update, or delete a non-existent book)

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or support, please open an issue on the GitHub repository.
