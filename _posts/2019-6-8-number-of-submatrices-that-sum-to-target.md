---
title:  "1074. Number of Submatrices That Sum to Target"
date:   2019-06-08 22:08:00 +0930
categories: Leetcode
tags: Hard Matrix
---

[{{page.title}}](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/){:target="_blank"}

    Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

    A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

    Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that
    is different: for example, if x1 != x1'.



    Example 1:

    Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
    Output: 4
    Explanation: The four 1x1 submatrices that only contain 0.

    Example 2:

    Input: matrix = [[1,-1],[-1,1]], target = 0
    Output: 5
    Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.



    Note:

      1 <= matrix.length <= 300
      1 <= matrix[0].length <= 300
      -1000 <= matrix[i] <= 1000
      -10^8 <= target <= 10^8


* N^3
  - dimesion compress to 1D
  - count with hashmap and prefix sum

```java

class Solution {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
        int[] arr = new int[matrix[0].length];
        int result = 0;
        for(int i = 0; i < matrix.length; i++) {
            arr = matrix[i].clone();
            result += count(arr, target);
            for(int j = i+1; j < matrix.length; j++) {
                for(int p = 0; p < matrix[0].length; p++) {
                    arr[p] += matrix[j][p];
                }
                result += count(arr, target);
            }
        }
        return result;
    }
    public int count(int[] arr, int k) {
        int result = 0, sum = 0;;
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        for(int i = 0; i < arr.length; i++) {
            sum += arr[i];
            int v = sum - k;
            if(map.containsKey(v)) {
                result += map.get(v);
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return result;
    }
}
```
