---
title:  "518. Coin Change II"
date:   2019-3-8 16:30:13 +0930
categories: Leetcode
tags: Knapsack DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/coin-change-2/){:target="_blank"}


    You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

    Example 1:

    Input: amount = 5, coins = [1, 2, 5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1


* Bottom Up

https://leetcode.com/problems/coin-change-2/discuss/99212/

```java
public int change(int amount, int[] coins) {
    int[] dp = new int[amount + 1];
    dp[0] = 1;
    for(int c : coins) {
        for(int i = 1; i <= amount; i++) {
            if(c <= i) dp[i] += dp[i - c];
        }
    }
    return dp[amount];
}
```

* Memory Pad Top Down

```java
public int change2(int amount, int[] coins) {
    if(amount == 0) return 1;
    if(coins.length == 0) return 0;
    Integer[][] memo = new Integer[coins.length][amount+1];
    return dfs(0, coins, 0, amount, memo);
}

public int dfs(int index, int[] coins, int sum, int amount, Integer[][] memo) {
    if(sum > amount) return 0;
    if(sum == amount) return 1;
    if(memo[index][amount-sum] != null) {
        return memo[index][amount-sum];
    }
    int ans = 0;
    for(int i = index; i < coins.length; i++) {
        ans += dfs(i, coins, sum + coins[i], amount, memo);
    }
    memo[index][amount-sum] = ans;
    return ans;
}
```
