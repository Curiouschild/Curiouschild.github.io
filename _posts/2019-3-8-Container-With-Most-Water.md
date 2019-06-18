---
title:  "11. Container With Most Water"
date:   2019-3-8 09:02:11 +0930
categories: Leetcode
tags: TwoPointer
---

[{{page.title}}](https://leetcode.com/problems/container-with-most-water/){:target="_blank"}

    Given n non-negative integers a1, a2, ..., an , where each represents a point at
    coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
    line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms
    a container, such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.

![Example1](/img/posts/container_with_most_water.jpg)

    Example:

    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49

* TwoPointer

```java
public int maxArea(int[] height) {
    int l = 0, r = height.length - 1;
    int max = 0;
    while(l < r) {
        max = Math.max(max, Math.min(height[l], height[r]) * (r - l));
        if(height[l] < height[r]) l++;
        else r--;
    }
    return max;
}
```
