FROM python:3.10-slim

WORKDIR /app

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN pip install poetry==2.1.3

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

CMD ["sh", "-c", "poetry run uvicorn app.main:app --host ${APP_HOST:-0.0.0.0} --port ${APP_PORT:-8000} --reload"]