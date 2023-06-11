FROM python:3.8.10-alpine

LABEL author="di.zhu.jude@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY . /app

WORKDIR /app
EXPOSE 8000

RUN apk add --no-cache gcc

RUN python -m venv /py &&\
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home app

ENV PATH="/py/bin:$PATH"

USER app
