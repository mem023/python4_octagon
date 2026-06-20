from sqlalchemy import ForeignKey, Numeric, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    books: Mapped[list["Book"]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan",
    )


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    url: Mapped[str] = mapped_column(String(500), nullable=True)

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False,
    )

    category: Mapped[Category] = relationship(back_populates="books")
