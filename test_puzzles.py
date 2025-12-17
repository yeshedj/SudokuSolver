"""
Author: Yeshe Jangchup
Date: December 2025

File: test_puzzles.py 
Description: This file contains test cases used to make sure the Sudoku Solver is able to solve across different puzzle difficulties and edge cases.

Test puzzles sourced from:
- Easy/Medium/Hard: Sudoku examples from Sudoku.com printable puzzles (12/16/2025) [https://sudoku.com/sudoku-printable]
- Invalid: Custom puzzle to test edge case
- Minimal: Puzzle with a minimum of 17 clues, mathematically proven and established by Gary McGuire's team [https://arxiv.org/pdf/1201.0749]
"""

from sudoku_solver import solve_sudoku, print_board, count_empty_cells, is_valid_puzzle
import time


def test_easy():
    """
    Easy test puzzle 
    """
    print("\n" + "="*60)
    print("TEST 1: EASY PUZZLE")
    print("="*60)
    
    puzzle = [
        [0, 0, 2, 7, 0, 1, 0, 0, 6],
        [0, 0, 0, 6, 9, 0, 0, 1, 0],
        [0, 9, 6, 0, 8, 0, 0, 5, 3],
        [9, 8, 4, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 6, 4, 0],
        [6, 0, 3, 0, 0, 5, 8, 0, 0],
        [0, 7, 8, 0, 1, 4, 9, 0, 0],
        [4, 2, 0, 3, 6, 7, 0, 0, 5],
        [5, 0, 1, 0, 0, 9, 3, 0, 4]
    ]
    
    print(f"Empty cells: {count_empty_cells(puzzle)}")
    print("Original puzzle:")
    print_board(puzzle)
    
    start_time = time.time()
    solved = solve_sudoku(puzzle)
    end_time = time.time()
    
    if solved:
        print("✅ SOLVED!")
        print_board(puzzle)
        print(f"Time taken: {end_time - start_time:.4f} seconds")
    else:
        print("🚫 No solution found")
    
    return solved


def test_medium():
    """
    Medium test puzzle
    """
    print("\n" + "="*60)
    print("TEST 2: MEDIUM PUZZLE")
    print("="*60)
    
    puzzle = [
        [0, 9, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 6],
        [0, 0, 3, 5, 0, 0, 8, 0, 0],
        [8, 6, 0, 3, 1, 0, 0, 7, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 2],
        [1, 2, 0, 6, 0, 0, 5, 3, 0],
        [0, 1, 0, 0, 0, 3, 2, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 7],
        [6, 0, 8, 2, 4, 7, 0, 0, 0]
    ]
    
    print(f"Empty cells: {count_empty_cells(puzzle)}")
    print("Original puzzle:")
    print_board(puzzle)
    
    start_time = time.time()
    solved = solve_sudoku(puzzle)
    end_time = time.time()
    
    if solved:
        print("✅ SOLVED!")
        print_board(puzzle)
        print(f"Time taken: {end_time - start_time:.4f} seconds")
    else:
        print("🚫 No solution found")
    
    return solved


def test_hard():
    """
    Hard test puzzle 
    """
    print("\n" + "="*60)
    print("TEST 3: HARD PUZZLE")
    print("="*60)
    
    puzzle = [
        [6, 0, 0, 3, 0, 1, 0, 8, 4],
        [0, 0, 0, 0, 6, 9, 0, 0, 7],
        [0, 0, 0, 0, 0, 7, 0, 1, 3],
        [4, 0, 0, 6, 9, 0, 0, 0, 8],
        [0, 0, 0, 0, 1, 5, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 7, 0, 0],
        [2, 0, 4, 0, 0, 3, 1, 0, 0]
    ]
    
    print(f"Empty cells: {count_empty_cells(puzzle)}")
    print("Original puzzle:")
    print_board(puzzle)
    
    print("Solving...")
    start_time = time.time()
    solved = solve_sudoku(puzzle)
    end_time = time.time()
    
    if solved:
        print("✅ SOLVED!")
        print_board(puzzle)
        print(f"Time taken: {end_time - start_time:.4f} seconds")
    else:
        print("🚫 No solution found")
    
    return solved


def test_invalid():
    """
    Invalid test puzzle 
    """
    print("\n" + "="*60)
    print("TEST 4: INVALID PUZZLE (No Solution)")
    print("="*60)
    
    puzzle = [
        [4, 3, 0, 0, 7, 0, 0, 0, 4],  
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [0, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print(f"Empty cells: {count_empty_cells(puzzle)}")
    print("Original puzzle:")
    print_board(puzzle)
    
    if not is_valid_puzzle(puzzle):
        print("⚠️ Warning: This puzzle is invalid!")
    
    start_time = time.time()
    solved = solve_sudoku(puzzle)
    end_time = time.time()
    
    if solved:
        print("✅ SOLVED! (Unexpected)")
        print_board(puzzle)
    else:
        print("🚫 No solution found! (as expected)")
        print(f"Time taken: {end_time - start_time:.4f} seconds")
    
    return not solved  


def test_minimal():
    """
    Puzzle with minimum number of clues (17)
    """
    print("\n" + "="*60)
    print("TEST 5: MINIMAL PUZZLE (McGuire's 17 clue puzzle)")
    print("="*60)
    
    puzzle = [
        [0, 0, 0, 8, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 3],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 2, 0, 0, 3, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 7, 5],
        [0, 0, 3, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 6, 0, 0]
    ]
    
    print(f"Empty cells: {count_empty_cells(puzzle)}")
    print("Original puzzle:")
    print_board(puzzle)
    
    print("Solving... (this may take a moment)")
    start_time = time.time()
    solved = solve_sudoku(puzzle)
    end_time = time.time()
    
    if solved:
        print("✅ SOLVED!")
        print_board(puzzle)
        print(f"Time taken: {end_time - start_time:.4f} seconds")
    else:
        print("🚫 No solution found")
    
    return solved


def run_all_tests():
    """
    Runs all 5 test cases and reports the results
    """
    print("\n")
    print("*" * 67)
    print("*" + " " * 65 + "*")
    print("*" + " " * 22 + "SUDOKU SOLVER TESTS" + " " * 24 + "*")
    print("*" + " " * 17 + "Using Backtracking Algorithm" + " " * 20 + "*")
    print("*" + " " * 65 + "*")
    print("*" * 67)
    
    tests = [
        ("Easy", test_easy),
        ("Medium", test_medium),
        ("Hard", test_hard),
        ("Invalid", test_invalid),
        ("Minimal", test_minimal)
    ]
    
    results = []
    total_start = time.time()
    
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n🚫 Test '{name}' failed with error: {e}")
            results.append((name, False))
    
    total_end = time.time()
    

    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "🚫 FAIL"
        print(f"{name:15} {status}")
    
    print("-"*70)
    print(f"Total: {passed}/{total} tests passed")
    print(f"Total time: {total_end - total_start:.4f} seconds")
    print("="*70 + "\n")


if __name__ == "__main__":
    run_all_tests()