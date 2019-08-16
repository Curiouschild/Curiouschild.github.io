---
title:  "329. Longest Increasing Path in a Matrix"
date:   2019-4-24 12:17:00 +0930
categories: Leetcode
tags: Matrix Search DFS Hard
---

[{{page.title}}](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/){:target="_blank"}

    Given an integer matrix, find the length of the longest increasing path.

    From each cell, you can either move to four directions: left, right, up or down. You may NOT move
    diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

    Example 1:

    Input: nums =
    [
      [9,9,4],
      [6,6,8],
      [2,1,1]
    ]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9].

    Example 2:

    Input: nums =
    [
      [3,4,5],
      [3,2,6],
      [2,2,1]
    ]
    Output: 4
    Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.





* Recursive with memo pad

```java
class Solution {
    int[] xs = {0,0,-1,1};
    int[] ys = {1,-1,0,0};
    public int longestIncreasingPath(int[][] matrix) {
        if(matrix.length == 0 || matrix[0].length == 0) return 0;
        int result = 0;
        int[][] memo = new int[matrix.length][matrix[0].length];
        for(int i = 0; i < matrix.length; i++) {
            for(int j = 0; j < matrix[0].length; j++) {
                result = Math.max(result, backtrack(matrix, i, j,memo));
            }
        }
        return result;
    }

    public int backtrack(int[][] matrix, int x, int y, int[][] memo) {
        if(memo[x][y] > 0) return memo[x][y];
        int result = 0;
        for(int k = 0; k < 4; k++) {
            int nx = x + xs[k], ny = y + ys[k];
            if(!check(matrix, nx, ny)) continue;
            if(matrix[nx][ny] <= matrix[x][y]) continue;
            int sub = backtrack(matrix, nx, ny, memo);
            result = Math.max(result, sub);
        }
        memo[x][y] = result + 1;
        return result+1;
    }

    public boolean check(int[][] matrix, int i, int j) {
        return i >= 0 && j >= 0 && matrix.length > i && j < matrix[0].length;
    }
  }
```
