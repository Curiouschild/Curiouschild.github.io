---
title:  "301. Remove Invalid Parentheses"
date:   2019-3-7 09:30:22 +0930
categories: Leetcode
tags: BackTraking Parentheses
---

[{{page.title}}](https://leetcode.com/problems/remove-invalid-parentheses/){:target="_blank"}

    Remove the minimum number of invalid parentheses in order to
    make the input string valid. Return all possible results.

    Note: The input string may contain letters other than the parentheses ( and ).

    Example 1:

    Input: "()())()"
    Output: ["()()()", "(())()"]

    Example 2:

    Input: "(a)())()"
    Output: ["(a)()()", "(a())()"]


```java
public List<String> removeInvalidParentheses(String s) {
    int lb = 0, rb = 0;
    for(char c : s.toCharArray()) {
        if(c == '(') lb++;
        if(c == ')') {
            if(lb > 0) lb--;
            else rb++;
        }
    }
    HashSet<String> set = new HashSet<>();
    backtraking(lb, rb, 0, 0, set, s, 0, "");
    return new ArrayList<>(set);
}

public void backtraking(int lb, int rb, int left, int right, HashSet<String> set, String s, int i, String temp) {
    if(i == s.length()) {
        if(lb == 0 && rb == 0 && left == right) set.add(temp);
        return;
    }
    if(s.charAt(i) == '(') {
        if(lb > 0) {
            backtraking(lb-1, rb, left, right, set, s, i+1, temp);
        }
        backtraking(lb, rb, left+1, right, set, s, i+1, temp + "(");
    } else if(s.charAt(i) == ')') {
        if(rb > 0) {
            backtraking(lb, rb-1, left, right, set, s, i+1, temp);
        }
        if(left > right) {
            backtraking(lb, rb, left, right+1, set, s, i+1, temp + ")");
        }
    } else {
        backtraking(lb, rb, left, right, set, s, i+1, temp + s.charAt(i));
    }
}
```
