---
title:  "20. Valid Parentheses"
date:   2019-3-6 22:45:35 +0930
categories: Leetcode
tags: Stack Parentheses
---

[{{page.title}}](https://leetcode.com/problems/valid-parentheses/){:target="_blank"}

    Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

    Note that an empty string is also considered valid.

```java
public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();
    HashMap<Character, Character> map = new HashMap<>();
    map.put(')', '(');
    map.put(']', '[');
    map.put('}', '{');
    for(char c : s.toCharArray()) {
        if(!map.containsKey(c)) {
            stack.push(c);
        } else {
            if(!stack.isEmpty() && stack.peek() == map.get(c))
                stack.pop();
            else
                return false;
        }
    }
    return stack.isEmpty();
}
```
