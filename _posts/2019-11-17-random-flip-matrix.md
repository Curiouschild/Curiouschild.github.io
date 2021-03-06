---
title:  "519. Random Flip Matrix"
date:   2019-11-17 19:02:00 +0930
categories: Leetcode
tags: Medium Randomness
---

[{{page.title}}](https://leetcode.com/problems/random-flip-matrix/){:target="_blank"}

    You are given the number of rows n_rows and number of columns n_cols of a 2D binary matrix where all values are
    initially 0. Write a function flip which chooses a 0 value uniformly at random, changes it to 1, and then returns
    the position [row.id, col.id] of that value. Also, write a function reset which sets all values back to 0. Try to
    minimize the number of calls to system's Math.random() and optimize the time and space complexity.

    Note:

        1 <= n_rows, n_cols <= 10000
        0 <= row.id < n_rows and 0 <= col.id < n_cols
        flip will not be called when the matrix has no 0 values left.
        the total number of calls to flip and reset will not exceed 1000.

    Example 1:

    Input:
    ["Solution","flip","flip","flip","flip"]
    [[2,3],[],[],[],[]]
    Output: [null,[0,1],[1,2],[1,0],[1,1]]

    Example 2:

    Input:
    ["Solution","flip","flip","reset","flip"]
    [[1,2],[],[],[],[]]
    Output: [null,[0,0],[0,1],null,[0,0]]



* Virtual Mapping

```java

class Solution {
    Map<Integer, Integer> V = new HashMap<>();
    int nr, nc, rem;
    Random rand = new Random();

    public Solution(int n_rows, int n_cols) {
        nr = n_rows;
        nc = n_cols;
        rem = nr * nc;
    }

    public int[] flip() {
        int r = rand.nextInt(rem--);
        int x = V.getOrDefault(r, r);
        V.put(r, V.getOrDefault(rem, rem));
        return new int[]{x / nc, x % nc};
    }

    public void reset() {
        V.clear();
        rem = nr * nc;
    }
}

```
