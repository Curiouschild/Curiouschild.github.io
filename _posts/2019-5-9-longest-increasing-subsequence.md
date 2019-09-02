---
title:  "300. Longest Increasing Subsequence"
date:   2019-05-09 15:28:00 +0930
categories: Leetcode
tags: Medium Array
---

[{{page.title}}](https://leetcode.com/problems/longest-increasing-subsequence/){:target="_blank"}

    Given an unsorted array of integers, find the length of longest increasing subsequence.

    Example:

    Input: [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

    Note:

        There may be more than one LIS combination, it is only necessary for you to return the length.
        Your algorithm should run in O(n2) complexity.

    Follow up: Could you improve it to O(n log n) time complexity?


* Binary Search DP

```java
public int lengthOfLIS(int[] nums) {
    if(nums.length == 0) return 0;
    int[] dp = new int[nums.length];
    dp[0] = nums[0];
    int len = 1;
    for(int i = 1; i < nums.length; i++) {
        // first greater than nums[i]
        int l = 0, r = len;
        while(l < r) {
            int mid = l + (r-l) / 2;
            if(dp[mid] >= nums[i])
                r = mid;
            else
                l = mid + 1;
        }
        if(l == len) {
            dp[len++] = nums[i];
        } else {
            dp[l] = nums[i];
        }
    }
    return len;
}
```
