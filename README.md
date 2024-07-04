# Sudoku Solver/Generator

This project is a Python-based Sudoku puzzle solver and generator. The solver uses a backtracking algorithm to solve given Sudoku puzzles, while the generator creates new puzzles with a specified number of initially filled cells.

## Features

- **Sudoku Solver**: Uses a backtracking algorithm to solve Sudoku puzzles.
- **Sudoku Generator**: Generates Sudoku puzzles with a given number of initial numbers.

## Usage

### Generating Sudoku Puzzles

To generate Sudoku puzzles with a specified number of initial numbers:

```sh
python3 sudoku.py -g <number_of_initial_numbers> <number_of_puzzles>
```

To solve Sudoku puzzles:

```sh
python3 sudoku.py -s
```
## Note

All generated puzzles are output to a "Sudoku" textfile and granted that an unsolved puzzle is formatted correctly, the solver will draw the puzzles from the same texfile and replace them with their solved counterparts.


