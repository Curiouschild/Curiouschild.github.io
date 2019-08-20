---
title:  "59. Spiral Matrix II"
date:   2019-4-27 23:32:00 +0930
categories: Leetcode
tags: Medium Matrix
---

[{{page.title}}](https://leetcode.com/problems/spiral-matrix-ii/){:target="_blank"}


    Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

    Example:

    Input: 3
    Output:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]

```java

public List<Integer> spiralOrder(int[][] m) {
    if(m.length == 0 || m[0].length == 0) return new ArrayList<>();
    int h = m.length, k = m[0].length;
    List<Integer> result = new ArrayList<>();
    for(int i = 0; i < h/2 && i < k/2; i++) {
        for(int col = i; col < k - i - 1; col++) result.add(m[i][col]);
        for(int row = i; row < h - i - 1; row++) result.add(m[row][k-i-1]);
        for(int col = k-i-1; col > i; col--) result.add(m[h-i-1][col]);
        for(int row = h-i-1; row > i; row--) result.add(m[row][i]);
    }
    if(k >= h && h % 2 == 1)
        for(int col = h / 2; col <= k - h/2 - 1; col++)
            result.add(m[h/2][col]);
    if(k < h && k % 2 == 1)
        for(int row = k/2; row <= h - k/2 - 1; row++)
            result.add(m[row][k/2]);
    return result;
}
```
