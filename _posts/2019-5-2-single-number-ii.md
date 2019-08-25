---
title:  "137. Single Number II"
date:   2019-05-02 17:56:00 +0930
categories: Leetcode
tags: Medium BitManiputlation
---

[{{page.title}}](https://leetcode.com/problems/single-number-ii/){:target="_blank"}

    Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

    Note:

    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Example 1:

    Input: [2,2,3,2]
    Output: 3

    Example 2:

    Input: [0,1,0,1,0,1,99]
    Output: 99



* 00, 10, 11 represents three states
  zero or three, one, two

```java
public int singleNumber(int[] nums) {
    int once = 0, twice = 0;
    for(int i : nums) {
        once = ~twice & (once ^ i);
        twice = ~once & (twice ^ i);
    }
    return once;
}
```

* A more understandable version
Count the 1s at very bits for all the numbers, and module the repeated times

```java
public int singleNumber(int[] nums) {
    int[] bits = new int[32];
    for(int n : nums) {
        for(int i = 0; i < 32; i++)
            bits[31-i] += (n >> i) & 1;
    }
    int ans = 0;
    for(int i = 0; i < 32; i++) {
        if(bits[i] % 3 == 1)
            ans |= (1 << (31-i));
    }
    return ans;
}
```
