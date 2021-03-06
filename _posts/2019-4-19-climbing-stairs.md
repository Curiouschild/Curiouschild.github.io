---
title:  "70. Climbing Stairs (509	Fibonacci Number)"
date:   2019-4-19 21:40:00 +0930
categories: Leetcode
tags: DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/climbing-stairs/){:target="_blank"}

    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Note: Given n will be a positive integer.

    Example 1:

    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    Example 2:

    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step



* Simple DP

```java
public int climbStairs(int n) {
    if(n <= 1) return n;
    int x = 1, y = 2;
    for(int i = 2; i < n; i++) {
        int z = x + y;
        x = y;
        y = z;
    }
    return y;
}
```
