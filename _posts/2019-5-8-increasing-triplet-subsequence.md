---
title:  "334. Increasing Triplet Subsequence"
date:   2019-05-07 23:20:00 +0930
categories: Leetcode
tags: Medium DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/increasing-triplet-subsequence/){:target="_blank"}

    Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

    Formally the function should:

        Return true if there exists i, j, k
        such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

    Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

    Example 1:

    Input: [1,2,3,4,5]
    Output: true

    Example 2:

    Input: [5,4,3,2,1]
    Output: false



* Longest Increasing subsequent

```java
public boolean increasingTriplet(int[] nums) {
    if(nums.length == 0) return false;
    int[] dp = new int[3];
    int len = 1;
    dp[0] = nums[0];
    for(int i = 1; i < nums.length; i++) {
        int j = 0;
        for(; j < len; j++) {
            if(nums[i] <= dp[j]) {
                dp[j] = nums[i];
                break;
            }
        }
        if(j == len) {
            dp[len++] = nums[i];
            if(len == 3) return true;
        }
    }
    return false;
}
```
