from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory "database" of books
books_db: Dict[int, dict] = {}

# Pydantic model for a book
class Book(BaseModel):
    title: str
    author: str
    description: str = None

@app.post("/books/{book_id}")
def create_book(book_id: int, book: Book):
    if book_id in books_db:
        raise HTTPException(status_code=400, detail="Book already exists")
    books_db[book_id] = book.dict()
    return {"msg": "Book created", "book": books_db[book_id]}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[book_id]

@app.patch("/books/{book_id}")
def update_book(book_id: int, book: Book):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    books_db[book_id].update(book.dict(exclude_unset=True))
    return {"msg": "Book updated", "book": books_db[book_id]}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    deleted = books_db.pop(book_id)
    return {"msg": "Book deleted", "book": deleted}
