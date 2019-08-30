---
title:  "410. Split Array Largest Sum"
date:   2019-05-07 14:32:00 +0930
categories: Leetcode
tags: Hard DynamicProgramming BinarySearch
---

[{{page.title}}](https://leetcode.com/problems/split-array-largest-sum/){:target="_blank"}

    Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

    Note:
    If n is the length of array, assume the following constraints are satisfied:

        1 ≤ n ≤ 1000
        1 ≤ m ≤ min(50, n)

    Examples:

    Input:
    nums = [7,2,5,10,8]
    m = 2

    Output:
    18

    Explanation:
    There are four ways to split nums into two subarrays.
    The best way is to split it into [7,2,5] and [10,8],
    where the largest sum among the two subarrays is only 18.

* Binary Search
canSplit(array, m, x):
  true if the array can be splited into m parts with the largest subarray sum is less than or equal to x
if(canSplit(x)) is true, then canSplit(y) that y > x is true, so the answer space is like

...F F F F F T(the answer) T T T T...

This is a typical binary search problem.

```java
public int splitArray(int[] nums, int m) {
    long l = Integer.MAX_VALUE, r = 0;
    for(int n : nums) {
        r += n;
        l = Math.min(l, n);
    }
    while(l < r) {
        long mid = l + (r-l) / 2;
        if(canSplit(nums, m, mid)) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    return (int)r;
}
```

* DynamicProgramming
dp[i][j]: the min max subarray sum form 0 to j, divided into i parts

```java
public int splitArray(int[] nums, int m) {
    int[] prefix = new int[nums.length];
    prefix[0] = nums[0];
    for(int i = 1; i < prefix.length; i++)
        prefix[i] = prefix[i-1]+nums[i];

    int[][] dp = new int[m+1][nums.length];
    for(int i = 0; i < dp.length; i++) {
        Arrays.fill(dp[i], Integer.MAX_VALUE);
    }
    for(int j = 0; j < dp[0].length; j++)
        dp[1][j] = prefix[j];
    for(int i = 2; i < dp.length; i++) {
        for(int j = i-1; j < nums.length; j++) {
            for(int k = 0; k < j; k++) {
                dp[i][j] = Math.min(dp[i][j], Math.max(dp[i-1][k], (prefix[j]-prefix[k])));
            }
        }
    }
    return dp[m][nums.length-1];
}
```
