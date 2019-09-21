---
title:  "325. Maximum Size Subarray Sum Equals k"
date:   2019-05-27 19:39:00 +0930
categories: Leetcode
tags: Medium Array
---

[{{page.title}}](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/){:target="_blank"}

    Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there
    isn't one, return 0 instead.

    Note:
    The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

    Example 1:

    Input: nums = [1, -1, 5, -2, 3], k = 3
    Output: 4
    Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

    Example 2:

    Input: nums = [-2, -1, 2, 1], k = 1
    Output: 2
    Explanation: The subarray [-1, 2] sums to 1 and is the longest.

    Follow Up:
    Can you do it in O(n) time?


```java

public int maxSubArrayLen(int[] nums, int k) {
    HashMap<Integer, Integer> map = new HashMap<>();
    map.put(0, -1);
    int sum = 0;
    int result = 0;
    for(int i = 0; i < nums.length; i++) {
        sum += nums[i];
        if(map.containsKey(sum-k)) { // find a candidate
            result = Math.max(result, i-map.get(sum-k));
        }
        if(!map.containsKey(sum)) map.put(sum, i); // keep the smallest index
    }
    return result;
}

```
