# sudoku.py
import os
import sys
from src.puzzle import Solver, Generator, Auxil

filename = "Sudoku"

def main():
    if sys.argv[1] == "-g":
        generate(int(sys.argv[2]), int(sys.argv[3]))
        return
    
    if sys.argv[1] == "-s":
        solve()
        return
    
    print("Invalid parameters")

def generate(num_puzzles: int, num_start_blocks: int):
    gen = Generator()
    aux = Auxil()
    ans = ""

    puzzle = gen.generate_puzzle(num_start_blocks, num_puzzles)
    for i in range(num_puzzles):
        ans += f"Puzzle {i+1}\n\n" + aux.return_puzzle(puzzle[i]) + "\n"
    
    save_to_file(ans, 'w')

def solve():
    solv = Solver()
    aux = Auxil()
    ans = ""

    for i, puzzle in enumerate(read_puzzles_from_file()):
        ans += f"Puzzle {i+1}\n\n" + aux.return_puzzle(solv.solve_puzzle(puzzle)) + "\n"

    save_to_file(ans, 'w')

def save_to_file(string: str, save_type: chr):
    try:
        with open(filename, save_type) as file:
            file.write(string)
    except IOError as e:
        print(f"Error saving content to {filename}: {e}")

def read_puzzles_from_file() -> list:
    aux = Auxil()
    puzzles = []
    current_puzzle = []
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Remove any leading/trailing whitespace
            
            # Skip empty lines
            if not line:
                continue
            
            # Check if line starts with "Puzzle"
            if line.startswith("Puzzle"):
                if current_puzzle:
                    # Parse current_puzzle and add to puzzles list
                    puzzles.append(aux.parse_puzzle(current_puzzle))
                    current_puzzle = []  # Reset current_puzzle
            else:
                current_puzzle.append(line)  # Append the puzzle line
        
        # Add the last puzzle in the file
        if current_puzzle:
            puzzles.append(aux.parse_puzzle(current_puzzle))
    
    return puzzles

if __name__ == "__main__":
    main()