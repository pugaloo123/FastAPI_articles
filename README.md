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

## Структура проекта

```
articles_api/
├── app/
│   ├── main.py            # точка входа, обработчики ошибок
│   ├── database.py        # подключение к БД
│   ├── models.py           # таблицы Article и Comment
│   ├── schemas.py          # Pydantic-схемы запросов/ответов
│   └── routers/
│       ├── articles.py     # эндпоинты /articles/...
│       └── comments.py     # эндпоинты /comments/{id}
├── requirements.txt
└── README.md
```

## Эндпоинты

| Метод  | Путь                          | Описание                              |
|--------|-------------------------------|----------------------------------------|
| GET    | /articles                     | Список статей (фильтр `?blog_id=X`)   |
| GET    | /articles/{id}                | Статья по ID + её комментарии          |
| POST   | /articles                     | Создать статью                         |
| PUT    | /articles/{id}                | Обновить статью                        |
| DELETE | /articles/{id}                | Удалить статью (каскадно с комментами) |
| GET    | /articles/{id}/comments       | Комментарии к статье                   |
| POST   | /articles/{id}/comments       | Добавить комментарий (404, если статьи нет) |
| PUT    | /comments/{comment_id}        | Обновить текст комментария             |
| DELETE | /comments/{comment_id}        | Удалить комментарий                    |

