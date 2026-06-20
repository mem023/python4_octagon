from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import schemas
from app.db import crud
from app.db.db import get_db


router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@router.get("/", response_model=list[schemas.CategoryRead])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.get("/{category_id}", response_model=schemas.CategoryRead)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, category_id)

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return category


@router.post(
    "/",
    response_model=schemas.CategoryRead,
    status_code=status.HTTP_201_CREATED,
)
def create_category(
    category_data: schemas.CategoryCreate,
    db: Session = Depends(get_db),
):
    existing_category = crud.get_category_by_title(db, category_data.title)

    if existing_category is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category already exists",
        )

    return crud.create_category(db, category_data.title)


@router.put("/{category_id}", response_model=schemas.CategoryRead)
def update_category(
    category_id: int,
    category_data: schemas.CategoryUpdate,
    db: Session = Depends(get_db),
):
    category = crud.update_category(
        db=db,
        category_id=category_id,
        title=category_data.title,
    )

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return category


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    is_deleted = crud.delete_category(db, category_id)

    if not is_deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
