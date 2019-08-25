---
title:  "97. Interleaving String"
date:   2019-05-02 20:37:00 +0930
categories: Leetcode
tags: Hard Recursive
---

[{{page.title}}](https://leetcode.com/problems/interleaving-string/){:target="_blank"}

    Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

    Example 1:

    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true

    Example 2:

    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: false

* easy

Reminds me the Regular Expression Matching and Wild Matching

```java
public boolean isInterleave(String s1, String s2, String s3) {
    if(s1.length() + s2.length() != s3.length()) return false;
    HashMap<Character, Integer> map = new HashMap<>();
    for(char c : (s1+s2).toCharArray())
        map.put(c, map.getOrDefault(c, 0)+1);
    for(char c : s3.toCharArray()) {
        if(!map.containsKey(c)) return false;
        map.put(c, map.get(c)-1);
    }
    for(int i : map.values()) if(i != 0) return false;
    int[][] memo = new int[s1.length()+1][s2.length()+1];
    return check(s1, s2, s3, memo);
}
public boolean check(String s1, String s2, String s3, int[][] memo) {
    if(memo[s1.length()][s2.length()] != 0) return memo[s1.length()][s2.length()] == 1;
    if((s1+s2).equals(s3) || (s2+s1).equals(s3)) return true;
    if(s1.length() == 0 || s2.length() == 0) return false;
    boolean result = false;
    if(s1.charAt(0) == s3.charAt(0))
        result |= check(s1.substring(1), s2, s3.substring(1), memo);
    if(!result && s2.charAt(0) == s3.charAt(0))
        result |= check(s1, s2.substring(1), s3.substring(1), memo);
    memo[s1.length()][s2.length()] = result ? 1 : 2;
    return result;
}
```

* DP Version

```java

public boolean isInterleave(String s1, String s2, String s3) {
    if(s1.length() + s2.length() != s3.length()) return false;
    HashMap<Character, Integer> map = new HashMap<>();
    for(char c : (s1+s2).toCharArray())
        map.put(c, map.getOrDefault(c, 0)+1);
    for(char c : s3.toCharArray()) {
        if(!map.containsKey(c)) return false;
        map.put(c, map.get(c)-1);
    }
    for(int i : map.values()) if(i != 0) return false;


    boolean[][] dp = new boolean[s1.length()+1][s2.length()+1];
    dp[0][0] = true;
    for(int i = 1; i <= s1.length(); i++) dp[i][0] = s3.startsWith(s1.substring(0,i));
    for(int i = 1; i <= s2.length(); i++) dp[0][i] = s3.startsWith(s2.substring(0,i));
    for(int k = 2; k <= s3.length(); k++) {
        for(int i = k-s2.length() > 1 ? k-s2.length() : 1; i < k && i <= s1.length(); i++) {
            int j = k - i;
            dp[i][j] = (dp[i-1][j] && s1.charAt(i-1) == s3.charAt(k-1)) || (dp[i][j-1] && s2.charAt(j-1) == s3.charAt(k-1));
        }
    }
    return dp[s1.length()][s2.length()];
}

```
