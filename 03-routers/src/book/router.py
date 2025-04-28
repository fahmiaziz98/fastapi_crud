from fastapi import APIRouter, status, HTTPException
from src.book.book_data import books
from src.book.schema import Book, BookResponse, BookUpdate

def get_all_books():
    return books

def get_next_book_id():
    if books:
        return max(book["id"] for book in books) + 1
    return 1

book_router = APIRouter(prefix="/api/v1", tags=["books"])

@book_router.get("/books", tags=["books"], response_model=list[BookResponse])
async def read_books() -> list[BookResponse]:
    return get_all_books()


@book_router.get("/book/{book_id}", tags=["books"], response_model=BookResponse)
async def read_book(book_id: int) -> BookResponse:
    """Get a book by ID."""
    for book in books:
        if book["id"] == book_id:
            return BookResponse(**book)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {book_id} not found",
    )

@book_router.post("/books", tags=["books"], response_model=BookResponse, status_code=status.HTTP_201_CREATED)
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


@book_router.patch("/book/{book_id}", tags=["books"], response_model=BookResponse, status_code=status.HTTP_202_ACCEPTED)
async def update_book(book_id: int, book_update_data: BookUpdate):
    for book in books:
        if book["id"] == book_id:
            update_data = book_update_data.model_dump(exclude_unset=True)
            book.update(update_data)
            return BookResponse(**book)
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {book_id} not found.",
    )


@book_router.delete("/book/{book_id}", tags=["books"], response_model=dict, status_code=status.HTTP_200_OK)
async def delete_book_id(book_id: int):
    """
    Delete book by ID.
    """
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {
                "message": "Book deleted successfully", 
                "deleted_book": book
            }
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {book_id} not found."
    )