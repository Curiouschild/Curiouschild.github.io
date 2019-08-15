---
title:  "341. Flatten Nested List Iterator"
date:   2019-4-3 16:11:00 +0930
categories: Leetcode
tags: Stack DataStructure
---

[{{page.title}}](https://leetcode.com/problems/flatten-nested-list-iterator/){:target="_blank"}

    Given a nested list of integers, implement an iterator to flatten it.

    Each element is either an integer, or a list -- whose elements may also be integers or other lists.

    Example 1:

    Input: [[1,1],2,[1,1]]
    Output: [1,1,2,1,1]
    Explanation: By calling next repeatedly until hasNext returns false,
                 the order of elements returned by next should be: [1,1,2,1,1].

* Stack
```java
public class NestedIterator implements Iterator<Integer> {
    Stack<NestedInteger> stack;
    public NestedIterator(List<NestedInteger> nestedList) {
        stack = new Stack<>();
        for(int i = nestedList.size()-1; i >= 0; i--) {
            stack.push(nestedList.get(i));
        }
    }
    public Integer next() {
        return stack.pop().getInteger();
    }
    public boolean hasNext() {
        if(stack.isEmpty()) return false;
        if(!stack.peek().isInteger()) {
            List<NestedInteger> nestedList = stack.pop().getList();
            for(int i = nestedList.size()-1; i >= 0; i--) {
                stack.push(nestedList.get(i));
            }
            hasNext(); // recursive flatten lists
        }
        return !stack.isEmpty(); // may flatten empty nested lists
    }
  }
```
