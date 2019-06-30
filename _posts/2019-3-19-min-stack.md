---
title:  "155. Min Stack"
date:   2019-3-19 23:21:00 +0930
categories: Leetcode
tags: Stack DataStructure
---

[{{page.title}}](https://leetcode.com/problems/min-stack/){:target="_blank"}

    Design a stack that supports push, pop, top, and retrieving the minimum
    element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.


```java
class MinStack {
    Stack<Integer> mins = new Stack<>();
    Stack<Integer> stack = new Stack<>();
    public void push(int x) {
        if(mins.isEmpty()) mins.push(x);
        else mins.push(mins.peek() > x ? x : mins.peek());
        stack.push(x);
    }

    public void pop() {
        mins.pop();
        stack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return mins.peek();
    }
}
```
