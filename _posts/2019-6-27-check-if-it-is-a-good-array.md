---
title:  "1250. Check If It Is a Good Array"
date:   2019-06-27 21:45:00 +0930
categories: Leetcode
tags: Hard Math
---

[{{page.title}}](https://leetcode.com/problems/check-if-it-is-a-good-array/){:target="_blank"}

    Given an array nums of positive integers. Your task is to select some subset of nums, multiply each element by an
    integer and add all these numbers. The array is said to be good if you can obtain a sum of 1 from the array by any
    possible subset and multiplicand.

    Return True if the array is good otherwise return False.

    Example 1:

    Input: nums = [12,5,7,23]
    Output: true
    Explanation: Pick numbers 5 and 7.
    5*3 + 7*(-2) = 1

    Example 2:

    Input: nums = [29,6,10]
    Output: true
    Explanation: Pick numbers 29, 6 and 10.
    29*1 + 6*(-3) + 10*(-1) = 1

    Example 3:

    Input: nums = [3,6]
    Output: false

    Constraints:

        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^9



* Math
  - https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity
  - pure math

```java

public boolean isGoodArray(int[] nums) {
    int result = nums[0];
    for(int i = 1; i < nums.length; i++) {
        result = gcd(result, nums[i]);
    }
    return result == 1;
}

public int gcd(int a, int b) {
    if(b == 0) return a;
    return gcd(b, a % b);
}
```
