---
title:  "53. Maximum Subarray"
date:   2019-3-6 012:22:21 +0930
categories: Leetcode
tags: Array
---

[{{page.title}}](https://leetcode.com/problems/maximum-subarray/){:target="_blank"}

    Given an integer array nums, find the contiguous subarray (containing 
    at least one number) which has the largest sum and return its sum.

1. DP brutal

```java
public int maxSubArrayBrutal(int[] nums) {
    int result = Integer.MIN_VALUE;
    for(int i = 0; i < nums.length; i++) {
        int sum = 0;
        for(int j = i; j < nums.length; j++) {
            sum += nums[j];
            result = Math.max(sum, result);
        }
    }
    return result;
}
```
2. One Pass

```java
public int maxSubArray(int[] nums) {
    int result = Integer.MIN_VALUE, sum = 0;
    for(int n : nums) {
        sum = sum + n < 0 ? 0 : sum + n; // reset sum when it becoming negative
        result = n < 0 ? Math.max(result, n) : Math.max(result, sum); // imaging an array with only negative elements
    }
    return result;
}
```
