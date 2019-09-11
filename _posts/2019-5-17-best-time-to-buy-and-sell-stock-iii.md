---
title:  "123. Best Time to Buy and Sell Stock III"
date:   2019-05-17 22:21:00 +0930
categories: Leetcode
tags: Hard DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/){:target="_blank"}

    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete at most two transactions.

    Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

    Example 1:

    Input: [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
                 Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

    Example 2:

    Input: [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                 Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
                 engaging multiple transactions at the same time. You must sell before buying again.


* All increasing continuous subarray

```java

public int maxProfit(int[] prices) {
    int k = 2;
    int[] buy = new int[k+1], sell = new int[k+1];
    Arrays.fill(buy, Integer.MIN_VALUE);
    for(int j = 0; j < prices.length; j++) {
        for(int t = 1; t <= 2; t++) {
            buy[t] = Math.max(buy[t], sell[t-1]-prices[j]);
            sell[t] = Math.max(sell[t], buy[t]+prices[j]);
        }
    }
    return sell[sell.length-1];
}
```
