# game-of-life
[![python](https://img.shields.io/badge/python-3.9-teal)](https://www.python.org/downloads/)

A simple implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life ) using Python. Uses [ascii-animator](https://pypi.org/project/ascii-animator/) to animate the game to the terminal.

## Execution using Docker image
```bash
docker container run --rm -it soda480/game-of-life:latest
```
![example](https://raw.githubusercontent.com/soda480/game-of-life/main/docs/images/game-of-life.gif)

## Execution without Docker
Clone this repository to your machine, then change directory to the directory where the repository was cloned.

Install requirements:
```bash
pip install -r requirements.txt
```

Execute script:
```bash
python game.py
```

## Execution using locally built Docker image
Clone this repository to your machine, then change directory to the directory where the repository was cloned.

Build Docker Image:
```bash
docker image build -t game-of-life:latest .
```

Run Docker Container:
```bash
docker container run --rm -it game-of-life:latest
```
