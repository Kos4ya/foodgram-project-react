FROM python:3.7-slim

WORKDIR /app

RUN pip install gunicorn==20.1.0

ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "--bind", "0:8000", "foodgram.wsgi"]
