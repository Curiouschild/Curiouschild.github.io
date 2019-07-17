---
title:  "45. Jump Game II"
date:   2019-4-2 16:43:00 +0930
categories: Leetcode
tags: BFS DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/jump-game-ii/){:target="_blank"}

    Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Your goal is to reach the last index in the minimum number of jumps.

    Example:

    Input: [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2.
        Jump 1 step from index 0 to 1, then 3 steps to the last index.

```java
public int jump(int[] nums) {
    if(nums.length <= 1) return 0;
    int i = 0, frontier = 0, step = -1;
    while(i < nums.length) {
        int newFrontier = -1;
        while(i <= frontier && i < nums.length) {
            newFrontier = Math.max(newFrontier, i+nums[i]);
            i++;
        }
        frontier = newFrontier;
        step++;
    }
    return step;
}
```
