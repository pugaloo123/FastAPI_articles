# Статьи и комментарии — FastAPI

CRUD API для статей и системы комментариев к ним (Задача 4).

## Стек

- Python 3.10+
- FastAPI
- SQLModel (SQLAlchemy + Pydantic v2)
- SQLite (файл `articles.db` создаётся автоматически)
- Uvicorn

## Установка и запуск

1. Создать и активировать виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Запустить сервер:

   ```bash
   uvicorn app.main:app --reload
   ```

4. Открыть документацию Swagger:

   http://127.0.0.1:8000/docs

При первом запуске автоматически создаётся файл БД `articles.db` со всеми таблицами.


