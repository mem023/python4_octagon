from app.db.db import SessionLocal, engine
from app.db.models import Base
from app.db.crud import create_book, create_category, get_books


def init_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        programming = create_category(db, "Программирование")
        databases = create_category(db, "Базы данных")

        create_book(
            db=db,
            title="Python для начинающих",
            description="Книга для изучения основ Python.",
            price=1200,
            url="",
            category_id=programming.id,
        )

        create_book(
            db=db,
            title="Чистый код",
            description="Книга о написании понятного и поддерживаемого кода.",
            price=1800,
            url="",
            category_id=programming.id,
        )

        create_book(
            db=db,
            title="SQL основы",
            description="Книга для изучения SQL-запросов.",
            price=1000,
            url="",
            category_id=databases.id,
        )

        create_book(
            db=db,
            title="PostgreSQL на практике",
            description="Книга о работе с PostgreSQL.",
            price=1500,
            url="",
            category_id=databases.id,
        )

        books = get_books(db)

        print("База данных успешно создана и заполнена.")
        print(f"Добавлено книг: {len(books)}")

    finally:
        db.close()


if __name__ == "__main__":
    init_database()
