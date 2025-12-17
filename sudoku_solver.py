"""
sudoku_solver.py
COMP 221 Final Project - Sudoku Solver using Backtracking

This file contains the core backtracking algorithm and helper functions for solving 9x9 Sudoku puzzles.
"""


def print_board(board):
    """
    Prints the Sudoku board in a formatted way with grid lines
    """
    print("\n" + "="*37)
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 37)
        
        row_str = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_str += " | "
            
            if board[i][j] == 0:
                row_str += " . "
            else:
                row_str += f" {board[i][j]} "
        
        print(row_str)
    print("="*37 + "\n")


def is_valid(board, row, col, num):
    """
    Checks if placing 'num' at position (row, col) is valid or not according to Sudoku rules.
    
    Returns True if:
    - 'num' is not already in the same row
    - 'num' is not already in the same column
    - 'num' is not already in the same box

    """
    for j in range(9):
        if board[row][j] == num:
            return False
    
    for i in range(9):
        if board[i][col] == num:
            return False
    
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    
    for i in range(box_row_start, box_row_start + 3):
        for j in range(box_col_start, box_col_start + 3):
            if board[i][j] == num:
                return False
    
    return True


def find_empty_cell(board):
    """
    Finds the next empty cell (represented by 0) in the board and scans left-to-right, top-to-bottom
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def solve_sudoku(board, show_steps=False):
    """
    Solves the Sudoku puzzle using backtracking recursion.
    
    ALGORITHM:
    1. Finds an empty cell
    2. Try digits 1-9 in that cell
    3. For every digit, checks if it is valid
    4. If valid, places it and recursively solves the rest
    5. If the recursive call succeeds, yay, we're done!
    6. If it fails, backtrack to remove the digit and try the next one
    7. If no digit works, returns False (and triggers backtracking in previous call)
    """
    empty_cell = find_empty_cell(board)
    if empty_cell is None:
        return True
    
    row, col = empty_cell
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if show_steps:
                print(f"Trying {num} at ({row}, {col})")
                print_board(board)
                input("Press Enter to continue...")
            
            if solve_sudoku(board, show_steps):
                return True 
            
            board[row][col] = 0
            
            if show_steps:
                print(f"Backtracking from ({row}, {col})")
    
    return False


def load_puzzle_from_string(puzzle_string):
    """
    Converts a string representation of a puzzle into a 9x9 board. Uses 0 for empty cells
    """
    board = []
    puzzle_string = puzzle_string.replace('.', '0')
    
    for i in range(9):
        row = []
        for j in range(9):
            digit = int(puzzle_string[i * 9 + j])
            row.append(digit)
        board.append(row)
    
    return board


def count_empty_cells(board):
    """
    Counts how many empty cells are in puzzle
    """
    count = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                count += 1
    return count


def is_valid_puzzle(board):
    """
    Checks if the initial puzzle configuration is valid. Makes sure of no 
    duplicate numbers in any rows, columns, or boxes, and at least 17 clues
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = board[i][j]
                board[i][j] = 0 
                if not is_valid(board, i, j, num):
                    board[i][j] = num  
                    return False
                board[i][j] = num  
    return True

