#   -*- coding: utf-8 -*-
FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /code
COPY . /code/
RUN python -m pip install --upgrade build && python -m pip install .
ENTRYPOINT ["game-of-life"]