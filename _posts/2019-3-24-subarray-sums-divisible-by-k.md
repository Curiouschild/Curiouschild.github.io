---
title:  "974. Subarray Sums Divisible by K"
date:   2019-3-24 13:51:00 +0930
categories: Leetcode
tags: Array HashMap Math
---

[{{page.title}}](https://leetcode.com/problems/subarray-sums-divisible-by-k/){:target="_blank"}

    Given an array A of integers, return the number of (contiguous, non-empty) subarrays
    that have a sum divisible by K.



    Example 1:

    Input: A = [4,5,0,-2,-3,1], K = 5
    Output: 7
    Explanation: There are 7 subarrays with a sum divisible by K = 5:
    [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

* HashMap

```java

public int subarraysDivByK(int[] A, int K) {
    int result = 0, sum = 0;
    HashMap<Integer, Integer> map = new HashMap<>();
    map.put(0, 1);
    for(int i : A) {
        sum += i;
        int residual = (sum % K + K) % K;
        int preCnt = map.getOrDefault(residual, 0);
        result += preCnt;
        map.put(residual, preCnt + 1);
    }
    return result;
}
```
