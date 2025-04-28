from fastapi import FastAPI, status, HTTPException
from models import Book, BookResponse, BookUpdate
from db.example_db_book import books

def get_all_books():
    return books

def get_next_book_id():
    if books:
        return max(book["id"] for book in books) + 1
    return 1

app = FastAPI(
    title="Book API",
    description="A simple CRUD API for books",
    version="1.0.0",
)

@app.get("/books", tags=["books"], response_model=list[BookResponse])
async def read_books() -> list[BookResponse]:
    return get_all_books()


@app.get("/book/{book_id}", tags=["books"], response_model=BookResponse)
async def read_book(book_id: int) -> BookResponse:
    """Get a book by ID."""
    for book in books:
        if book["id"] == book_id:
            return BookResponse(**book)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {book_id} not found",
    )

@app.post("/books", tags=["books"], response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(new_book_data: Book) -> BookResponse:
    new_book = new_book_data.model_dump()
    new_book["id"] = get_next_book_id()
    
    if any(book["title"] == new_book["title"] for book in books):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A book with the same title already exists.",
        )
    
    books.append(new_book)
    return BookResponse(**new_book)


@app.patch("/book/{book_id}", tags=["books"], response_model=BookResponse, status_code=status.HTTP_202_ACCEPTED)
async def update_book(book_id: int, book_update_data: BookUpdate):
    for book in books:
        if book["id"] == book_id:
            # Hanya perbarui atribut yang diberikan oleh pengguna
            update_data = book_update_data.model_dump(exclude_unset=True)
            book.update(update_data)
            return BookResponse(**book)
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {book_id} not found.",
    )


@app.delete("/book/{book_id}", tags=["books"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_id(book_id: int):
    """
    Delete book by ID
    """
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {book_id} not found."
    )
