from fastapi import FastAPI

from app.api import books, categories
from app.db.db import engine
from app.db.models import Base

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Books API",
    description="API для работы с книгами и категориями",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(categories.router)
app.include_router(books.router)