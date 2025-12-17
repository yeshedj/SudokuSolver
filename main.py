"""
main.py
COMP 221 Final Project - Sudoku Solver using Backtracking

Main file for the Sudoku Solver program, giving a simple menu interface for running tests/solving puzzles.
Uses puzzles from the Sudoku Exchange Puzzle Bank (https://github.com/grantm/sudoku-exchange-puzzle-bank).
"""

from sudoku_solver import (
    solve_sudoku, 
    print_board,
    count_empty_cells,
    is_valid_puzzle
)
from test_puzzles import run_all_tests
import sys
import time
import random


def solve_custom_puzzle():
    """
    Allows the user to input a custom puzzle manually
    """
    while True: 
        print("\n" + "="*60)
        print("CUSTOM PUZZLE SOLVER")
        print("="*60)
        print("\nEnter your puzzle row by row (9 digits each, use 0 for empty):")
        print("Example: 530070000")
        print()
        
        puzzle = []
        for i in range(9):
            while True:
                row_input = input(f"Row {i+1}: ").strip().replace('.', '0')
                
                if len(row_input) == 9 and all(c in '0123456789' for c in row_input):
                    row = [int(c) for c in row_input]
                    puzzle.append(row)
                    break
                else:
                    print("  Invalid input. Please enter exactly 9 digits (0-9).")
        
        print("\nYour puzzle:")
        print_board(puzzle)
        
        if not is_valid_puzzle(puzzle):
            print("⚠️ Invalid: duplicates in row, column, or box, or incomplete (17 clue minimum)")
            response = input("\nTry reentering the puzzle? (y/n): ")
            if response.lower() != 'y':
                return
        else:
            break
    
    print(f"Empty cells: {count_empty_cells(puzzle)}")
    print("\nSolving...")
    
    start_time = time.time()
    if solve_sudoku(puzzle):
        end_time = time.time()
        print("\n✅ SOLVED!")
        print_board(puzzle)
        print(f"Time taken: {end_time - start_time:.4f} seconds")
    else:
        end_time = time.time()
        print("\n🚫 No solution found :( The puzzle may be invalid!")
        print(f"Time taken: {end_time - start_time:.4f} seconds")


def solve_from_puzzle_bank():
    """
    Loads and solves puzzles from the Sudoku Exchange Puzzle Bank.
    100 puzzles selected from the 'easy.txt', 'medium.txt', and 'hard.txt' files.
    """
    print("\n" + "="*60)
    print("SOLVE FROM PUZZLE BANK")
    print("="*60)
    print("\nPuzzle bank files from:")
    print("https://github.com/grantm/sudoku-exchange-puzzle-bank")
    
    print("\nSelect difficulty level:")
    print("  1. Easy")
    print("  2. Medium") 
    print("  3. Hard")
    print("  4. Back to main menu")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == '4':
        return
    
    difficulty_files = {
        '1': 'puzzle_bank/easy-puzzles.txt',
        '2': 'puzzle_bank/medium-puzzles.txt',
        '3': 'puzzle_bank/hard-puzzles.txt'
    }
    
    if choice in difficulty_files:
        filename = difficulty_files[choice]
    else:
        print("\n🚫 Invalid choice")
        return
    
    try:
        puzzles = load_puzzles_from_bank_file(filename)
        
        if not puzzles:
            print("\n🚫 No valid puzzles found!")
            return
        
        print(f"\nFound {len(puzzles)} puzzle(s) in file.")
        
        print("\nOptions:")
        print("  1. Solve a random puzzle")
        print(f"  2. Solve a specific puzzle (1-{len(puzzles)})")
        print("  3. Back to main menu")
        
        solve_choice = input("\nEnter choice (1-3): ").strip()
        
        if solve_choice == '3':
            return
        elif solve_choice == '1':
            puzzle = random.choice(puzzles)
            print(f"\nSolving a random puzzle from {len(puzzles)} available...")
            solve_a_puzzle(puzzle)
        elif solve_choice == '2':
            puzzle_num = input(f"Enter puzzle number (1-{len(puzzles)}): ").strip()
            try:
                puzzle_num = int(puzzle_num)
                if 1 <= puzzle_num <= len(puzzles):
                    print(f"\nSolving puzzle #{puzzle_num}...")
                    solve_a_puzzle(puzzles[puzzle_num - 1]) 
                else:
                    print(f"\n🚫 Please enter a number between 1 and {len(puzzles)}")
            except ValueError:
                print("\n🚫 Invalid number.")
        else:
            print("\n🚫 Invalid choice.")
    
    except FileNotFoundError:
        print(f"\n🚫 Error: File '{filename}' not found.")
        print("\nMake sure puzzle files are in the 'puzzle_bank/' folder")
    except Exception as e:
        print(f"\n🚫 Error loading puzzle: {e}")


def load_puzzles_from_bank_file(filename):
    """
    Loads puzzles from Sudoku Exchange Puzzle Bank "Easy", "Medium", and "Hard" files.
    Each line contains: puzzle_id puzzle_string difficulty_rating
    (e.g.: 0000183b305c 050703060007000800000816000000030000005000100730040086906000204840572093000409000  1.2)
    """
    puzzles = []
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            if not line or line.startswith('#'):
                continue
            
            parts = line.split()
            
            if len(parts) >= 2:
                puzzle_str = parts[1].replace('.', '0')
                
                if len(puzzle_str) == 81 and all(c in '0123456789' for c in puzzle_str):
                    puzzle = convert_puzzle_string(puzzle_str)
                    puzzles.append(puzzle)
    
    return puzzles


def convert_puzzle_string(puzzle_str):
    """
    Converts the 81-character string into a 9x9 puzzle board
    """
    board = []
    puzzle_str = puzzle_str.replace('.', '0')
    
    for i in range(9):
        row = []
        for j in range(9):
            digit = int(puzzle_str[i * 9 + j])
            row.append(digit)
        board.append(row)
    
    return board


def solve_a_puzzle(puzzle):
    """
    Solves and displays a single puzzle
    """
    print("\nOriginal puzzle:")
    print_board(puzzle)
    
    if not is_valid_puzzle(puzzle):
        print("⚠️ Warning: This puzzle is invalid!")
    
    print(f"Empty cells: {count_empty_cells(puzzle)}")
    print("\nSolving...")
    
    start_time = time.time()
    
    puzzle_copy = [row[:] for row in puzzle]
    
    if solve_sudoku(puzzle_copy):
        end_time = time.time()
        print("\n✅ SOLVED!")
        print_board(puzzle_copy)
        print(f"Time taken: {end_time - start_time:.4f} seconds")
    else:
        end_time = time.time()
        print("\n🚫 No solution found.")
        print(f"Time taken: {end_time - start_time:.4f} seconds")


def show_menu():
    """
    Displays the main menu
    """
    print("\n" + "="*60)
    print(" " * 20 + "SUDOKU SOLVER 🔢🧩")
    print(" " * 15 + "Using Backtracking Algorithm")
    print("="*60)

    
    print("\nOptions:")
    print("  1. Run all test cases")
    print("  2. Solve puzzle from puzzle bank")
    print("  3. Solve a custom puzzle (manual entry)")
    print("  4. Exit")
    print()


def main():
    """
    The main program loop
    """
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            run_all_tests()
        elif choice == '2':
            solve_from_puzzle_bank()
        elif choice == '3':
            solve_custom_puzzle()
        elif choice == '4':
            print("\nThank you for using Sudoku Solver!")
            sys.exit(0)
        else:
            print("\n🚫 Invalid choice! Please enter 1, 2, 3, or 4.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted.")
        print("Byebye!\n")
        sys.exit(0)