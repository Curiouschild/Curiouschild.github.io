---
title:  "44. Wildcard Matching"
date:   2019-3-11 12:03:29 +0930
categories: Leetcode
tags: DynamicProgramming Recursive
---

[{{page.title}}](https://leetcode.com/problems/wildcard-matching/){:target="_blank"}

    Given an input string (s) and a pattern (p), implement wildcard pattern matching with
    support for '?' and '*'.

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).

    The matching should cover the entire input string (not partial).

    Note:

      s could be empty and contains only lowercase letters a-z.
      p could be empty and contains only lowercase letters a-z, and characters like ? or *.

    Example 1:

    Input:
    s = "aa"
    p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

* Recursive

```java
public boolean isMatch(String s, String p) {
    if(p.length() == 0) return s.length() == 0;
    if(s.length() > 0 && (p.charAt(0) == '?' || p.charAt(0) == s.charAt(0))) {
        return isMatch(s.substring(1, s.length()), p.substring(1, p.length()));
    } else if(p.charAt(0) == '*') {
        return s.length() > 0 && isMatch(s.substring(1, s.length()), p) || isMatch(s, p.substring(1, p.length()));
    }
    return false;
}
```

* Recursive With Memorisation

```java
public boolean isMatch(String s, String p) {
    int[][] dp = new int[p.length()+1][s.length()+1];
    dp[0][0] = 1;
    return isMatchRecursive(s, p, dp);

}
public boolean isMatchRecursive(String s, String p, int[][] dp) {
    if(dp[p.length()][s.length()] != 0) return dp[p.length()][s.length()] == 1;
    if(p.length() == 0) return s.length() == 0;
    boolean result = false;
    if(s.length() > 0 && (p.charAt(0) == '?' || p.charAt(0) == s.charAt(0))) {
        result = isMatchRecursive(s.substring(1, s.length()), p.substring(1, p.length()), dp);
    } else if(p.charAt(0) == '*') {
        result = s.length() > 0 && isMatchRecursive(s.substring(1, s.length()), p, dp) || isMatchRecursive(s, p.substring(1, p.length()), dp);
    }
    dp[p.length()][s.length()] = result ? 1 : 2;
    return result;
}
```

* DynamicProgramming

The same with Shortest Edit Distance

```java
public boolean isMatch(String s, String p) {
    boolean[][] dp = new boolean[p.length()+1][s.length()+1];
    dp[0][0] = true;
    for(int i = 1; i <= p.length(); i++) {
        dp[i][0] = dp[i-1][0] && p.charAt(i-1) == '*';
        for(int j = 1; j <= s.length(); j++) {
            boolean addP = dp[i-1][j] && p.charAt(i-1) == '*';
            boolean addS = dp[i][j-1] && p.charAt(i-1) == '*';
            boolean addBoth = dp[i-1][j-1] && (p.charAt(i-1) == '*' || p.charAt(i-1) == '?' || p.charAt(i-1) == s.charAt(j-1));
            dp[i][j] = addP || addS || addBoth;
        }
    }
    return dp[p.length()][s.length()];
}
```
