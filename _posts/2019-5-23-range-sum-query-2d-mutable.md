---
title:  "308. Range Sum Query 2D - Mutable"
date:   2019-05-23 19:06:00 +0930
categories: Leetcode
tags: Hard SegmentTree
---

[{{page.title}}](https://leetcode.com/problems/range-sum-query-mutable/){:target="_blank"}

    Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left
    corner (row1, col1) and lower right corner (row2, col2).

    Range Sum Query 2D
    The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3),
    which contains sum = 8.

    Example:

    Given matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]

    sumRegion(2, 1, 4, 3) -> 8
    update(3, 2, 2)
    sumRegion(2, 1, 4, 3) -> 10


* Segment Tree

```java
class NumMatrix {
    int[] arr;
    int[][] matrix;
    public NumMatrix(int[][] matrix) {
        if(!(matrix == null || matrix.length == 0)) {
            this.matrix = matrix;
            int n = matrix.length * matrix[0].length;
            int h = (int)Math.ceil(Math.log(n)/Math.log(2));
            int len = (int)Math.pow(2, h+1)-1;
            arr = new int[len];
            build(0, n-1, 0);
        }
    }

    public int build(int start, int end, int index) {
        if(start == end) {
            arr[index] = getValue(start);
        } else {
            int mid = start + (end-start) / 2;
            arr[index] = build(start, mid, index * 2 + 1)
                        + build(mid+1, end, index * 2 + 2);
        }
        return arr[index];
    }

    public int getValue(int n) {
        int i = n / matrix[0].length;
        int j = n % matrix[0].length;
        return matrix[i][j];
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        if(arr == null) return 0;
        int result = 0;
        for(int i = row1; i <= row2; i++) {
            int start = i * matrix[0].length + col1;
            int end = start + (col2-col1);
            result += query(start, end, 0, matrix.length*matrix[0].length-1, 0);
        }
        return result;
    }

    public void update(int row, int col, int val) {
        if(arr == null) return;
        int diff = val - matrix[row][col];
        matrix[row][col] = val;
        update(row * matrix[0].length+col, diff, 0, matrix.length*matrix[0].length-1, 0);
    }

    public void update(int target, int diff, int start, int end, int index) {
        arr[index] += diff;
        if(start == end) return;
        int mid = start + (end-start) / 2;
        if(target <= mid) update(target, diff, start, mid, 2*index+1);
        else update(target, diff, mid+1, end, 2*index+2);
    }

    public int query(int i, int j, int start, int end, int index) {
        if(i <= start && j >= end) return arr[index];
        if(i > end || j < start) return 0;
        int mid = start + (end-start) / 2;
        return query(i, j, start, mid, 2 * index + 1)
            + query(i, j, mid+1, end, 2 * index + 2);
    }


}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * obj.update(row,col,val);
 * int param_2 = obj.sumRegion(row1,col1,row2,col2);
 */
```
