---
title:  "52. N-Queens II"
date:   2019-05-22 21:43:00 +0930
categories: Leetcode
tags: Hard Backtrack NP
---

[{{page.title}}](https://leetcode.com/problems/n-queens-ii/){:target="_blank"}

    The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

    Given an integer n, return the number of distinct solutions to the n-queens puzzle.

    Example:

    Input: 4
    Output: 2
    Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
    [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],

     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]

* Easy

```java
ArrayList<int[]> qs;
boolean[] js;
int result = 0;
public int totalNQueens(int n) {
    qs = new ArrayList<>();
    js = new boolean[n];
    build(n, 0);
    return result;
}

public void build(int n, int row) {
    if(row == n) {
        result++;
        return;
    }
    for(int j = 0; j < n; j++) {
        if(!check(row, j)) continue;
        qs.add(new int[] {row, j});
        js[j] = true;
        build(n, row+1);
        js[j] = false;
        qs.remove(qs.size()-1);
    }
}

public boolean check(int i, int j) {
    if(js[j]) return false;
    for(int[] q : qs) {
        if(Math.abs(q[0]-i) == Math.abs(q[1]-j)) return false;
    }
    return true;
}
```
