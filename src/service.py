import uvicorn
from typing import Optional
from fastapi import FastAPI, Header, status
from models import BookDataModel
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/get_headers", status_code=status.HTTP_200_OK)
async def get_header(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None)
):
    request_header = {}
    request_header["Accept"] = accept
    request_header["Content-Type"] = content_type
    request_header["User-Agent"] = user_agent
    request_header["Host"] = host
    return request_header

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