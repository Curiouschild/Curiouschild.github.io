---
title:  "54. Spiral Matrix"
date:   2019-3-11 15:29:21 +0930
categories: Leetcode
tags: Matrix
---

[{{page.title}}](https://leetcode.com/problems/spiral-matrix/){:target="_blank"}

    Given a matrix of m x n elements (m rows, n columns), return all elements of
    the matrix in spiral order.

    Example 1:

    Input:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]


```java
public List<Integer> spiralOrder(int[][] matrix) {
    if(matrix.length == 0) return new ArrayList<>();
    int[] dirs = {1, 2, 3, 0};
    int d = 0;
    int[] is = {0, 1, 0, -1};
    int[] js = {1, 0, -1, 0};
    int top = 0, bottom = matrix.length - 1, left = 0, right = matrix[0].length - 1;
    int i = 0, j = 0;
    List<Integer> result = new ArrayList<>();
    while(top <= i && i <= bottom && left <= j && j <= right) {
        result.add(matrix[i][j]);
        int ni = i + is[d], nj = j + js[d];
        if(top <= ni && ni <= bottom && left <= nj && nj <= right) {
            i = ni;
            j = nj;
        } else {
            d = dirs[d];
            ni = i + is[d];
            nj = j + js[d];
            if(d == 1) top++;
            if(d == 2) right--;
            if(d == 3) bottom--;
            if(d == 0) left++;
            if(top <= ni && ni <= bottom && left <= nj && nj <= right) {
                i = ni;
                j = nj;
            } else {
                break;
            }
        }
    }
    return result;
}
```
