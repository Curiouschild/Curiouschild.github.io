---
title:  "221. Maximal Square"
date:   2019-05-13 15:09:00 +0930
categories: Leetcode
tags: Medium Matrix
---

[{{page.title}}](https://leetcode.com/problems/maximal-square/){:target="_blank"}

    Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return
    its area.

    Example:

    Input:

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

    Output: 4

* Check diagonals.

p1       p3


p2       p4


```java

public int maximalSquare(char[][] matrix) {
    if(matrix.length == 0) return 0;
    int[][] dp = new int[matrix.length+1][matrix[0].length+1];
    int result = 0;
    for(int i = 1; i < dp.length; i++) {
        for(int j = 1; j < dp[0].length; j++) {
            if(matrix[i-1][j-1] == '1') {
                dp[i][j] = 1 + Math.min(Math.min(dp[i-1][j-1], dp[i-1][j]), dp[i][j-1]);
                result = Math.max(result, dp[i][j] * dp[i][j]);
            }
        }
    }
    return result;
}
```
