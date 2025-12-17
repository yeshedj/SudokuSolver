# Sudoku Solver 🔢🧩 

This COMP 221 Algorithms project implements the _**Backtracking Algorithm**_ to solve Sudoku puzzles, recursively trying digits 1-9 in empty cells and backtracking when it encounters invalid placements that violate Sudoku rules.

#### Files Included:
1. **`main.py`**: Main program with the menu interface
2. **`sudoku_solver.py`**: Core backtracking algorithm and helper functions
3. **`test_puzzles.py`**: Test cases of different difficulties and situations
4. **`puzzle_bank/`**: Folder containing puzzle files 
---

### Using Sudoku Solver 🔢🧩!

Run main.py which loads the interactive menu, where you can:
- Option 1: Run All Tests which will run 5 test cases (easy, medium, hard, invalid, minimal) and show timing results.
- Option 2: Solve puzzles from a puzzle bank (easy/medium/hard)
- Option 3: Solve a custom, manually entered, puzzle
- Option 4: Exit the program

Using Puzzle Bank:
1. Download the 100-puzzle subset files, `easy-puzzles.txt` `medium-puzzles.txt` `hard-puzzles.txt`, included in this [Sudoku Solver repository](https://github.com/yeshedj/SudokuSolver/tree/main/puzzle_bank)
2. Make sure they are placed in the `puzzle_bank/` directory
3. Run the program and select "Option 2: Solve puzzle from puzzle bank" from the main menu

Manually Entering a Custom Puzzle
- Enter 9 digits in all 9 rows
- Use `0` for empty cells
- Do not include spaces or separators
- Make sure the puzzle contains at least the theoretical minimum of 17 clues
- Make sure there are no duplicates in any row, column, or 3x3 box

---

### Algorithm Explanation 

_**Backtracking Algorithm**_: a problem-solving approach that searches for solutions by incrementally building a solution, trying possible solutions, and abandoning (backtracking from) any choice that does not lead to a valid complete solution or results in a dead-end.

How Sudoku Solver 🔢🧩 Uses Backtracking:
1. Searches for an empty cell, scanning the board left-to-right, top-to-bottom
2. Tries all the possible digits, 1-9, in that cell
3. For every digit, checks if the placement is valid
4. If valid, places the digit and recursively solves the rest
5. If the recursive call returns True, success! We're done!
6. If it fails, removes the digit and tries the next one (backtracking)
7. If no digit works, returns False to signal a dead end
8. If no empty cells remain, returns True and puzzle is solved!

---

### Future Improvements
- Enable users to upload their own .txt puzzle files
- Add a step-by-step visualization that shows the backtracking algorithm process in action
- Create a user-friendly graphical user interface (GUI) where you can attempt the puzzle manually and then have the backtracking algorithm check your solution

---

#### Sources!
- **Easy/Medium/Hard puzzles**: [12/16/2025](https://github.com/yeshedj/SudokuSolver/blob/main/121625-sudoku.com-puzzle.jpg) [Printable Sudoku.com Puzzles](https://sudoku.com/sudoku-printable)
- **Minimal puzzle**: Dr. Gary McGuire (University College Dublin)'s ["Solving the Sudoku Minimum Number of Clues Problem" Paper](https://arxiv.org/pdf/1201.0749)
- **Puzzle bank**: [Sudoku Exchange "Puzzle Bank" Repository](https://github.com/grantm/sudoku-exchange-puzzle-bank) by Grant McLean
  - For this project, 100 puzzles were selected from the `easy.txt`, `medium.txt`, and `hard.txt` difficulty level files
  - These subset of puzzles for each level are stored in `puzzle_bank/`

