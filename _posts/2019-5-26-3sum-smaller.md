---
title:  "259. 3Sum Smaller"
date:   2019-05-26 11:53:00 +0930
categories: Leetcode
tags: Medium Array
---

[{{page.title}}](https://leetcode.com/problems/3sum-smaller/){:target="_blank"}

    Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j <
    k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

    Example:

    Input: nums = [-2,0,1,3], and target = 2
    Output: 2 
    Explanation: Because there are two triplets which sums are less than 2:
                 [-2,0,1]
                 [-2,0,3]

    Follow up: Could you solve it in O(n2) runtime?


* break three sum to two sum

```java

public int threeSumSmaller(int[] nums, int target) {
    Arrays.sort(nums);
    int result = 0;
    for(int i = 0; i < nums.length; i++) {
        int t = target - nums[i];
        int l = i+1, r = nums.length-1;
        while(l < r) {
            int sum = nums[l] + nums[r];
            if(sum < t) {
                result += r-l; // give up the smallest value
                l++;
            } else {
                r--; // give up the largest value
            }
        }
    }
    return result;
}
```
