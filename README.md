# eight_queens_python
[![Build Status](https://travis-ci.org/LuisBrime/eightqueenspython.svg?branch=master)](https://travis-ci.org/LuisBrime/eightqueenspython)

This is the solution for [Eight Queens Puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) written in Python.

## Tests
Found in test_basic.py

Tests were written with **pytest** and contiuosly tested each commit by **TravisCI**.

Solutions for the queens puzzle with N = 8 queens to N = 17 can be tested. By default the only test is for 8 Queens but the others can be uncommented.
 
## Run the code
### Prerequisites
- [Docker](https://docs.docker.com/v17.09/engine/installation/#cloud)
- [Docker-Compose](https://docs.docker.com/compose/install/)

1. Clone this repository

2. Start containers
Run the following command:
```
sudo docker-compose up -d --build
```

3. Run containers
Run the following command:
```
sudo docker-compose run web python main.py db postgres_queens
```

Running the code will solve for 8 Queens, it prints the number of solutions and each of them and stores them in a PostgreSQL Database.

To connect to the database and check for the solutions, run the following code:

```
sudo docker exec -it postgres_queens psql -U brime -d queensdb
```

This will enable you to type queries to the table *solutions*, for example:

```
SELECT * FROM solutions;
```