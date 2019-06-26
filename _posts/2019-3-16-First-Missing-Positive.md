---
title:  "41. First Missing Positive"
date:   2019-3-16 16:24:33 +0930
categories: Leetcode
tags:  Array
---

[{{page.title}}](https://leetcode.com/problems/first-missing-positive/){:target="_blank"}

    Given an unsorted integer array, find the smallest missing positive integer.

    Example 1:

    Input: [1,2,0]
    Output: 3

    Example 2:

    Input: [3,4,-1,1]
    Output: 2

    Example 3:

    Input: [7,8,9,11,12]
    Output: 1

Use indexs and nagetive value to store information.

```java
public int firstMissingPositive(int[] nums) {
    boolean hasOne = false;
    for(int i = 0; i < nums.length; i++) {
        if(nums[i] == 1) hasOne = true;
        if(nums[i] <= 0) nums[i] = 1;
    }
    if(!hasOne) return 1;
    for(int i = 0; i < nums.length; i++) {
        if(nums[i] <= nums.length) {
            int index = Math.abs(nums[i]) - 1; // negative value represents a existed number in the array
            if(nums[index] > 0) nums[index] = -nums[index];
        }
    }
    for(int i = 0; i < nums.length; i++) {
        if(nums[i] > 0) return i+1;
    }
    return nums.length+1;
  }
```
