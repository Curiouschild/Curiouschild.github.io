---
title:  "26. Remove Duplicates from Sorted Array"
date:   2019-05-01 14:04:00 +0930
categories: Leetcode
tags: Easy Array
---

[{{page.title}}](https://leetcode.com/problems/remove-duplicates-from-sorted-array/){:target="_blank"}

    Given a sorted array nums, remove the duplicates in-place such that each element appear only once and
    return the new length.

    Do not allocate extra space for another array, you must do this by modifying the input array in-place with
    O(1) extra memory.

    Example 1:

    Given nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

    It doesn't matter what you leave beyond the returned length.


* Easy

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length == 0) return 0;
        int j = 1;
        for(int i = 1; i < nums.length; i++) {
            if(nums[i] != nums[i-1])
                nums[j++] = nums[i];
        }
        return j;
    }
}
```
