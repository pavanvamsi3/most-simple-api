# Most Simple API

A lightweight, minimalist API built with FastAPI for testing and demonstration purposes.

## Overview

This project provides a simple API with basic endpoints that can be used for:
- Testing API integrations
- Learning FastAPI framework
- Demonstrating HTTP methods (GET, POST, PUT, DELETE)
- Quick prototyping

## Features

- Basic CRUD operations
- Health check endpoint
- Simple authentication example
- Logging functionality
- Configurable port via environment variables

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
   pip install fastapi uvicorn
   ```

## Usage

### Starting the server

Run the API server with:

```bash
python main.py
```

By default, the server will run on port 8000. You can modify the port by setting the `PORT` environment variable.

### Endpoints

The API provides the following endpoints:

- `GET /` - Returns a welcome message
- `GET /health` - Health check endpoint
- `GET /items/{item_id}` - Retrieve an item by ID
- `POST /items/` - Create a new item
- `PUT /items/{item_id}` - Update an existing item
- `DELETE /items/{item_id}` - Delete an item

### Example Requests

#### Get Welcome Message
```bash
curl http://localhost:8000/
```

Response:
```json
{"message": "Welcome to the Most Simple API"}
```

#### Health Check
```bash
curl http://localhost:8000/health
```

Response:
```json
{"status": "healthy"}
```

#### Get an Item
```bash
curl http://localhost:8000/items/1
```

Response:
```json
{"item_id": 1, "name": "Example Item", "description": "This is an example item"}
```

#### Create an Item
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "New Item", "description": "A brand new item"}' http://localhost:8000/items/
```

Response:
```json
{"item_id": 2, "name": "New Item", "description": "A brand new item"}
```

## Configuration

You can configure the following settings:

- **PORT**: The port number for the server (default: 8000)
  ```bash
  PORT=9000 python main.py
  ```

## Logging

The API logs all requests to the console with timestamp, HTTP method, and endpoint information.

## Development

### Structure

```
most-simple-api/
├── main.py          # Main application file with API implementation
├── README.md        # Project documentation
```

### Extending the API

To add new endpoints, modify the `main.py` file following the existing patterns.

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or support, please open an issue on the GitHub repository.
