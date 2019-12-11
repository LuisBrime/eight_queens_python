# eight_queens_python
[![Build Status](https://travis-ci.org/LuisBrime/eightqueenspython.svg?branch=master)](https://travis-ci.org/LuisBrime/eightqueenspython)

This is the solution for [Eight Queens Puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) written in Python.

## Tests
Found in test_basic.py

Tests were written with **pytest** and contiuosly tested each commit by **TravisCI**.

Solutions for the queens puzzle with N = 8 queens to N = 17 can be tested. By default the only test is for 8 Queens but the others can be uncommented.
 
## Run the code
### Prerequisites
- Docker
- Docker-Compose

1. Run this repository

2. Start containers
Run the following command:
```
docker-compose up -d --build
```

3. Run containers
Run the following command:
```
docker-compose run web python main.py db postgres_queens
```