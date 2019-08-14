---
title:  "10. Regular Expression Matching"
date:   2019-3-10 19:54:23 +0930
categories: Leetcode
tags: Recursive DynamicProgramming RegularExpression String
---

[{{page.title}}](https://leetcode.com/problems/regular-expression-matching/){:target="_blank"}

    Given an input string (s) and a pattern (p), implement regular expression matching with
     support for '.' and '*'.

    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

    The matching should cover the entire input string (not partial).

    Note:

        s could be empty and contains only lowercase letters a-z.
        p could be empty and contains only lowercase letters a-z, and characters like . or *.

    Example 1:


    Input:
    s = "aa"
    p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

    Example 2:

    Input:
    s = "aa"
    p = "a*"
    Output: true
    Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating
     'a' once, it becomes "aa".

    Example 3:

    Input:
    s = "ab"
    p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".

* Recursive

```java
public boolean isMatch(String s, String p) {
    if(p.length() == 0) return s.length() == 0;
    boolean firstMatch = s.length() > 0 && (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.');
    if(p.length() > 1 && p.charAt(1) == '*') {
        boolean shrinkP = isMatch(s, p.substring(2, p.length()));
        if(shrinkP) return shrinkP; // s is empty, and p is a*b*c*
        boolean shrinkS = firstMatch && isMatch(s.substring(1, s.length()), p);
        return shrinkS;
    }
    return firstMatch && isMatch(s.substring(1, s.length()), p.substring(1, p.length()));
}
```

* DynamicProgramming

The same with Shortest Edit Distance

```java
public boolean isMatch(String s, String p) {
    boolean[][] dp = new boolean[p.length()+1][s.length()+1];
    dp[0][0] = true;

    //    "" s0 s1 s2 s3
    // "" T  F  F  F  F
    // p1
    // p2
    // p3
    // p4

    for(int i = 1; i < p.length()+1; i++) {
        // true when previous is true and current or then next is a "*"
        dp[i][0] = dp[i-1][0] && (p.charAt(i-1) == '*' || (i < p.length() && p.charAt(i) == '*'));
        for(int j = 1; j < s.length()+1; j++) {
            // add a p only when currenty p[i] is a "*" ,two situation: use p[i-1] or not use p[i-1]
            boolean addP = p.charAt(i-1) == '*' && (dp[i-1][j] || i-2 >= 0 && dp[i-2][j]);
            // add a s when previous p is "*", and this s is the same with the char before the "*"
            boolean addS = dp[i][j-1] && p.charAt(i-1) == '*' && (p.charAt(i-2) == '.' || p.charAt(i-2) == s.charAt(j-1));
            // add both when the left up diagonal is true and current s and p match
            boolean addBoth = dp[i-1][j-1] && (p.charAt(i-1) == '.' || p.charAt(i-1) == s.charAt(j-1) || i-2 >= 0 && p.charAt(i-1) == '*' && s.charAt(j-1) == p.charAt(i-2));
            dp[i][j] = addP || addS || addBoth;
        }
    }
    return dp[p.length()][s.length()];
}
```
