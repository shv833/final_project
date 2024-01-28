ARG PYTHON_VERSION=3.10.11
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install pipenv

COPY . .

RUN pipenv install --system --deploy --ignore-pipfile

# Run the application.
ENTRYPOINT  ["python", "__main__.py"]
