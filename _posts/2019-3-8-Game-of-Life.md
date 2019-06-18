---
title:  "289. Game of Life"
date:   2019-3-8 12:18:11 +0930
categories: Leetcode
tags: Game
---

[{{page.title}}](https://leetcode.com/problems/game-of-life/){:target="_blank"}


    According to the Wikipedia's article: "The Game of Life, also known simply as Life,
    is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

    Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
    Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using
    the following four rules (taken from the above Wikipedia article):

        Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population..
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

    Write a function to compute the next state (after one update) of the board given its
    current state. The next state is created by applying the above rules simultaneously
    to every cell in the current state, where births and deaths occur simultaneously.

    Example:

    Input:
    [
      [0,1,0],
      [0,0,1],
      [1,1,1],
      [0,0,0]
    ]
    Output:
    [
      [0,0,0],
      [1,0,1],
      [0,1,1],
      [0,1,0]
    ]


```java
public void gameOfLife(int[][] board) {
    int[] xs = {0,0,1,1,1,-1,-1,-1};
    int[] ys = {1,-1,0,1,-1,0,1,-1};
    // 0. d-d
    // 1. l-l
    // 2. l-d
    // 3. d-l
    for(int i = 0; i < board.length; i++) {
        for(int j = 0; j < board[0].length; j++) {
            int live = 0;
            for(int k = 0; k < 8; k++) {
                int nx = i + xs[k], ny = j + ys[k];
                if(nx >= 0 && ny >= 0 && nx < board.length && ny < board[0].length) {
                    if(board[nx][ny] == 1 || board[nx][ny] == 2) live++;
                }
            }
            if(board[i][j] == 1 && (live < 2 || live > 3)) board[i][j] = 2;
            if(board[i][j] == 0 && live == 3) board[i][j] = 3;
        }
    }
    for(int i = 0; i < board.length; i++) {
        for(int j = 0; j < board[0].length; j++) {
            if(board[i][j] == 3) board[i][j] = 1;
            if(board[i][j] == 2) board[i][j] = 0;
        }
    }

}
```
