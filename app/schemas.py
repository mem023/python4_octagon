from pydantic import BaseModel, ConfigDict, Field


class CategoryBase(BaseModel):
    title: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BookBase(BaseModel):
    title: str
    description: str | None = None
    price: float = Field(ge=0)
    url: str | None = None
    category_id: int


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    price: float | None = Field(default=None, ge=0)
    url: str | None = None
    category_id: int | None = None


class BookRead(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
