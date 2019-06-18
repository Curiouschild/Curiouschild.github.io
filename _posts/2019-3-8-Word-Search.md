---
title:  "79. Word Search"
date:   2019-3-8 16:52:13 +0930
categories: Leetcode
tags: Graph
---

[{{page.title}}](https://leetcode.com/problems/coin-change-2/){:target="_blank"}

    Given a 2D board and a word, find if the word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cell,
    where "adjacent" cells are those horizontally or vertically neighboring.
    The same letter cell may not be used more than once.

    Example:

    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

    Given word = "ABCCED", return true.
    Given word = "SEE", return true.
    Given word = "ABCB", return false.

* BackTraking

```java
public boolean exist(char[][] board, String word) {
    for(int i = 0; i < board.length; i++) {
        for(int j = 0; j < board[0].length; j++) {
            if(dfs(board, word, 0, i, j)) return true;
        }
    }
    return false;
}

public boolean dfs(char[][] board, String word, int index, int i, int j) {
    if(index == word.length()) return true;
    if(!inBound(board, i, j) || word.charAt(index) != board[i][j]) return false;
    board[i][j] = '*';
    int[] xs = {1,-1,0,0}, ys = {0,0,1,-1};
    for(int k = 0; k < 4; k++) {
        int ni = i + xs[k], nj = j + ys[k];
        if(dfs(board, word, index + 1, ni, nj)) return true;
    }
    board[i][j] = word.charAt(index);
    return false;
}

public boolean inBound(char[][] board, int i, int j) {
    return i >= 0 && j >= 0 && i < board.length && j < board[0].length;
}
```
