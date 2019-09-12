---
title:  "169. Majority Element"
date:   2019-05-19 23:28:00 +0930
categories: Leetcode
tags: Easy Gready Array HashMap
---

[{{page.title}}](https://leetcode.com/problems/majority-element/){:target="_blank"}

    Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

    You may assume that the array is non-empty and the majority element always exist in the array.

    Example 1:

    Input: [3,2,3]
    Output: 3

    Example 2:

    Input: [2,2,1,1,1,2,2]
    Output: 2



* Space O(N)

Decrease searching space

 [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
cnt=               0      0            0
maj=      7           5         5             7

```java

public int majorityElement(int[] nums) {
    int majority = 0, cnt = 0;
    for(int i : nums) {
        if(cnt == 0) majority = i;
        cnt += majority == i ? 1 : -1;
    }
    return majority;
}
```

* HashMap

```java

public int majorityElementMap(int[] nums) {
    HashMap<Integer, Integer> map = new HashMap<>();
    for(int i : nums) map.put(i, map.getOrDefault(i, 0)+1);
    Map.Entry<Integer, Integer> max = null;
    for(Map.Entry<Integer, Integer> e : map.entrySet()) {
        if(max == null || e.getValue() > max.getValue()) max = e;
    }
    return max.getKey();
}
```
