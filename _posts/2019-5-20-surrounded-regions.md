---
title:  "130. Surrounded Regions"
date:   2019-05-20 15:37:00 +0930
categories: Leetcode
tags: Medium Graph Matrix
---

[{{page.title}}](https://leetcode.com/problems/surrounded-regions/){:target="_blank"}

    Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in that surrounded region.

    Example:

    X X X X
    X O O X
    X X O X
    X O X X

    After running your function, the board should be:

    X X X X
    X X X X
    X X X X
    X O X X

    Explanation:

    Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.


```java
class Solution {
    int[] xs = {0,0,1,-1}, ys = {1,-1,0,0};
    public void solve(char[][] board) {
        if(board == null || board.length == 0 || board[0] == null || board[0].length == 0) return;
        for(int i = 0; i < board.length; i++) {
            mark(board, i, 0);
            mark(board, i, board[0].length-1);
        }
        for(int j = 0; j < board[0].length; j++) {
            mark(board, 0, j);
            mark(board, board.length-1, j);
        }

        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[0].length; j++) {
                char c = board[i][j];
                if(c == 'B') board[i][j] = 'O';
                if(c == 'O') board[i][j] = 'X';
            }
        }

    }

    public void mark(char[][] board, int i, int j) {
        if(board[i][j] == 'B' || board[i][j] == 'X' ) return;
        board[i][j] = 'B';
        for(int k = 0; k < 4; k++) {
            int nx = xs[k] + i, ny = ys[k] + j;
            if(nx >= 0 && ny >= 0 && nx < board.length && ny < board[0].length && board[nx][ny] != 'B' && board[nx][ny] != 'X') {
                mark(board, nx, ny);
            }
        }
    }
  }
```
