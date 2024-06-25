import random
import multiprocessing
from multiprocessing.pool import Pool
from validator import SudokuValidator

x = 0

class Solver:
    def __init__(self):
        pass
    
    def backtrack_solver(self, puzzle: list) -> bool:
        validator = SudokuValidator(puzzle)

        def solve_recursive() -> bool:
            for i in range(81):
                if puzzle[i] == x:
                    for number in range(1, 10):
                        puzzle[i] = number
                        if validator.valid_number_at_pos(i):
                            if solve_recursive():
                                return True
                        puzzle[i] = x  # Backtrack
                    return False  # No valid number found for this position
            return True  # Puzzle solved

        return solve_recursive()

class Generator:
    def __init__(self):
        self.solver = Solver()
    
    def attempt_gen_puzzle(self, begin_numbers: int) -> list:
        while True:
            puzzle = [0] * 81  # Initialize the puzzle with 81 zeros
            filled_positions = set()
            i = 0
            
            while i < begin_numbers:
                num = random.randint(1, 9)
                position = random.randint(0, 80)
                if position not in filled_positions:  # Ensure position is not already filled
                    puzzle[position] = num
                    if not SudokuValidator(puzzle).valid_number_at_pos(position):
                        puzzle[position] = 0  # Reset if not valid
                    else:
                        filled_positions.add(position)
                        i += 1
          
            # Check if the generated puzzle is solvable
            if self.solver.backtrack_solver(puzzle):
                for i in range(0, 81):
                    if i not in filled_positions:
                        puzzle[i] = 0
                return puzzle  # Return the solvable puzzle
            
    def generate_puzzle(self, begin_numbers: int) -> list:
        gen = Generator()
        pool = multiprocessing.Pool()
        solving = []

        while True:
            p = pool.apply_async(gen.attempt_gen_puzzle, (begin_numbers,))
            solving.append(p)

            for process in solving:
                if process.ready():
                    solved_puzzle = process.get()
                    pool.terminate()
                    pool.join()
                    return solved_puzzle
    
class Auxil:
    def print_puzzle(self, puzzle: list):
        for i in range(81):
            if puzzle[i] == 0:
                print('x', end=' ')
            else:
                print(puzzle[i], end=' ')
            
            if (i + 1) % 9 == 0:
                print()