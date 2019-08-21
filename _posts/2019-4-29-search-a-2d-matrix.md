---
title:  "74. Search a 2D Matrix"
date:   2019-4-28 10:48:00 +0930
categories: Leetcode
tags: Medium BinarySearch
---

[{{page.title}}](https://leetcode.com/problems/search-a-2d-matrix/){:target="_blank"}


    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

        Integers in each row are sorted from left to right.
        The first integer of each row is greater than the last integer of the previous row.

    Example 1:

    Input:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 3
    Output: true

    Example 2:

    Input:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 13
    Output: false



* Binary Search

```java
public boolean searchMatrix(int[][] matrix, int target) {
    if(matrix.length == 0 || matrix[0].length == 0) return false;
    int n = matrix.length, m = matrix[0].length;
    int l = 0, r = n * m - 1;
    while(l <= r) {
        int mid = l + (r-l) / 2;
        int i = mid / m, j = mid - i * m;
        if(matrix[i][j] == target)
            return true;
        else if(matrix[i][j] < target) {
            l = mid + 1;
        else
            r = mid - 1;
    }
    return false;
}
```
