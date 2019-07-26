FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src

WORKDIR /usr/src

COPY . .

RUN apk update && \
  apk add --no-cache --virtual .build-deps \
  ca-certificates gcc postgresql-dev linux-headers musl-dev \
  libffi-dev jpeg-dev zlib-dev && \
  pip install --upgrade pip && \
  pip install -r requirements.txt

EXPOSE 80 443

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000