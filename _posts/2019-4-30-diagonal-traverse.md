---
title:  "498. Diagonal Traverse"
date:   2019-4-30 16:27:00 +0930
categories: Leetcode
tags: Medium Math Matrix
---

[{{page.title}}](https://leetcode.com/problems/diagonal-traverse/){:target="_blank"}

    Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order
    as shown in the below image.


    Example:

    Input:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]

    Output:  [1,2,4,7,5,3,6,8,9]

    Explanation:


![img1](/img/posts/diagonal-traverse-1.png)


    Note:

    The total number of elements of the given matrix will not exceed 10,000.


* Linear function

```java
public int[] findDiagonalOrder(int[][] matrix) {
     if(matrix == null || matrix.length == 0 || matrix[0] == null || matrix[0].length == 0) return new int[0];
     int n = matrix.length, m = matrix[0].length;
     int[] result = new int[n*m];
     int index = 0;
     boolean up = true;
     for(int k = 0; k < m+n-1; k++) {
         if(up) {
             int startJ = k - n + 1 < 0 ? 0 : k - n + 1;
             for(int j = startJ; j < m; j++) {
                 int i = k-j;
                 if(i < 0 || i >= n) break;
                 result[index++] = matrix[i][j];
             }
         } else {
             int startJ = k <= m-1 ? k : m-1;
             for(int j = startJ; j >= 0; j--) {
                 int i = k-j;
                 if(i < 0 || i >= n) continue;
                 result[index++] = matrix[i][j];
             }
         }
         up ^= true;
     }
     return result;
 }
```
