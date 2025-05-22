# Сервис по управлению видеопотоками 🎬

Используемые технологии: **Python 3.10**, **FastAPI**, **Uvicorn**, **SQLAlchemy**, **Alembic**, **PostgreSQL**, **Redis**, **Celery**, **Flower**, **Pydantic**, **Poetry**, **Docker & Docker Compose**.

## 🚀 Основные задачи включают в себя:

-   Загрузку информации о видео
-   Генерацию HLS-плейлистов
-   Кеширование данных в Redis
-   Фоновую обработку задач с помощью Celery

---

## 🛠️ Клонирование и настройка

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/kamilgareev/streaming_app.git
    cd streaming_app
    ```

2.  **Создайте и настройте файл `.env`** в корне проекта. Вы можете использовать `.env.sample` как шаблон или скопировать данные ниже:
    ```env
    # app config
    APP_PORT=8000
    APP_HOST=0.0.0.0
    
    # postgres config
    POSTGRES_HOST=db
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=pass
    POSTGRES_DB=streaming_app_db
    POSTGRES_PORT=5432
    
    # redis config
    REDIS_HOST=redis
    REDIS_PORT=6379
    REDIS_CACHE_DB_NUM=0
    REDIS_BROKER_DB_NUM=1
    REDIS_RESULT_BACKEND_DB_NUM=2
    
    # flower config
    FLOWER_PORT=5555
    ```
---

## 🏁 Запуск проекта

1.  **Сборка и запуск приложения:**
    ```bash
    docker-compose up --build
    ```

2.  **Применение миграций базы данных:**
    ```bash
    docker-compose exec app poetry run alembic upgrade head
    ```

---

## 📚 Документация проекта:

-   **Swagger UI:**
    [`http://localhost:8000/docs`](http://localhost:8000/docs)
    *(или порт, указанный в `APP_PORT` вашего `.env` файла)*

## 📊 Мониторинг Celery задач:

-   **Flower (веб-интерфейс для мониторинга Celery задач):**
    [`http://localhost:5555`](http://localhost:5555)
    *(или порт, указанный в `FLOWER_PORT` вашего `.env` файла)*

---

## 🔌 API Эндпоинты

### `POST /api/videos/`
Добавление информации о новом видео.

-   **Content-Type:** `application/json`
-   **Тело запроса (Request Body):**
    ```json
    {
        "title": "Название видео",
        "url": "http://example.com/path/to/video.mp4"
    }
    ```
-   **Ответ (201 Created):**
    ```json
    {
        "id": 1,
        "title": "Название видео",
        "playlist_url": "http://example.com/hls/1.m3u8"
    }
    ```

### `GET /api/videos/{video_id}/`
Получение информации о видео по ID.

-   **Параметры пути:**
    -   `video_id` (integer): ID видео.
-   **Ответ (200 OK):**
    ```json
    {
        "id": 1,
        "title": "Название видео",
        "playlist_url": "http://example.com/hls/1.m3u8"
    }
    ```
-   **Ответ (404 Not Found):**
    ```json
    {
        "detail": "Video not found"
    }
    ```
---