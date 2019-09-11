---
title:  "698. Partition to K Equal Sum Subsets"
date:   2019-05-18 10:23:00 +0930
categories: Leetcode
tags: Medium Backtrack
---

[{{page.title}}](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/){:target="_blank"}

    Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

    Example 1:

    Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
    Output: True
    Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

    Note:

        1 <= k <= len(nums) <= 16.
        0 < nums[i] < 10000.



```java

public boolean canPartitionKSubsets(int[] nums, int k) {
    if(nums == null || nums.length == 0) return false;
    boolean[] used = new boolean[nums.length];
    int sum = 0;
    for(int i : nums) sum += i;
    // System.out.println(sum);
    if(sum % k != 0) return false;
    int target = sum / k;
    return backtrack(nums, used, target, 0, k, 0);
}

public boolean backtrack(int[] nums, boolean[] used, int target, int sum, int k, int start) {
    if(k == 1) return true;
    if(sum == target) return backtrack(nums, used, target, 0, k-1, 0);
    for(int i = start; i < nums.length; i++) {
        if(used[i]) continue;
        used[i] = true;
        boolean result = backtrack(nums, used, target, sum + nums[i], k, i+1);
        if(result) return true;
        used[i] = false;
    }
    return false;
}
```
