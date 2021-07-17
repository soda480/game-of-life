#   -*- coding: utf-8 -*-
FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /game
COPY . /game/
RUN pip install mp4ansi
ENTRYPOINT ["python", "/game/game.py"]
