# Post Filtering Service

Асинхронный сервис на FastAPI для фильтрации и анализа текстовых постов с использованием PostgreSQL и SQLAlchemy.

## Стек

- Python 3.11  
- FastAPI  
- SQLAlchemy 2 (async)  
- Alembic  
- PostgreSQL  
- Docker & Docker Compose

## Быстрый старт

1. Клонировать репозиторий:

```bash
git clone https://github.com/XRU13/posts_test.git
cd post_test
```

2. Собрать и запустить контейнеры:

```bash
docker compose up --build
```

- Поднимаются контейнеры FastAPI (`web`) и PostgreSQL (`db`)
- Автоматически применяются миграции
- Сервис доступен на http://localhost:8000

3. Заполнить базу мок-данными:

```bash
docker compose exec web python app/fixtures.py
```

## API

### GET `/posts`

Фильтрация и обработка постов на лету.

#### Параметры запроса:

| Параметр   | Тип     | Описание                                          |
|------------|----------|---------------------------------------------------|
| category   | string   | Фильтр по категории                               |
| keywords   | string[] | Ключевые слова через запятую (например: python,ai)|
| limit      | int      | Максимум записей (по умолчанию: 10)               |
| offset     | int      | Смещение (по умолчанию: 0)                        |

#### Пример запроса:

```
/posts/search?category=tech&keywords=python,async&limit=5
```

#### Пример ответа:

```json
{
  "total": 2,
  "limit": 5,
  "offset": 0,
  "items": [
    {
      "id": 1,
      "category": "tech",
      "top_words": [["python", 3], ["async", 2], ["programming", 1]],
      "tags": ["python"]
    }
  ]
}
```


##  Основные особенности

- Асинхронный SQLAlchemy с `asyncpg`
- Построчная обработка (`session.stream()`)
- Поддержка фильтрации, пагинации и анализа текста
- Частотный анализ слов и выделение тегов
- Чистое разделение слоёв (репозиторий / сервис)
- Возможность расширения (например, сохранение результатов)

