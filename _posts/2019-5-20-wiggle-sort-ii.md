---
title:  "324. Wiggle Sort II"
date:   2019-05-20 15:37:00 +0930
categories: Leetcode
tags: Medium Array Sorting
---

[{{page.title}}](https://leetcode.com/problems/wiggle-sort-ii/){:target="_blank"}

    Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

    Example 1:

    Input: nums = [1, 5, 1, 1, 6, 4]
    Output: One possible answer is [1, 4, 1, 5, 1, 6].

    Example 2:

    Input: nums = [1, 3, 2, 2, 3, 1]
    Output: One possible answer is [2, 3, 1, 3, 1, 2].

    Note:
    You may assume all input has valid answer.

    Follow Up:
    Can you do it in O(n) time and/or in-place with O(1) extra space?

```java
public void wiggleSort(int[] nums) {
    Arrays.sort(nums);
    int[] result = new int[nums.length];
    int cnt = 0;
    for(int i = (result.length-1) % 2 == 1 ? result.length-2 : result.length-1; i >= 0; i -= 2) {
        result[i] = nums[cnt++];
    }
    for(int i = (result.length-1) % 2 == 0 ? result.length-2 : result.length-1; i >= 0; i -= 2) {
        result[i] = nums[cnt++];
    }
    System.arraycopy(result, 0, nums, 0, nums.length);
}
```
