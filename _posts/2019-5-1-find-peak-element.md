---
title:  "162. Find Peak Element"
date:   2019-05-01 13:49:00 +0930
categories: Leetcode
tags: Medium BinarySearch
---

[{{page.title}}](https://leetcode.com/problems/find-peak-element/){:target="_blank"}

    A peak element is an element that is greater than its neighbors.

    Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

    The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

    You may imagine that nums[-1] = nums[n] = -∞.

    Example 1:

    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.

* Easy

```java
class Solution {
    public int findPeakElement(int[] nums) {
        int l = 0, r = nums.length-1;
        while(l+1 < r) {
            int mid = l + (r-l) / 2;
            int left = mid == 0 ? Integer.MIN_VALUE : nums[mid-1];
            int right = mid == nums.length-1 ? Integer.MIN_VALUE : nums[mid+1];
            if(nums[mid] > left && nums[mid] > right) return mid;
            else if(nums[mid] < left && nums[mid] > right) r = mid;
            else l = mid;
        }
        return nums[l] > nums[r] ? l : r;
    }
}
```
