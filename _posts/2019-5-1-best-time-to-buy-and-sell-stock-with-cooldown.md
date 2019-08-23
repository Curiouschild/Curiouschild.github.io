---
title:  "309. Best Time to Buy and Sell Stock with Cooldown"
date:   2019-05-01 10:22:00 +0930
categories: Leetcode
tags: Medium DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/squares-of-a-sorted-array/){:target="_blank"}

    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

        You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
        After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

    Example:

    Input: [1,2,3,0,2]
    Output: 3
    Explanation: transactions = [buy, sell, cooldown, buy, sell]


* DP

buy[i] : Maximum profit which end with buying on day i or end
with buying on a day before i and takes rest until the day i since then.

sell[i] : Maximum profit which end with selling on day i or end
with selling on a day before i and takes rest until the day i since then.

```java
public int maxProfit(int[] p) {
    if(p.length == 0) return 0;
    int[] sell = new int[p.length], buy = new int[p.length];
    buy[0] = -p[0];
    for(int i = 1; i < p.length; i++) {
        sell[i] = Math.max(sell[i-1], buy[i-1]+p[i]);
        buy[i] = Math.max(buy[i-1], (i-2 >= 0 ? sell[i-2] : 0)-p[i]);
    }
    return sell[sell.length-1];
}
```

* Space Optimized

```java
public int maxProfit(int[] prices) {
    if(prices.length == 0) return 0;
    int s = 0, s1 = 0, s2 = 0, b = 0, b1 = -prices[0];
    for(int p : prices) {
        s = Math.max(s1, b1 + p);
        b = Math.max(b1, s2 - p);
        s2 = s1;
        s1 = s;
        b1 = b;
    }
    return s;
}
```
