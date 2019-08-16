---
title:  "48. Rotate Image"
date:   2019-4-22 10:40:00 +0930
categories: Leetcode
tags: Matrix Medium
---

[{{page.title}}](https://leetcode.com/problems/rotate-image/){:target="_blank"}

    You are given an n x n 2D matrix representing an image.

    Rotate the image by 90 degrees (clockwise).

    Note:

    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

    Example 1:

    Given input matrix =
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ],

    rotate the input matrix in-place such that it becomes:
    [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]

    Example 2:

    Given input matrix =
    [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ],

    rotate the input matrix in-place such that it becomes:
    [
      [15,13, 2, 5],
      [14, 3, 4, 1],
      [12, 6, 8, 9],
      [16, 7,10,11]
    ]


* O(1) Space

```java

public void rotate(int[][] matrix) {
    int offset = 0;
    while(true) {
        if(matrix.length - offset * 2 <= 1) break;
        int far = matrix.length - 1 - offset;
        for(int j = offset; j < far; j++) {
            int temp = matrix[offset][j];
            matrix[offset][j] = matrix[far-(j-offset)][offset];
            matrix[far-(j-offset)][offset] = matrix[far][far-(j-offset)];
            matrix[far][far-(j-offset)] = matrix[j][far];
            matrix[j][far] = temp;
        }
        offset++;
    }
}
```


* Buffer array

```java

public void rotate(int[][] matrix) {
    int offset = 0;
    while(true) {
        if(matrix.length - offset * 2 <= 1) break;
        int[] buffer = new int[matrix.length - offset * 2 - 1];
        System.arraycopy(matrix[offset], offset, buffer, 0, buffer.length);
        System.out.println(Arrays.toString(buffer));
        int far = offset + buffer.length;
        for(int k = offset; k < far; k++) matrix[offset][k] = matrix[far-(k-offset)][offset];
        for(int k = offset; k < far; k++) matrix[far-(k-offset)][offset] = matrix[far][far-(k-offset)];
        for(int k = offset; k < far; k++) matrix[far][far-(k-offset)] = matrix[k][far];
        for(int k = offset; k < far; k++) matrix[k][far] = buffer[k-offset];
        offset++;
    }
}
```
