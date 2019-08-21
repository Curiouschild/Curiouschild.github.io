---
title:  "448. Find All Numbers Disappeared in an Array"
date:   2019-4-28 19:19:00 +0930
categories: Leetcode
tags: Easy Array
---

[{{page.title}}](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/){:target="_blank"}


    Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others
    appear once.

    Find all the elements of [1, n] inclusive that do not appear in this array.

    Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as
    extra space.

    Example:

    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [5,6]

* negative as duplicate

```java
public List<Integer> findDisappearedNumbers(int[] nums) {
    for(int i = 0; i < nums.length; i++) {
        int j = Math.abs(nums[i])-1;
        if(nums[j] > 0)
            nums[j] = -nums[j];
    }
    ArrayList<Integer> result = new ArrayList<>();
    for(int i = 0; i < nums.length; i++) {
        if(nums[i] > 0)
            result.add(i+1);
    }
    return result;

}
```
