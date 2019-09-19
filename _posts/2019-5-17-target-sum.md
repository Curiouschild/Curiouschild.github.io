---
title:  "494. Target Sum"
date:   2019-05-17 12:03:00 +0930
categories: Leetcode
tags: Medium Knapsack
---

[{{page.title}}](https://leetcode.com/problems/target-sum/){:target="_blank"}

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

* Recursion with memo

```java
public int findTargetSumWays(int[] nums, int S) {
    return dp(nums, nums.length-1, Integer.valueOf(S), new HashMap<String, Integer>());
}

public int dp(int[] nums, int i, int t, HashMap<String, Integer> map) {
    if(i == -1) return t == 0 ? 1 : 0;
    String k = "" + t + "," + i;
    if(map.containsKey(k)) return map.get(k);
    int cnt = dp(nums, i-1, t-nums[i], map)
            + dp(nums, i-1, t+nums[i], map);
    map.put(k, cnt);
    return cnt;
}
```




* Bottom Up

dp[i] relies only on dp[i-1]; init dp[0][sum] = 1 (here sum is the offset + zero)
the actual range of the sum (index j) is -sum ~ sum, plus offset sum --> 0 ~ 2*sum

```java

class Solution {
    public int findTargetSumWaysMN(int[] nums, int S) {
        int sum = 0;
        for(int i : nums) sum += i; // sum is the offset
        if(S > sum) return 0;
        int[][] dp = new int[nums.length+1][sum * 2 + 1];
        dp[0][sum] = 1;
        for(int i = 1; i < dp.length; i++) {
            for(int j = 0; j < dp[0].length; j++) {
                if(j+nums[i-1] < dp[0].length)
                    dp[i][j] += dp[i-1][j+nums[i-1]];
                if(j-nums[i-1] >= 0)
                    dp[i][j] += dp[i-1][j-nums[i-1]];
            }
        }
        // 0 -- -sum
        // x  -- S
        return dp[dp.length-1][S + sum];
    }

  public int findTargetSumWaysM(int[] nums, int S) {
        int sum = 0;
        for(int i : nums) sum += i; // sum is the offset
        if(S > sum) return 0;
        int[][] dp = new int[2][sum * 2 + 1];
        dp[0][sum] = 1;

        for(int n : nums) {
            for(int j = 0; j < dp[0].length; j++) {
                if(j+n < dp[0].length)
                    dp[1][j] += dp[0][j+n];
                if(j-n >= 0)
                    dp[1][j] += dp[0][j-n];
            }
            dp[0] = dp[1];
            dp[1] = new int[dp[1].length];
        }
        // 0 -- -sum
        // x  -- S
        return dp[0][S + sum];
    }
}
```
