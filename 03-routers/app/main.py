from fastapi import FastAPI
from app.api.routers.book_router import book_router

app = FastAPI(
    title="Book API",
    description="A simple CRUD API for books",
    version="1.0",
)

app.include_router(book_router)