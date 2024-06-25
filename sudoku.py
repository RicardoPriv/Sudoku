# sudoku.py
import os
from puzzle import Generator, Auxil

if __name__ == "__main__":
    gen = Generator()
    aux = Auxil()
    puzzle = gen.generate_puzzle(17)
    aux.print_puzzle(puzzle)