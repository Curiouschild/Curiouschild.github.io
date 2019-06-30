---
title:  "85. Maximal Rectangle"
date:   2019-3-19 19:27:00 +0930
categories: Leetcode
tags: MonotonicStack
---

[{{page.title}}](https://leetcode.com/problems/maximal-rectangle/){:target="_blank"}

    Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing
    only 1's and return its area.

    Example:

    Input:
    [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    Output: 6


* MonotonicStack

```java
public int maximalRectangle(char[][] matrix) {
    if(matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;
    int[] h = new int[matrix[0].length+1];
    int result = 0;
    for(int i = 0; i < matrix.length; i++) {
        if(i == 0) {
            for(int j = 0; j < matrix[0].length; j++)
                h[j] = matrix[i][j] == '1' ? 1 : 0;
        } else {
            for(int j = 0; j < matrix[0].length; j++)
                h[j] = matrix[i][j] == '1' ? h[j] + 1 : 0;
        }
        result = Math.max(result, largestRectangleArea(h));
    }
    return result;
}

public int largestRectangleArea(int[] h) {
    ArrayDeque<Integer> stack = new ArrayDeque<>();
    stack.push(-1);
    int result = 0;
    for(int i = 0; i < h.length; i++) {
        while(stack.peek() != -1 && h[stack.peek()] > h[i]) {
            int height = h[stack.pop()];
            result = Math.max(result, height * (i - 1 - stack.peek()));
        }
        stack.push(i);
    }
    return result;
}
```

* DP row by row, N^2 * M

```java
public int maximalRectangleAccumulateRows(char[][] matrix) {
    if(matrix.length == 0 || matrix[0].length == 0) return 0;
    int result = Integer.MIN_VALUE;
    int[] temp = new int[matrix[0].length];
    for(int i = 0; i < matrix.length; i++) {
        for(int j = i; j < matrix.length; j++) {
            if(j == i) {
                for(int k = 0; k < temp.length; k++) temp[k] = matrix[j][k] - '0';
            }
            else {
                for(int k = 0; k < matrix[0].length; k++) {
                    if(matrix[j][k] == '1' && temp[k] > 0) temp[k] += 1;
                    else temp[k] = 0;
                }
            }
            int sum = 0;
            for(int k = 0; k < temp.length; k++) {
                if(k == 0 || temp[k] != temp[k-1]) sum = temp[k];
                else sum += temp[k];
                result = Math.max(sum, result);
            }
        }
    }
    return result;
}
```

or

```java

public int maximalRectangleReduceDimension(char[][] matrix) {
    if(matrix==null || matrix.length == 0 || matrix[0] == null || matrix[0].length==0) return 0;
    int n = matrix.length, m = matrix[0].length;
    int ans = 0;
    char[] buffer = new char[m];
    Arrays.fill(buffer, '1');
    for(int i = 0; i < n; i++) {
        for(int j = i; j < n; j++) {
            int cols = 0;
            for(int k = 0; k < m; k++) {
                buffer[k] = buffer[k] == '1' && matrix[j][k] == '1' ? '1' : '0';
            }
            for(int k = 0; k < m; k++) {
                if(buffer[k] == '0') {
                    cols = 0;
                } else {
                    cols++;
                }
                ans = Math.max(ans, (j-i+1)*cols);
            }
        }
        Arrays.fill(buffer,'1');
    }
    return ans;
}
```
