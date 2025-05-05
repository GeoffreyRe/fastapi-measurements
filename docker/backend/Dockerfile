FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential libpq-dev

WORKDIR /

COPY app /app

COPY docker/backend/src .

RUN pip3 install -r /requirements.txt

ENV PYTHONPATH=/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--reload-dir", "app", "--host", "0.0.0.0"]