from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from app import schemas
from app.db import crud
from app.db.db import get_db


router = APIRouter(
    prefix="/books",
    tags=["books"],
)


@router.get("/", response_model=list[schemas.BookRead])
def read_books(
    category_id: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    if category_id is not None:
        category = crud.get_category_by_id(db, category_id)

        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found",
            )

        return crud.get_books_by_category(db, category_id)

    return crud.get_books(db)


@router.get("/{book_id}", response_model=schemas.BookRead)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    return book


@router.post(
    "/",
    response_model=schemas.BookRead,
    status_code=status.HTTP_201_CREATED,
)
def create_book(
    book_data: schemas.BookCreate,
    db: Session = Depends(get_db),
):
    category = crud.get_category_by_id(db, book_data.category_id)

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category does not exist",
        )

    return crud.create_book(
        db=db,
        title=book_data.title,
        description=book_data.description,
        price=book_data.price,
        url=book_data.url,
        category_id=book_data.category_id,
    )


@router.put("/{book_id}", response_model=schemas.BookRead)
def update_book(
    book_id: int,
    book_data: schemas.BookUpdate,
    db: Session = Depends(get_db),
):
    book = crud.get_book_by_id(db, book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    update_data = book_data.model_dump(exclude_unset=True)

    if "category_id" in update_data:
        category = crud.get_category_by_id(db, update_data["category_id"])

        if category is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Category does not exist",
            )

    updated_book = crud.update_book(
        db=db,
        book_id=book_id,
        **update_data,
    )

    return updated_book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    is_deleted = crud.delete_book(db, book_id)

    if not is_deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
