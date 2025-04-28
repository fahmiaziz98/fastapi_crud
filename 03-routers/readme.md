# FastAPI CRUD with Routers

This project demonstrates a CRUD API for managing books using FastAPI with routers.

## How to Run

1. **Navigate to the Project Directory**:
   ```bash
   cd 03-routers
   ```

2. **Run the FastAPI Application**:
   ```bash
   fastapi dev src/.
   ```

## Example Endpoint: Delete Book by ID

### Endpoint
```http
DELETE /api/v1/book/{book_id}
```


### Example Request
```bash
curl -X DELETE http://127.0.0.1:8000/api/v1/book/1
```

### Example Response
**Success**:
```json
{
    "message": "Book deleted successfully",
    "deleted_book": {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "page_count": 300,
        "language": "English"
    }
}
```

**Error (If Book Not Found)**:
```json
{
    "detail": "Book with id 1 not found."
}
```