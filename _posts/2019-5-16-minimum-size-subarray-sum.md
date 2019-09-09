---
title:  "209. Minimum Size Subarray Sum"
date:   2019-05-16 22:29:00 +0930
categories: Leetcode
tags: Medium Math
---

[{{page.title}}](https://leetcode.com/problems/minimum-size-subarray-sum/){:target="_blank"}

    Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous
    subarray of which the sum ≥ s. If there isn't one, return 0 instead.

    Example: 

    Input: s = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: the subarray [4,3] has the minimal length under the problem constraint.

    Follow up:
    If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n
    log n).


```java

public int minSubArrayLen(int s, int[] nums) {
    if(nums.length == 0) return 0;
    int sum = nums[0], l = 0, r = l;
    int result = nums.length+1;
    while(true) {
        if(sum < s) {
            if(r + 1 == nums.length) break;
            sum += nums[++r];
        } else {
            result = Math.min(result, r-l+1);
            if(l == nums.length) break;
            sum -= nums[l++];
        }
    }
    return result == nums.length+1 ? 0 : result;
}
```
