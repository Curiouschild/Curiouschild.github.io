---
title:  "238. Product of Array Except Self"
date:   2019-3-7 10:19:31 +0930
categories: Leetcode
tags: Array
---

[{{page.title}}](https://leetcode.com/problems/product-of-array-except-self/){:target="_blank"}

    Given an array nums of n integers where n > 1,  return an array output
    such that output[i] is equal to the product of all the elements of nums except nums[i].

    Example:

    Input:  [1,2,3,4]
    Output: [24,12,8,6]


* Two Pass

```java
public int[] productExceptSelf(int[] nums) {
    int[] result = new int[nums.length];
    int product = 1;
    for(int i = 0; i < nums.length; i++) {
        result[i] = product;
        product *= nums[i];
    }
    product = 1;
    for(int i = nums.length-1; i >= 0; i--) {
        result[i] *= product;
        product *= nums[i];
    }
    return result;
}
```

* Two Pass More Space

```java
public int[] productExceptSelfBad(int[] nums) {
    if(nums.length == 0) return new int[0];
    int[] left = new int[nums.length], right = new int[nums.length];
    left[0] = 1;
    right[nums.length-1] = 1;
    for(int i = 1; i < nums.length; i++) left[i] = left[i-1] * nums[i-1];
    for(int i = nums.length-2; i >= 0; i--) right[i] = right[i+1] * nums[i+1];
    int[] result = new int[nums.length];
    for(int i = 0; i < result.length; i++) result[i] = left[i] * right[i];
    return result;
}
```
