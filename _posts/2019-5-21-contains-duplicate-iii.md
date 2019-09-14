---
title:  "220. Contains Duplicate III"
date:   2019-05-21 22:42:00 +0930
categories: Leetcode
tags: Medium BinarySearchTree
---

[{{page.title}}](https://leetcode.com/problems/contains-duplicate-iii/){:target="_blank"}

    Given an array of integers, find out whether there are two distinct indices i and j in the array such that
    the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and
    j is at most k.

    Example 1:

    Input: nums = [1,2,3,1], k = 3, t = 0
    Output: true

    Example 2:

    Input: nums = [1,0,1,1], k = 1, t = 2
    Output: true

    Example 3:

    Input: nums = [1,5,9,1,5,9], k = 2, t = 3
    Output: false

* TreeSet

```java
public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
    if(nums.length <= 1 || k == 0) return false;
    TreeMap<Integer, Integer> map = new TreeMap<>();
    for(int i = 0; i < nums.length; i++) {
        Integer floor = map.floorKey(nums[i]), ceiling = map.ceilingKey(nums[i]);
        if(floor != null && (long)nums[i] - floor <= t) return true;
        if(ceiling != null && (long)ceiling - nums[i] <= t) return true;
        if(i >= k) {
            int prev = nums[i-k];
            if(map.get(prev) == 1) map.remove(prev);
            else map.put(prev, map.get(prev)-1);
        }
        map.put(nums[i], map.getOrDefault(nums[i],0)+1);
    }
    return false;
}
```
