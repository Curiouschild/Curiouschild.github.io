---
title:  "42. Trapping Rain Water"
date:   2019-3-5 23:12:51 +0930
categories: Leetcode
tags: DynamicProgramming MonotonicStack
---

[{{page.title}}](https://leetcode.com/problems/trapping-rain-water/){:target="_blank"}

    Given n non-negative integers representing an elevation map where the
    width of each bar is 1, compute how much water it is able to trap after raining.

1. DynamicProgramming: Two Pass(left max and right max)

```java
public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> result = new ArrayList<>();
    for(int i = 0; i < nums.length - 2; i++) {
        if(i > 0 && nums[i] == nums[i-1]) continue; // remove duplicate
        int l = i + 1, r = nums.length-1;
        while(l < r) {
            if(l > i+1 && nums[l] == nums[l-1]) { // remove duplicate
                l++;
                continue;
            }
            if(nums[l] + nums[r] + nums[i] == 0) {
                result.add(new ArrayList<Integer>(Arrays.asList(nums[i], nums[l], nums[r])));
                l++;
                r--;
            } else if(nums[l] + nums[r] + nums[i] < 0) {
                l++;
            } else {
                r--;
            }
        }
    }
    return result;
}
```
2. DP: One Pass

```java
public int trap(int[] height) {
    int max = Integer.MIN_VALUE;
    int l = 0, r = height.length-1;
    int result = 0;
    while(l < r) {
        if(height[l] < height[r]) {
            max = Math.max(max, height[l]);
            result += Math.min(max, height[r]) - height[l];
            l++;
        } else {
            max = Math.max(max, height[r]);
            result += Math.min(max, height[l]) - height[r];
            r--;
        }
    }
    return result;
}
```

3. MonotonicStack

```java
public int trap(int[] height) {
    Deque<Integer> stack = new ArrayDeque<>();
    int result = 0;
    for(int i = 0; i < height.length; i++) {
        while(!stack.isEmpty() && height[i] >= height[stack.peek()]) {
            int base = height[stack.pop()];
            if(!stack.isEmpty()) {
                int preHeight = height[stack.peek()];
                result += (Math.min(preHeight, height[i]) - base) * (i-stack.peek() - 1);
            }
        }
        stack.push(i);
    }
    return result;
}
```
