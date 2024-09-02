# game-of-life
[![python](https://img.shields.io/badge/python-3.9-teal)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/game-of-life-animation.svg)](https://badge.fury.io/py/game-of-life-animation)

A simple implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life ) using Python. Uses [ascii-animator](https://pypi.org/project/ascii-animator/) to animate the game to the terminal.

## Install

```bash
pip install game-of-life-animation
```

## Execute

```bash
game-of-life
```

![example](https://raw.githubusercontent.com/soda480/game-of-life/main/docs/images/game-of-life.gif)

## Development

```bash
python -m pip install --upgrade build
python -m build
```

## Execution using Docker image
```bash
docker container run --rm -it soda480/game-of-life:latest
```

## Execution using locally built Docker image
Clone this repository to your machine, then change directory to the directory where the repository was cloned.

Build Docker Image:
```bash
docker image build -t game-of-life:latest .
```

Run Docker Container:
```bash
docker container run --rm -t game-of-life:latest
```

