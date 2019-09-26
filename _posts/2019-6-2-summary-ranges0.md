---
title:  "419. Battleships in a Board"
date:   2019-06-02 10:45:00 +0930
categories: Leetcode
tags: Medium Matrix
---

[{{page.title}}](https://leetcode.com/problems/max-increase-to-keep-city-skyline/){:target="_blank"}

    Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty
    slots are represented with '.'s. You may assume the following rules:

        You receive a valid board, made of only battleships or empty slots.
        Battleships can only be placed horizontally or vertically. In other words, they can only be made of the
        shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
        At least one horizontal or vertical cell separates between two battleships - there are no adjacent
        battleships.

    Example:

    X..X
    ...X
    ...X

    In the above board there are 2 battleships.

    Invalid Example:

    ...X
    XXXX
    ...X

    This is an invalid board that you will not receive - as battleships will always have a cell separating between them.

    Follow up:
    Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?


* Follow up
  - easier than Medium
  - count the # of horizontal consecutive X --> result
  - for each vertical ship of length N --> result -= (N-1) // minus overcount vertical ships
```java

public int countBattleships(char[][] board) {
    int result = 0;
    for(int i = 0; i < board.length; i++) {
        int cnt = 0;
        boolean hasX = false;
        for(int j = 0; j < board[0].length; j++) {
            if(board[i][j] == 'X') {
                hasX = true;
                if(i+1 < board.length && board[i+1][j] == 'X')
                    result--;
            } else {
                if(hasX) result++;
                hasX = false;
            }
        }
        if(hasX) result++;
    }
    return result;
}
```

* Modify boards
```java
public int countBattleshipsModifyBoard(char[][] board) {
    int result = 0;
    for(int i = 0; i < board.length; i++) {
        for(int j = 0; j < board[0].length; j++) {
            if(board[i][j] == 'X') {
                result++;
                for(int x = i; x >= 0 && board[x][j] == 'X'; x--) board[x][j] = '.';
                for(int x = i+1; x < board.length && board[x][j] == 'X'; x++) board[x][j] = '.';
                for(int y = j; y >= 0 && board[i][y] == 'X'; y--) board[i][y] = '.';
                for(int y = j+1; y < board[0].length && board[i][y] == 'X'; y++) board[i][y] = '.';

            }
        }
    }
    return result;
}
```
