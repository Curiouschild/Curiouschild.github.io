---
title:  "37. Sudoku Solver"
date:   2019-4-21 22:04:00 +0930
categories: Leetcode
tags: Recursive
---

[{{page.title}}](https://leetcode.com/problems/sudoku-solver/){:target="_blank"}

This problem reminds me the N-Queens problem: [N-queens](https://curiouschild.github.io/leetcode/2019/04/03/n-queens.html){:target="_blank"}

    Write a program to solve a Sudoku puzzle by filling the empty cells.

    A sudoku solution must satisfy all of the following rules:

        Each of the digits 1-9 must occur exactly once in each row.
        Each of the digits 1-9 must occur exactly once in each column.
        Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

    Empty cells are indicated by the character '.'.


    A sudoku puzzle...


    ...and its solution numbers marked in red.

    Note:

        The given board contain only digits 1-9 and the character '.'.
        You may assume that the given Sudoku puzzle will have a single unique solution.
        The given board size is always 9x9.




* BackTraking
```java
class Solution {
    HashSet[] rows = new HashSet[9], cols = new HashSet[9], subs = new HashSet[9];
    boolean find;
    public void solveSudoku(char[][] board) {
        for(int i = 0; i < 9; i++) rows[i] = new HashSet<Integer>();
        for(int i = 0; i < 9; i++) cols[i] = new HashSet<Integer>();
        for(int i = 0; i < 9; i++) subs[i] = new HashSet<Integer>();
        for(int i = 0; i < 9; i++)
            for(int j = 0; j < 9; j++)
                if(board[i][j] != '.')
                    visit(board[i][j]-'0', i, j, getSubIndex(i,j));
        backtrack(board, 0, 0);
    }

    public void backtrack(char[][] board, int i, int j) {
        if(find) return;
        if(j == 9) {
            i++;
            j = 0;
        }
        if(i == 9) {
            find = true;
            return;
        }
        int subIndex = getSubIndex(i, j);
        if(board[i][j] != '.')
            backtrack(board, i, j+1);
        else {
            for(int k = 1; k <= 9; k++) {
                if(isValid(k, i, j, subIndex)) {
                    board[i][j] = (char)(k + '0');
                    visit(k, i, j, subIndex);
                    backtrack(board, i, j+1);
                    if(find) return;
                    cancel(k, i, j, subIndex);
                    board[i][j] = '.';
                }
            }
        }
    }
    public void visit(int k, int i, int j, int z) {
        rows[i].add(k);
        cols[j].add(k);
        subs[z].add(k);
    }
    public void cancel(int k, int i, int j, int z) {
        rows[i].remove(k);
        cols[j].remove(k);
        subs[z].remove(k);
    }
    public boolean isValid(int k, int i, int j, int z) {
        return !(rows[i].contains(k) || cols[j].contains(k) || subs[z].contains(k));
    }

    public int getSubIndex(int i, int j) {
        return (i / 3) * 3 + (j / 3);
    }
}
```
