---
title:  "363. Max Sum of Rectangle No Larger Than K"
date:   2019-06-08 22:05:00 +0930
categories: Leetcode
tags: Hard Matrix
---

[{{page.title}}](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/){:target="_blank"}

    Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such
    that its sum is no larger than k.

    Example:

    Input: matrix = [[1,0,1],[0,-2,3]], k = 2
    Output: 2 
    Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
                 and 2 is the max number no larger than k (k = 2).

    Note:

        The rectangle inside the matrix must have an area > 0.
        What if the number of rows is much larger than the number of columns?


* N^3 * log(N)

```java

public int maxSumSubmatrix(int[][] matrix, int k) {
    int[] arr = new int[matrix[0].length];
    int result = Integer.MIN_VALUE;
    for(int i = 0; i < matrix.length; i++) {
        arr = matrix[i].clone();
        int temp = count(arr, k);
        for(int j = i+1; j < matrix.length; j++) {
            for(int p = 0; p < matrix[0].length; p++) {
                arr[p] += matrix[j][p];
            }
            temp = Math.max(temp, count(arr, k));
        }
        result = Math.max(result, temp);
    }
    return result;
}
public int count(int[] arr, int k) {
    int result = Integer.MIN_VALUE, sum = 0;;
    TreeSet<Integer> set = new TreeSet<>();
    set.add(0);
    for(int i = 0; i < arr.length; i++) {
        sum += arr[i];
        int v = sum - k;
        Integer candidate = set.ceiling(v);
        if(candidate != null)
            result = Math.max(result, sum - candidate);
        set.add(sum);
    }
    return result;
}
```
