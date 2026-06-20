from app.db.db import SessionLocal
from app.db.crud import get_categories

print("Hello, World!")

def main():
    db = SessionLocal()

    try:
        categories = get_categories(db)

        print("Категории и книги из базы данных:")
        print("-" * 50)

        for category in categories:
            print(f"Категория: {category.title}")

            if not category.books:
                print("  Книг нет")

            for book in category.books:
                print(f"  Книга: {book.title}")
                print(f"  Описание: {book.description}")
                print(f"  Цена: {book.price}")
                print(f"  URL: {book.url}")
                print()

            print("-" * 50)

    finally:
        db.close()


if __name__ == "__main__":
    main()