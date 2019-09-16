---
title:  "377. Combination Sum IV"
date:   2019-05-13 09:54:00 +0930
categories: Leetcode
tags: Medium Backtrack
---

[{{page.title}}](https://leetcode.com/problems/combination-sum-iv/){:target="_blank"}

    Given an integer array with all positive numbers and no duplicates, find the number of possible
    combinations that add up to a positive integer target.

    Example:

    nums = [1, 2, 3]
    target = 4

    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)

    Note that different sequences are counted as different combinations.

    Therefore the output is 7.

    Follow up:
    What if negative numbers are allowed in the given array?
    How does it change the problem?
    What limitation we need to add to the question to allow negative numbers?
    1. either positive number or negative number should be used only one time
    2. the maximum length of result set is given


```java

public int combinationSum4(int[] candidates, int target) {
    int[] dp = new int[target+1];
    dp[0] = 1;
    for(int i = 1; i < dp.length; i++) {
        for(int j : candidates) {
            if(i-j >= 0) {
                dp[i] += dp[i-j];
            }
        }
    }
    return dp[target];
}
```
