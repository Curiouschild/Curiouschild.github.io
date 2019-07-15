---
title:  "239. Sliding Window Maximum"
date:   2019-4-1 15:56:00 +0930
categories: Leetcode
tags: Dequeu DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/sliding-window-maximum/){:target="_blank"}

    Given an array nums, there is a sliding window of size k which is moving from the very left
    of the array to the very right. You can only see the k numbers in the window. Each time the
    sliding window moves right by one position. Return the max sliding window.

    Example:

    Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
    Output: [3,3,5,5,6,7]
    Explanation:

    Window position                Max
    -------------------------     -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7



```java
public int[] maxSlidingWindowDP(int[] nums, int k) {
    if(nums.length == 0 || k == 0) return new int[0];
    int[] result = new int[nums.length - k + 1];
    int[] leftMax = new int[nums.length], rightMax = new int[nums.length];
    for(int i = 0; i < leftMax.length; i++) {
        int pre = i % k == 0 || i == 0 ? Integer.MIN_VALUE : leftMax[i-1];
        leftMax[i] = Math.max(nums[i], pre);
    }
    for(int i = rightMax.length-1; i >= 0; i--) {
        int pre = i % k == k-1 || i == rightMax.length-1 ? Integer.MIN_VALUE : rightMax[i+1];
        rightMax[i] = Math.max(nums[i], pre);
    }

    for(int i = 0; i < result.length; i++)
        result[i] = Math.max(rightMax[i], leftMax[i+k-1]);
    return result;
}
```

```java
public int[] maxSlidingWindowDeQueue(int[] nums, int k) {
    if(nums.length == 0) return new int[0];
    ArrayDeque<int[]> q = new ArrayDeque<>();
    int[] result = new int[nums.length - k + 1];
    for(int i = 0; i < nums.length; i++) {
        if(!q.isEmpty() && q.peek()[0] <= i - k)
            q.poll();
        while(!q.isEmpty() && q.peekLast()[1] <= nums[i])
            q.removeLast();
        q.offer(new int[]{i, nums[i]});
        if(i-k+1 >= 0)
            result[i-k+1] = q.peek()[1];
    }
    return result;
}
```

```java
public void moveZeroes(int[] nums) {
    if (nums == null || nums.length == 0) return;

    int insertPos = 0;
    for (int num: nums) {
        if (num != 0) nums[insertPos++] = num;
    }

    while (insertPos < nums.length) {
        nums[insertPos++] = 0;
    }
}
```
