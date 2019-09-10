---
title:  "279. Perfect Squares"
date:   2019-05-17 10:03:00 +0930
categories: Leetcode
tags: Medium Knapsack
---

[{{page.title}}](https://leetcode.com/problems/perfect-squares/){:target="_blank"}

    Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

    Example 1:

    Input: n = 12
    Output: 3
    Explanation: 12 = 4 + 4 + 4.

    Example 2:

    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.


```java

public int numSquares(int n) {
    int[] dp = new int[n+1];
    Arrays.fill(dp, n+1);
    dp[0] = 0;
    for(int c = 1; c * c <= n; c++) {
        for(int i = 1; i < dp.length; i++) {
            if(i-c*c >= 0)
                dp[i] = Math.min(dp[i], dp[i-c*c]+1);
        }
    }
    return dp[n];

}

public int numSquares2D(int n) {
    ArrayList<Integer> coins = new ArrayList<>();
    for(int i = 1; i * i <= n; i++) {
        coins.add(i * i);
    }
    int[][] dp = new int[coins.size()+1][n+1];
    for(int i = 0; i < dp.length; i++)
        Arrays.fill(dp[i], n+1);
    for(int i = 0; i < dp.length; i++)
        dp[i][0] = 0;
    for(int i = 1; i < dp.length; i++) {
        for(int j = 1; j < dp[0].length; j++) {
            dp[i][j] = Math.min(dp[i-1][j], j-coins.get(i-1) >= 0 ? (1 + dp[i][j-coins.get(i-1)]) : n+1);
        }
    }
    return dp[dp.length-1][dp[0].length-1];
}
```
