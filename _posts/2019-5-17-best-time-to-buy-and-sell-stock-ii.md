---
title:  "122. Best Time to Buy and Sell Stock II"
date:   2019-05-17 12:40:00 +0930
categories: Leetcode
tags: Easy Array
---

[{{page.title}}](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/){:target="_blank"}

    You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols +
    and -. For each integer, you should choose one from + and - as its new symbol.

    Find out how many ways to assign symbols to make sum of integers equal to target S.

    Example 1:

    Input: nums is [1, 1, 1, 1, 1], S is 3.
    Output: 5
    Explanation:

    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3

    There are 5 ways to assign symbols to make the sum of nums be target 3.

    Note:

        The length of the given array is positive and will not exceed 20.
        The sum of elements in the given array will not exceed 1000.
        Your output answer is guaranteed to be fitted in a 32-bit integer.

* All increasing continuous subarray

```java

public int maxProfit(int[] prices) {
    int result = 0;
    int sum = 0;
    int l = 0, r = 1;
    while(r < prices.length) {
        while(r < prices.length && prices[r] >= prices[r-1]) r++;
        if(r-1 > l) {
            result += prices[r-1] - prices[l];
        }
        l = r;
        r++;
    }
    return result;
}
```
