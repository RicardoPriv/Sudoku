import os
from validator import SudokuValidator

x = 0
sudoku_puzzle = [
        5, 3, x, x, 7, x, x, x, x,
        6, x, x, 1, 9, 5, x, x, x,
        x, 9, 8, x, x, x, x, 6, x,
        8, x, x, x, 6, x, x, x, 3,
        4, x, x, 8, x, 3, x, x, 1,
        7, x, x, x, 2, x, x, x, 6,
        x, 6, x, x, x, x, 2, 8, x,
        x, x, x, 4, 1, 9, x, x, 5,
        x, x, x, x, 8, x, x, 7, 9
    ]

def backtrack_solver(puzzle: list) -> bool:
    validator = SudokuValidator(puzzle)

    def solve_recursive():
        for i in range(81):
            if puzzle[i] == x:
                for number in range(1, 10):
                    puzzle[i] = number
                    if validator.valid_number_at_pos(i):
                        if solve_recursive():
                            return True
                    puzzle[i] = x  # Backtrack
                return False  # No valid number found for this position
        print_puzzle(puzzle)
        return True  # Puzzle solved

    return solve_recursive()

def print_puzzle(puzzle: list):
    puz = []
    for i in range(81):
        puz.append(puzzle[i])
        if (i+1) % 9 == 0:
            print(puz)
            puz = []

def get_number(puzzle: list, position: int) -> int:
    for number in range(1,10):
        puzzle[position] = number
        validator = SudokuValidator(puzzle)
        if validator.valid_number_at_pos(position):
            return number
    
    return -1

if __name__ == "__main__":
    backtrack_solver(sudoku_puzzle)