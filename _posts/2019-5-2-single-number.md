---
title:  "136. Single Number"
date:   2019-05-02 14:38:00 +0930
categories: Leetcode
tags: Easy BitManiputlation
---

[{{page.title}}](https://leetcode.com/problems/single-number/){:target="_blank"}

    Given a non-empty array of integers, every element appears twice except for one. Find that single one.

    Note:

    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Example 1:

    Input: [2,2,1]
    Output: 1

    Example 2:

    Input: [4,1,2,1,2]
    Output: 4

* xor

```java
public int singleNumber(int[] nums) {
    int result = nums[0];
    for(int i = 1; i < nums.length; i++) result ^= nums[i];
    return result;
}
```
