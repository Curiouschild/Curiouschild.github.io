---
title:  "260. Single Number III"
date:   2019-05-02 18:26:00 +0930
categories: Leetcode
tags: Medium BitManiputlation
---

[{{page.title}}](https://leetcode.com/problems/single-number-iii/){:target="_blank"}

    Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

    Note:

    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Example 1:

    Input: [2,2,3,2]
    Output: 3

    Example 2:

    Input: [0,1,0,1,0,1,99]
    Output: 99

* Divide nums into two parts. Each of the two parts has one number.

```java
public int[] singleNumber(int[] nums) {
    int ab = 0;
    for(int n : nums) ab ^= n;
    int firstOnePosition = 0;
    while(((ab >> firstOnePosition) & 1) != 1) firstOnePosition++;
    int a = 0, b = 0;
    for(int n : nums) {
        if(((n >> firstOnePosition) & 1) == 1) a ^= n;
        else b ^= n;
    }
    return new int[] { a,b };
}
```
