---
title:  "123. Best Time to Buy and Sell Stock IV"
date:   2019-05-17 22:45:00 +0930
categories: Leetcode
tags: Hard DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/){:target="_blank"}

    Say you have an array for which the i-th element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete at most k transactions.

    Note:
    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy
    again).

    Example 1:

    Input: [2,4,1], k = 2
    Output: 2
    Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

    Example 2:

    Input: [3,2,6,5,0,3], k = 2
    Output: 7
    Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
                 Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


```java

public int maxProfit(int K, int[] prices) {
    if(K > prices.length / 2) {
        return greedy(prices);
    }
   int[] buy = new int[K+1], sell = new int[K+1];
    Arrays.fill(buy, Integer.MIN_VALUE);
    for(int i = 0; i < prices.length; i++) {
        for(int j = 1; j <= K; j++) {
            buy[j] = Math.max(buy[j], sell[j-1]-prices[i]);
            sell[j] = Math.max(sell[j], buy[j]+prices[i]);
        }
    }
    return sell[K];
}
public int greedy(int[] prices) {
    int result = 0;
    for(int i = 1; i < prices.length; i++) {
        if(prices[i]-prices[i-1] > 0) {
            result += prices[i]-prices[i-1];
        }
    }
    return result;
}
```
