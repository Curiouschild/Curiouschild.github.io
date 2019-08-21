---
title:  "442. Find All Duplicates in an Array"
date:   2019-4-28 19:13:00 +0930
categories: Leetcode
tags: Medium Array
---

[{{page.title}}](https://leetcode.com/problems/find-all-duplicates-in-an-array/){:target="_blank"}

    Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear
    once.

    Find all the elements that appear twice in this array.

    Could you do it without extra space and in O(n) runtime?

    Example:

    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [2,3]


* negative as duplicate

I should have easily solved this problem, but ... T_T

```java
public List<Integer> findDuplicates(int[] nums) {
    ArrayList<Integer> result = new ArrayList<>();
    for(int i = 0; i < nums.length; i++) {
        int index = Math.abs(nums[i])-1;
        if(nums[index] < 0) result.add(index+1);
        else nums[index] = -nums[index];
    }
    return result;
}
```
