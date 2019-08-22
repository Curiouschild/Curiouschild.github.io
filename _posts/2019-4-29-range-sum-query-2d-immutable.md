---
title:  "304. Range Sum Query 2D - Immutable"
date:   2019-4-28 23:59:00 +0930
categories: Leetcode
tags: Medium Design
---

[{{page.title}}](https://leetcode.com/problems/range-sum-query-2d-immutable/){:target="_blank"}

    Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

    Range Sum Query 2D
    The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

    Example:

    Given matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]

    sumRegion(2, 1, 4, 3) -> 8
    sumRegion(1, 1, 2, 2) -> 11
    sumRegion(1, 2, 2, 4) -> 12

    Note:

        You may assume that the matrix does not change.
        There are many calls to sumRegion function.
        You may assume that row1 ≤ row2 and col1 ≤ col2.


* Calculate all sums TLE pass 11/12

```java

class NumMatrix {
    int[][][][] dp;
    int[][] matrix;

    public NumMatrix(int[][] matrix) {
        if(!(matrix == null || matrix.length == 0 || matrix[0] == null || matrix[0].length == 0)) {
            this.matrix = matrix;
            int n = matrix.length, m = matrix[0].length;
            dp = new int[n][m][n][m];
            for(int area = 1; area <= m*n; area++) {
                for(int a = 1; a <= area; a++) {
                    if(area % a != 0) continue;
                    int b = area / a;
                    for(int i = 0; i < n; i++) {
                        for(int j = 0; j < m; j++) {
                            int r = i + a - 1, c = j + b - 1;
                            if(r >= n || c >= m) continue;
                            if(r == i && c == j) dp[i][j][r][c] = matrix[i][j];
                            else if(a==1) {
                                dp[i][j][r][c] = dp[i][j][r][c-1] + matrix[r][c];
                            } else if(b==1) {
                                dp[i][j][r][c] = dp[i][j][r-1][c] + matrix[r][c];
                            } else {
                                dp[i][j][r][c] = dp[i][j][r][c-1] + dp[i][c][r][c];
                            }
                        }
                    }
                }
            }
        }
        System.out.println("fin");
    }
    public int sumRegion(int row1, int col1, int row2, int col2) {
        if(matrix == null) return -1;
        return dp[row1][col1][row2][col2];
    }
```
