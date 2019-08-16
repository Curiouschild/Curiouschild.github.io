---
title:  "16. 3Sum Closest"
date:   2019-4-24 13:20:00 +0930
categories: Leetcode
tags: Medium Array
---

[{{page.title}}](https://leetcode.com/problems/3sum-closest/){:target="_blank"}

    Given an array nums of n integers and an integer target, find three integers in nums such that the sum is
    closest to target. Return the sum of the three integers. You may assume that each input would have exactly
    one solution.

    Example:

    Given array nums = [-1, 2, 1, -4], and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


* Based on classic three sum

```java

public int threeSumClosest(int[] nums, int target) {
    int result = nums[0] + nums[1] + nums[2];
    Arrays.sort(nums);
    for(int i = 0; i < nums.length - 2; i++) {
        int t = target - nums[i];
        int l = i+1, r = nums.length-1;
        while(l < r) {
            int sum = nums[l] + nums[r];
            if(sum < t) l++;
            else if(sum > t) r--;
            else return target;
            if(Math.abs(target - sum - nums[i]) < Math.abs(target - result))
                result = sum + nums[i];
        }
    }
    return result;
}
```
