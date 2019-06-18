---
title:  "22. Generate Parentheses"
date:   2019-3-8 12:18:11 +0930
categories: Leetcode
tags: Parentheses
---

[{{page.title}}](https://leetcode.com/problems/generate-parentheses/){:target="_blank"}


    Given n pairs of parentheses, write a function to generate all combinations
    of well-formed parentheses.

    For example, given n = 3, a solution set is:

    [
     "((()))",
     "(()())",
     "(())()",
     "()(())",
     "()()()"
    ]


* HashSet Brutal Force

```java
public List<String> generateParenthesis(int n) {
    HashSet<String> set = new HashSet<>();
    backtrack(n, 0, new StringBuilder(), set);
    return new ArrayList<>(set);
}

public void backtrack(int n, int m, StringBuilder sb, HashSet<String> set) {
    if(n == m) {
        set.add(sb.toString());
        return;
    }
    for(int i = 0; i <= sb.length() / 2; i++) {
        backtrack(n, m + 1, new StringBuilder(sb).insert(i, "()"), set);
    }
}
```

* Count left and right brackets

```java
public List<String> generateParenthesis(int n) {
    ArrayList<String> result = new ArrayList<>();
    backtrack(n, 0, 0, "", result);
    return result;
}

public void backtrack(int n, int left, int right, String temp, List<String> result) {
    if(left == n && right == n) {
        result.add(temp);
    } else {
        if(left < n) {
            backtrack(n, left + 1, right, temp + "(", result);
        }
        if(right < left) {
            backtrack(n, left, right + 1, temp + ")", result);
        }
    }
}
```
