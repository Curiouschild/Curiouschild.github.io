---
title:  "34. Find First and Last Position of Element in Sorted Array"
date:   2019-4-3 16:25:00 +0930
categories: Leetcode
tags: PriorityQueue
---

[{{page.title}}](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/){:target="_blank"}


    Given an array of integers nums sorted in ascending order, find the starting and ending
    position of a given target value.

    Your algorithm's runtime complexity must be in the order of O(log n).

    If the target is not found in the array, return [-1, -1].

    Example 1:

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

* BinarySearch

```java
public int[] searchRange(int[] nums, int target) {
    int l = 0, r = nums.length;
    while(l < r) {
        int mid = l + (r-l) / 2;
        if(nums[mid] < target) l = mid + 1;
        else {
            r = mid;
        }
    }
    if(l == nums.length || nums[l] != target) return new int[] {-1,-1};
    r = l;
    while(r < nums.length && nums[r] == nums[l]) r++;
    return new int[] {l, r-1};
}
```
