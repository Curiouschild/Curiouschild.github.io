---
title:  "121. Best Time to Buy and Sell Stock"
date:   2019-3-7 09:54:31 +0930
categories: Leetcode
tags: Array DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/){:target="_blank"}

    Say you have an array for which the ith element is the price of a given stock on day i.

    If you were only permitted to complete at most one transaction (i.e., buy one and
    sell one share of the stock), design an algorithm to find the maximum profit.

    Note that you cannot sell a stock before you buy one.


```java
public int maxProfit(int[] prices) {
    if(prices.length == 0) return 0;
    int[] profits = new int[prices.length-1];
    for(int i = 0; i < profits.length; i++)
        profits[i] = prices[i+1] - prices[i];
    int sum = 0, max = Integer.MIN_VALUE;
    for(int profit : profits) {
        // sum = sum + profit < 0 ? 0 : sum + profit;
        // max = profit < 0 ? Math.max(profit, max) : Math.max(sum, max);
        if(sum < 0) {
            sum = profit;
        } else {
            sum += profit;
        }
        max = Math.max(max, sum);
    }
    return max < 0 ? 0 : max;
}
```
