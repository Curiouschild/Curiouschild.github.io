---
title:  "73. Set Matrix Zeroes"
date:   2019-05-21 20:02:00 +0930
categories: Leetcode
tags: Easy Array
---

[{{page.title}}](https://leetcode.com/problems/set-matrix-zeroes/){:target="_blank"}

    Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

    Example 1:

    Input:
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    Output:
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]

    Example 2:

    Input:
    [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    Output:
    [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]

    Follow up:

        A straight forward solution using O(mn) space is probably a bad idea.
        A simple improvement uses O(m + n) space, but still not the best solution.
        Could you devise a constant space solution?



* in place use first col and row as zero indicators

```java

public void setZeroes(int[][] matrix) {
    int n = matrix.length, m = matrix[0].length;
    boolean col = false, row = false; // true is there is a zero on first col or row
    for(int i = 0; i < n; i++) if(matrix[i][0] == 0) col = true;
    for(int j = 0; j < m; j++) if(matrix[0][j] == 0) row = true;

    for(int i = 1; i < n; i++) {
        for(int j = 1; j < m; j++) {
            if(matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    for(int i = 1; i < n; i++) {
        for(int j = 1; j < m; j++) {
            if(matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }
    for(int i = 1; i < n; i++) {
        for(int j = 1; j < m; j++) {
            if(matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }
    if(row) Arrays.fill(matrix[0], 0);
    if(col) for(int i = 0; i < n; i++) matrix[i][0] = 0;
}

```

* In place with dummy value represents transformed zero

```java
public int thirdMaxQ(int[] nums) {
    PriorityQueue<Integer> q = new PriorityQueue<>();
    HashSet<Integer> set = new HashSet<>();
    for(int i : nums) set.add(i);
    for(int i : set) {
        if(q.size() < 3) q.offer(i);
        else if(q.peek() < i) {
            q.poll();
            q.offer(i);
        }
    }
    if(q.size() == 2) q.poll();
    return q.peek();
}
```

* Intuitive

```java
public void setZeroes(int[][] matrix) {
    HashSet<Integer> set = new HashSet<>();
    for(int[] arr : matrix) {
        for(int i : arr) set.add(i);
    }
    int n = 0;
    while(true) {
        if(set.contains(n)) n++;
        else break;
    }
    for(int i = 0; i < matrix.length; i++) {
        for(int j = 0; j < matrix[0].length; j++) {
            if(matrix[i][j] == 0) {
                for(int k = 0; k < matrix[0].length; k++) {
                    if(matrix[i][k] != 0) matrix[i][k] = n;
                }
                for(int k = 0; k < matrix.length; k++)
                    if(matrix[k][j] != 0) matrix[k][j] = n;
            }
        }
    }
    for(int i = 0; i < matrix.length; i++) {
        for(int j = 0; j < matrix[0].length; j++) {
            if(matrix[i][j] == n) matrix[i][j] = 0;
        }
    }

}
```
