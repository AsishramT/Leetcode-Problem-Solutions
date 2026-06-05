# 36. Valid Sudoku

[36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
Solved  
Medium

## Problem

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain digits `1-9` without repetition
- Each column must contain digits `1-9` without repetition
- Each of the nine `3 x 3` sub-boxes must contain digits `1-9` without repetition

---

## Notes

- A Sudoku board may be **partially filled**
- It does not need to be solvable
- Only validity rules matter

---

## Example 1

```text
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: true
```

---

## Example 2

```text
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: false
```

Explanation:

There are duplicate `8`s in the top-left 3×3 box.

---

## Constraints

- `board.length == 9`
- `board[i].length == 9`
- Each cell is a digit `'1'-'9'` or `'.'`