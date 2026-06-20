# Python4 Octagon / Books API

Проект реализует работу с PostgreSQL через SQLAlchemy и API на FastAPI.

## Что реализовано

- PostgreSQL подключён через SQLAlchemy.
- Созданы модели Category и Book.
- Реализованы CRUD-функции для категорий и книг.
- Реализован API на FastAPI.
- Добавлены роуты /categories и /books.
- Добавлен эндпоинт /health.
- Swagger-документация доступна по адресу http://127.0.0.1:8000/docs.

## Запуск проекта

1. Активировать виртуальное окружение:

source venv/bin/activate

2. Запустить PostgreSQL:

sudo service postgresql start

3. Установить зависимости:

python3 -m pip install -r requirements.txt

4. Заполнить базу тестовыми данными:

python3 -m app.init_db

5. Запустить API:

uvicorn app.main:app --reload

## Проверка API

Health check:

http://127.0.0.1:8000/health

Swagger:

http://127.0.0.1:8000/docs

Список категорий:

http://127.0.0.1:8000/categories/

Список книг:

http://127.0.0.1:8000/books/
