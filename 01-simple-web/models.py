from pydantic import BaseModel

class BookDataModel(BaseModel):
    title: str
    author: str
    description: str
    price: float