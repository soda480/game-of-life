#   -*- coding: utf-8 -*-
FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "/game/game.py"]