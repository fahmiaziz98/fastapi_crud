# FastAPI CRUD Example

This is a simple CRUD API for managing books using FastAPI.

## Features
- **Get All Books**: Retrieve a list of all books.
- **Get Book by ID**: Retrieve details of a specific book by its ID.
- **Create Book**: Add a new book to the collection.
- **Update Book**: Update specific fields of an existing book.
- **Delete Book**: Remove a book from the collection.

## Example Payload
### Create or Update Book
```json
{
  "title": "Overlord",
  "author": "Maruyama Sensei",
  "publisher": "Tokyo Novel",
  "published_date": "2019-06-19",
  "page_count": 300,
  "language": "JP-EN"
}
```

## Endpoints
### Get All Books
- **GET** `/books`

### Get Book by ID
- **GET** `/book/{book_id}`

### Create Book
- **POST** `/books`

### Update Book
- **PATCH** `/book/{book_id}`

### Delete Book
- **DELETE** `/book/{book_id}`