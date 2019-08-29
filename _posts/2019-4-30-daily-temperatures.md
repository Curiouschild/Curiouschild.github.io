---
title:  "739. Daily Temperatures"
date:   2019-4-30 20:17:00 +0930
categories: Leetcode
tags: Medium MonotonicStack
---

[{{page.title}}](https://leetcode.com/problems/daily-temperatures/){:target="_blank"}

    Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how
    many days you would have to wait until a warmer temperature. If there is no future day for which this is
    possible, put 0 instead.

    For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1,
    1, 4, 2, 1, 1, 0, 0].

    Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in
    the range [30, 100].

* Simple problem

```java

// find the first larger element with larger index
// monotonic stack
public int[] dailyTemperaturesMonotonicStack(int[] T) {
    Stack<Integer> stack = new Stack<>();
    // stack.push(Integer.MAX_VALUE);
    int[] result = new int[T.length];
    for(int i = 0; i < T.length; i++) {
        while(!stack.isEmpty() && T[stack.peek()] < T[i]) {
            int prev = stack.pop();
            result[prev] = i - prev;
        }
        stack.push(i);
    }
    return result;
}
```
