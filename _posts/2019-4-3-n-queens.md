---
title:  "51. N-Queens"
date:   2019-4-3 21:04:00 +0930
categories: Leetcode
tags: Backtracking
---

[{{page.title}}](https://leetcode.com/problems/n-queens/){:target="_blank"}



    The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that
    no two queens attack each other.

    Given an integer n, return all distinct solutions to the n-queens puzzle.

    Each solution contains a distinct board configuration of the n-queens' placement, where
    'Q' and '.' both indicate a queen and an empty space respectively.

![p1](/img/posts/n_queens.png)

    Example:

    Input: 4
    Output: [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],

     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
    Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.



* Backtracking

```java
public List<List<String>> solveNQueens(int n) {
    List<List<String>> result = new ArrayList<>();
    HashSet<Integer> cols = new HashSet<>();
    StringBuilder sb = new StringBuilder();
    LinkedList<int[]> qs = new LinkedList<>();
    for(int i = 0; i < n * n; i++) sb.append('.');
    backtrack(result, cols, qs, sb, n, 0);
    return result;
}

public void backtrack(List<List<String>> result, HashSet<Integer> cols, LinkedList<int[]> qs, StringBuilder sb, int n, int row) {
    out:for(int i = 0; i < n; i++) {
        if(cols.contains(i)) continue;
        int sum = row + i, diff = row - i;
        for(int[] q : qs) {
            if(q[0] + q[1] == sum || q[0] - q[1] == diff)
                continue out;
        }
        cols.add(i);
        qs.add(new int[] {row, i});
        sb.setCharAt(row*n+i, 'Q');
        if(row == n-1) {
            ArrayList<String> temp = new ArrayList<>();
            for(int j = 0; j < n; j++) {
                temp.add(sb.substring(j*n, j*n+n));
            }
            result.add(temp);
        }
        backtrack(result, cols, qs, sb, n, row+1);
        qs.removeLast();
        sb.setCharAt(row*n+i, '.');
        cols.remove(i);
    }
```
