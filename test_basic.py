import pytest
from eightqueens import QueensSolver

# Total number of solutions for N Queens from 8 to 17
# Source: https://en.wikipedia.org/wiki/Eight_queens_puzzle
numberOfSolutions = [
    92,
    352,
    724,
    2680,
    14200,
    73712,
    365596,
    2279184,
    14772512,
    95815104
]

def test_eightqueen_solver():
    solver = QueensSolver(8)
    assert len(solver.solutions) == numberOfSolutions[0]

# def test_ninequeen_solver():
#     solver = QueensSolver(9)
#     assert len(solver.solutions) == numberOfSolutions[1]

# def test_tenqueen_solver():
#     solver = QueensSolver(10)
#     assert len(solver.solutions) == numberOfSolutions[2]

# def test_elevenqueen_solver():
#     solver = QueensSolver(11)
#     assert len(solver.solutions) == numberOfSolutions[3]

# def test_twelvequeen_solver():
#     solver = QueensSolver(12)
#     assert len(solver.solutions) == numberOfSolutions[4]

# def test_thirteenqueen_solver():
#     solver = QueensSolver(13)
#     assert len(solver.solutions) == numberOfSolutions[5]

# def test_fourteenqueen_solver():
#     solver = QueensSolver(14)
#     assert len(solver.solutions) == numberOfSolutions[6]

# def test_fifteenqueen_solver():
#     solver = QueensSolver(15)
#     assert len(solver.solutions) == numberOfSolutions[7]

# def test_sixteenqueen_solver():
#     solver = QueensSolver(16)
#     assert len(solver.solutions) == numberOfSolutions[8]

# def test_seventeenqueen_solver():
#     solver = QueensSolver(17)
#     assert len(solver.solutions) == numberOfSolutions[9]