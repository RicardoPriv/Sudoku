import math

class SudokuValidator:
    #initializes the class with a puzzle to validate
    def __init__(self, puzzle: list):
        self.puzzle = puzzle
        
    #checks if the number in the Sudoku puzzle is valid at a given position
    def valid_number_at_pos(self, position: int) -> bool:
        return self.horizontal(position) and self.vertical(position) and self.box(position)

    #validates along the horizontal plane
    def horizontal(self, position: int) -> bool:
        row = position // 9
        number = self.puzzle[position]

        for i in range(row * 9, (row+1) * 9):
            if self.puzzle[i] == number and i != position:
                return False
            
        return True

    #validates along the vertical plane
    def vertical(self, position: int) -> bool:
        col = position % 9
        number = self.puzzle[position]

        for i in range(9):
            if self.puzzle[col + 9 * i] == number and (col + 9 * i) != position:
                return False

        return True

    #validates within the relevant 3x3 box
    def box(self, position: int) -> bool:
        number = self.puzzle[position]
        row = (position // 9 // 3) * 27
        col = (position % 9 // 3) * 3
        walk_pos = row + col

        for i in range(3):
            for j in range(3):
                if self.puzzle[walk_pos + j] == number and (walk_pos + j) != position:
                    return False
            walk_pos += 9

        return True