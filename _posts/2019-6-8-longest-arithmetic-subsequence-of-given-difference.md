---
title:  "1218. Longest Arithmetic Subsequence of Given Difference"
date:   2019-06-08 22:08:00 +0930
categories: Leetcode
tags: Medium HashMap DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/){:target="_blank"}

    Given an integer array arr and an integer difference, return the length of the longest subsequence in arr
    which is an arithmetic sequence such that the difference between adjacent elements in the subsequence
    equals difference.

    Example 1:

    Input: arr = [1,2,3,4], difference = 1
    Output: 4
    Explanation: The longest arithmetic subsequence is [1,2,3,4].

    Example 2:

    Input: arr = [1,3,5,7], difference = 1
    Output: 1
    Explanation: The longest arithmetic subsequence is any single element.

    Example 3:

    Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
    Output: 4
    Explanation: The longest arithmetic subsequence is [7,5,3,1].



* HashMap < value, length of valid sequence ends at this value>

```java

class Solution {
    public int longestSubsequence(int[] arr, int d) {
        int result = 1;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < arr.length; i++) {
            if(map.containsKey(arr[i]-d)) {
                map.put(arr[i], map.get(arr[i]-d)+1);
            } else {
                map.put(arr[i], 1);
            }
            result = Math.max(result, map.get(arr[i]));
        }
        return result;
    }
}
```
