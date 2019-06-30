---
title:  "84. Largest Rectangle in Histogram"
date:   2019-3-19 19:27:02 +0930
categories: Leetcode
tags: MonotonicStack
---

[{{page.title}}](https://leetcode.com/problems/largest-rectangle-in-histogram/){:target="_blank"}

    Given n non-negative integers representing the histogram's bar height where the width
    of each bar is 1, find the area of largest rectangle in the histogram.

  ![p1](/img/posts/largest_rectangle_in_histogram_1.png)

    Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

  ![p2](/img/posts/largest_rectangle_in_histogram_2.png)

    The largest rectangle is shown in the shaded area, which has area = 10 unit.


* MonotonicStack N * M

```java
public int largestRectangleArea(int[] h) {
    ArrayDeque<Integer> stack = new ArrayDeque<>();
    stack.push(-1);
    int result = 0;
    for(int i = 0; i < h.length; i++) {
        while(stack.peek() != -1 && h[stack.peek()] > h[i]) {
            int height = h[stack.pop()];
            result = Math.max(result, height * (i - 1 - stack.peek()));
        }
        stack.push(i);
    }
    while(stack.peek() != -1) {
        int height = h[stack.pop()];
        result = Math.max(result, height * (h.length - 1 - stack.peek()));
    }
    return result;
}
```
