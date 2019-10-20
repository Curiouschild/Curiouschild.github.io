---
title:  "1230. Toss Strange Coins"
date:   2019-06-21 21:08:00 +0930
categories: Leetcode
tags: Medium DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/toss-strange-coins/){:target="_blank"}

    You have some coins.  The i-th coin has a probability prob[i] of facing heads when tossed.
    Return the probability that the number of coins facing heads equals target if you toss every coin exactly
    once.

    Example 1:

    Input: prob = [0.4], target = 1
    Output: 0.40000

    Example 2:

    Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
    Output: 0.03125

    Constraints:

        1 <= prob.length <= 1000
        0 <= prob[i] <= 1
        0 <= target <= prob.length
        Answers will be accepted as correct if they are within 10^-5 of the correct answer.

* DP
  - dp[i][j]: j coins heads up in the first i coins


```java

public double probabilityOfHeads(double[] prob, int target) {
    double[][] dp = new double[prob.length+1][target+1];
    dp[0][0] = 1.0;
    for(int i = 1; i < dp.length; i++) {
        for(int j = 0; j <= Math.min(target, i); j++) {
            dp[i][j] = (j == 0 ? 0 : dp[i-1][j-1]) * prob[i-1] + dp[i-1][j] * (1-prob[i-1]);
        }
    }
    return dp[dp.length-1][dp[0].length-1];
}
```
