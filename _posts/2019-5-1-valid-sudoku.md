---
title:  "36. Valid Sudoku"
date:   2019-05-01 10:22:00 +0930
categories: Leetcode
tags: Medium Matrix
---

[{{page.title}}](https://leetcode.com/problems/valid-sudoku/){:target="_blank"}

    Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the
    following rules:

        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.


    A partially filled sudoku which is valid.

    The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

    Example 1:

    Input:
    [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    Output: true


```java
HashSet[] cols = new HashSet[9], rows = new HashSet[9], subs = new HashSet[9];
public boolean isValidSudoku(char[][] board) {
    for(int i = 0; i < 9; i++) {
        cols[i] = new HashSet<Character>();
        rows[i] = new HashSet<Character>();
        subs[i] = new HashSet<Character>();
    }
    for(int i = 0; i < board.length; i++) {
        for(int j = 0; j < board.length; j++) {
            int subKey = toKey(i, j);
            char v = board[i][j];
            if(v == '.') continue;
            if(cols[j].contains(v) || rows[i].contains(v) || subs[subKey].contains(v))
                return false;
            cols[j].add(v);
            rows[i].add(v);
            subs[subKey].add(v);
        }
    }
    return true;
}
public int toKey(int i, int j) {
    return i / 3 * 3 + j / 3;
}
```
