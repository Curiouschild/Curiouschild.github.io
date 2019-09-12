---
title:  "280. Wiggle Sort"
date:   2019-05-20 16:42:00 +0930
categories: Leetcode
tags: Medium Array Sorting
---

[{{page.title}}](https://leetcode.com/problems/wiggle-sort/){:target="_blank"}

    Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

    Example:

    Input: nums = [3,5,2,1,6,4]
    Output: One possible answer is [3,5,1,6,2,4]


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
