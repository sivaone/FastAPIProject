# Create a POST endpoint using FastAPI to add a new book to the collection. The endpoint should accept a JSON payload with the book's title, author, and publication year. The book should be added to an in-memory list of books.
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    year: int

books: List[Book] = []

@app.post("/books/")
def add_book(book: Book):
    books.append(book)
    return book

# Create a GET endpoint to retrieve the list of all books in the collection.
@app.get("/books/")
def get_books():
    return books

# Create a GET endpoint to retrieve a book by its title.
@app.get("/books/{title}")
def get_book_by_title(title: str):
    """
    Retrieve a book from the books collection by its title.
    
    Args:
        title (str): The title of the book to search for.
    
    Returns:
        dict: The book object matching the given title.
    
    Raises:
        HTTPException: If no book with the given title is found (404 status code).
    
    Example:
        >>> get_book_by_title("The Great Gatsby")
        {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', ...}
    """
    for book in books:
        if book.title == title:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Create a DELETE endpoint to remove a book from the collection by its title.
@app.delete("/books/{title}")
def delete_book(title: str):
    for book in books:
        if book.title == title:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
