---
title:  "560. Subarray Sum Equals K"
date:   2019-3-8 16:52:13 +0930
categories: Leetcode
tags: Array
---

[{{page.title}}](https://leetcode.com/problems/subarray-sum-equals-k/){:target="_blank"}

    Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

    Example 1:

    Input:nums = [1,1,1], k = 2
    Output: 2

    Note:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


* Acumulative Sum

```java
public int subarraySum3(int[] nums, int k) {
    int result = 0;
    for(int i = 0; i < nums.length; i++) {
        int sum = 0;
        for(int j = i; j < nums.length; j++) {
            sum += nums[j];
            if(sum == k) result++;
        }
    }
    return result;
}
```

* HashMap

```java
public int subarraySum(int[] nums, int k) {
    int count = 0, sum = 0;
    HashMap <Integer, Integer> map = new HashMap<>();
    map.put(0, 1);
    for (int i = 0; i < nums.length; i++) {
        sum += nums[i];
        if (map.containsKey(sum - k))
            count += map.get(sum - k);
        map.put(sum, map.getOrDefault(sum, 0) + 1);
    }
    return count;
}
```
