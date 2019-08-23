---
title:  "322. Coin Change"
date:   2019-3-8 15:21:11 +0930
categories: Leetcode
tags: Knapsack DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/coin-change/){:target="_blank"}


You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that
amount. If that amount of money cannot be made up by any combination of the coins, return -1.


* Bottom Up

i:coin j:amount
dp[i][j] = Math.min(dp[i-1][j], dp[i][j-coins[i]]+1)
--> reduce a dimension to
dp[j] = Math.min(dp[j] + dp[j-coins[i]]+1)

```java
public int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount+1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;
    for(int i = 0; i < amount + 1; i++) {
        for(int c : coins) {
            if(c <= i) {
                dp[i] = Math.min(dp[i], dp[i-c] + 1);
            }
        }
    }
    return dp[amount] == amount + 1 ? -1 : dp[amount];
}
```

* Memory Pad Top Down

```java
public int coinChange(int[] coins, int amount) {
    int result = recursive(coins, new HashMap<Integer, Integer>(), amount);
    return result;
}
public int recursive(int[] coins, HashMap<Integer, Integer> dp, int remain) {
    if(remain < 0) return -1;
    if(remain == 0) return 0;
    if(dp.containsKey(remain)) return dp.get(remain);
    int result = Integer.MAX_VALUE;
    for(int coin : coins) {
        int min = recursive(coins, dp, remain - coin);
        if(min >= 0) result = Math.min(result, min + 1); // valid change
    }
    if(result == Integer.MAX_VALUE) result = -1; // no valid change
    dp.put(remain, result);
    return result;
}
```
