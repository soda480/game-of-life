# game-of-life
[![python](https://img.shields.io/badge/python-3.9-teal)](https://www.python.org/downloads/)

A simple implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life ) using Python.

## Execution using Docker
```bash
docker container run \
--rm -it \
soda480/game-of-life:latest
```
![example](https://raw.githubusercontent.com/soda480/game-of-life/main/docs/images/execution.gif)

## Execution without Docker
Clone this repository to your machine, then change directory to the directory where the repository was cloned.

Install requirements
```bash
pip install -r requirements.txt
```

Execute script
```bash
python game.py
```