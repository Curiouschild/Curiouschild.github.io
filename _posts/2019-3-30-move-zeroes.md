---
title:  "283. Move Zeroes"
date:   2019-3-30 22:50:00 +0930
categories: Leetcode
tags: TwoPointers
---

[{{page.title}}](https://leetcode.com/problems/move-zeroes/){:target="_blank"}

    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Example:

    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

    Note:

        You must do this in-place without making a copy of the array.
        Minimize the total number of operations.



```java
public void moveZeroes(int[] nums) {
    int l = 0, r = 0;
    // l -> left most 0
    // r -> the first none 0 starting from l
    while(r < nums.length) {
        while(l < nums.length && nums[l] != 0) l++;
        r = l;
        while(r < nums.length && nums[r] == 0) r++;
        if(r < nums.length) swap(nums, l, r);
    }
}
```
