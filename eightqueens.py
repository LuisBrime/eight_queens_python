# Solution based on a previous solution I implemented on C++:
#       https://github.com/LuisBrime/eight-queens-cpp
class QueensSolver:
    def __init__(self, numberOfQueens):
        # N – Size of board; number of queens.
        self.numberOfQueens = numberOfQueens

        # List to store all solutions : [[Int]]
        self.solutions = []

        # Auxiliar list to store a single solution
        aux = [None] * numberOfQueens

        # Solve puzzle and store all solutions
        self.solve_queens(numberOfQueens, aux, 0)

    # solve_queens :: Int -> [Int] -> Int -> Void
    def solve_queens(self, board_size: int, solution: [int], queen: int):
        """Return all possible solutions for N Queens Problem

        Keyword arguments:
        board_size -- Number of Queens in the board and size of the board (NxN)
        solution -- Integer list auxiliar to store a solution.
        queen -- Current number of queen (also column)
        """
        # Each solution is an [Integer] of columns where each Integer represents the row in which queen #col is placed.
        if queen == board_size:
            self.solutions.append(solution.copy())
            return

        for row in range(board_size):
            if self.is_safe(solution, row, queen):
                solution[queen] = row

                self.solve_queens(board_size, solution, queen + 1)

                solution[queen] = None
    
    # is_safe :: [Int] -> Int -> Int -> Bool
    def is_safe(self, board: [int], row: int, col: int):
        """Check if it is safe to place a queen in the board.
        
        Keyword arguments:
        board -- Integer list representing columns, its values represent the row if a queen is placed.
        row -- Actual row to check for safeness.
        col -- Actual col to check for safeness.
        """
        safe_diagonals = True
        for c in range(len(board)):
            if board[c] != None:
                if board[c] + c == row + col or board[c] - c == row - col:
                    safe_diagonals = False
                    break

        return row not in board and safe_diagonals

if __name__ == '__main__':
    solver = QueensSolver(9)
    print(len(solver.solutions))