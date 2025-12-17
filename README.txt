# Sudoku Solver 

## COMP 221 Final Project
This project implements a backtracking algorithm to solve Sudoku puzzles, recursively trying digits 1-9 in empty cells and backtracking when it encounters invalid placements that violate Sudoku rules.

---

## Files Included

1. **sudoku_solver.py** - Core backtracking algorithm and helper functions
2. **test_puzzles.py** - Test cases of different difficulties and situations.
3. **main.py** - Main program with the menu interface
4. **puzzle_bank/** - Folder containing puzzle files from ([Sudoku Exchange "Puzzle Bank"](https://github.com/grantm/sudoku-exchange-puzzle-bank))

---

## How to Run

Run main.py which loads the interactive menu, where you can:
### Option 1: Run All Tests which will run 5 test cases (easy, medium, hard, invalid, minimal) and show timing results.
### Option 2: Solve puzzles from a puzzle bank (easy/medium/hard)
### Option 3: Solve a custom, manually entered, puzzle
### Option 4: Exit the program

---

## Puzzle Sources

### Test Puzzles (`test_puzzles.py`)

The test puzzles were completed by hand and chosen to make sure it demonstrates algorithm correctness:

1. **Easy Puzzle** - Standard easy-level puzzle from 12/16 Printable Sudoku.com Puzzles
2. **Medium Puzzle** - Standard medium-level puzzle from 12/16 Printable Sudoku.com Puzzles
3. **Hard Puzzle** - Standard hard-level puzzle from 12/16 Printable Sudoku.com Puzzles
4. **Invalid Puzzle** - Custom puzzle with a duplicate number 4 (unsolvable)
5. **Minimal Puzzle** - 17-clue puzzle from ([Gary McGuire's paper](https://arxiv.org/pdf/1201.0749))


### Puzzle Bank (`puzzle_bank/`)

This folder contains a subset of puzzles from the **Sudoku Exchange "Puzzle Bank"**:
- Source repository: https://github.com/grantm/sudoku-exchange-puzzle-bank
- Puzzles are initally stored in a standardized .sdm format, including the puzzle_id, puzzle_string, and difficulty_rating (e.g. 0000183b305c 050703060007000800000816000000030000005000100730040086906000204840572093000409000 1.2)
- Each puzzle is represented by an 81-character string that is converted into a 9x9 board
- For this project, 100 puzzles were selected from the easy, medium, and hard difficulty level files.

Using puzzle bank:
1. Download the shortened, curated puzzle file included in this Sudoku Solver repository
2. Make sure they are placed in the `puzzle_bank/` directory
3. Run the program and select "Soleve puzzle from puzzle bank" from the main menu

---

## Manually Entering a Custom Puzzle
Custom puzzles should be entered as 9 rows with 9 digits each:
- Use `0` for empty cells
- Do not include spaces or separators
- Make sure the puzzle contains at least the theoretical minimum of 17 clues
- Make sure there are no duplicates in any row, column, or 3x3 box

---

## Algorithm Explanation

### Backtracking Steps:
1. Searches for an empty cell, scanning the board left-to-right, top-to-bottom
2. Tries all the possible digits, 1-9, in that cell
3. For every digit, checks if the placement is valid
4. If valid, places the digit and recursively solves the rest
5. If the recursive call returns True, success! We're done!
6. If it fails, removes the digit and tries the next one (backtracking)
7. If no digit works, returns False to signal a dead end
8. If no empty cells remain, returns True and puzzle is solved!

---

## Future Improvements

Possible extensions (not required for this project):
- Being able to upload your own txt files
- Adding an aesthethic Graphical user interface (GUI) for you to try solving the puzzle on your own then the Backtracking algorithm checks for you
- Step-by-step visualization showing backtracking in action

---

## References
- **Easy/Medium/Hard puzzles**: 12/16/2025 Printable Sudoku.com Puzzles
- **Minimal puzzle**: Gary McGuire's 17-clue puzzle (University College Dublin)
- **Puzzle bank**: Sudoku Exchange "Puzzle Bank" by Grant McLean (https://github.com/grantm/sudoku-exchange-puzzle-bank)
