---
title:  "416. Partition Equal Subset Sum"
date:   2019-05-04 11:12:00 +0930
categories: Leetcode
tags: Medium Backtrack
---

[{{page.title}}](https://leetcode.com/problems/partition-equal-subset-sum/){:target="_blank"}

    Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

    Note:

        Each of the array element will not exceed 100.
        The array size will not exceed 200.

    Example 1:

    Input: [1, 5, 11, 5]

    Output: true

    Explanation: The array can be partitioned as [1, 5, 5] and [11].



    Example 2:

    Input: [1, 2, 3, 5]

    Output: false

    Explanation: The array cannot be partitioned into equal sum subsets.


* Brutal

```java
class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for(int i = 0; i < nums.length; i++) sum += nums[i];
        if(sum % 2 == 1) return false;
        System.out.println(sum / 2);
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i : nums) arr.add(i);
        Collections.sort(arr, Collections.reverseOrder());
        for(int i = 0; i < nums.length; i++) nums[i] = arr.get(i);
        boolean result = backtrack(nums, 0, 0, sum / 2, 0);
        return result;
    }

    public boolean backtrack(int[] nums, int start, int sum, int target, int abandon) {
        if(sum > target || start == nums.length || abandon > target) return false;
        if(sum == target) return true;
        boolean result = false;
        for(int i = start; i < nums.length; i++) {
            abandon += (i > start ? nums[i-1] : 0);
            result |= backtrack(nums, i+1, sum+nums[i], target, abandon);
            if(result) return true;
        }
        return result;
    }
}
```
