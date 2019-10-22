---
title:  "503. Next Greater Element II"
date:   2019-06-22 22:08:00 +0930
categories: Leetcode
tags: Medium MonotonicStack
---

[{{page.title}}](https://leetcode.com/problems/next-greater-element-ii/){:target="_blank"}

    Given a circular array (the next element of the last element is the first element of the array), print the
    Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to
    its traversing-order next in the array, which means you could search circularly to find its next greater
    number. If it doesn't exist, output -1 for this number.

    Example 1:

    Input: [1,2,1]
    Output: [2,-1,2]
    Explanation: The first 1's next greater number is 2;
    The number 2 can't find next greater number;
    The second 1's next greater number needs to search circularly, which is also 2.

    Note: The length of given array won't exceed 10000.

* First Version with Stack

```java

public int[] nextGreaterElements(int[] nums) {
    int[] arr = new int[nums.length * 2];
    System.arraycopy(nums, 0, arr, 0, nums.length);
    System.arraycopy(nums, 0, arr, nums.length, nums.length);
    int[] result = new int[nums.length];
    Arrays.fill(result, -1);
    LinkedList<Integer> q = new LinkedList<>();
    for(int i = 0; i < arr.length; i++) {
        while(!q.isEmpty() && arr[i] > arr[q.peekLast()]) {
            int index = q.removeLast();
            if(index < nums.length)
                result[index] = arr[i];
        }
        q.offer(i);
    }
    return result;
}
```

*  Optimization on space

```java

int[] result = new int[nums.length];
Arrays.fill(result, -1);
LinkedList<Integer> q = new LinkedList<>();
for(int i = 0; i < nums.length * 2; i++) {
    while(!q.isEmpty() && nums[i % nums.length] > nums[q.peekLast()]) {
        result[q.removeLast()] = nums[i % nums.length];
    }
    q.offer(i % nums.length);
}
return result;
}
```
