import uvicorn
from typing import Optional
from fastapi import FastAPI, Header, status
from models import BookDataModel
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get('/get_headers', status_code=status.HTTP_200_OK)
async def get_all_request_headers(
    user_agent: Optional[str] = Header(None),
    accept_encoding: Optional[str] = Header(None),
    referer: Optional[str] = Header(None),
    connection: Optional[str] = Header(None),
    accept_language: Optional[str] = Header(None),
    host: Optional[str] = Header(None),
):
    request_headers = {}
    request_headers["User-Agent"] = user_agent
    request_headers["Accept-Encoding"] = accept_encoding
    request_headers["Referer"] = referer
    request_headers["Accept-Language"] = accept_language
    request_headers["Connection"] = connection
    request_headers["Host"] = host

    return request_headers

@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
async def read_item(item_id: int, q: Optional[str] = None) -> dict:
    """
    'http://127.0.0.1:8000/items/3?q=hello' 
    """
    return {"item_id": item_id, "q": q}

@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: BookDataModel):
    return {
        "title": book_data.title,
        "author": book_data.author,
        "description": book_data.description,
        "price": book_data.price    
    }

if __name__ == "__main__":
    uvicorn.run("service:app", host="0.0.0.0", port=8000, reload=True)