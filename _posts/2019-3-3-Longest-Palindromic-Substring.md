---
title:  "5. Longest Palindromic Substring"
date:   2019-3-3 15:18:20 +0930
categories: Leetcode
tags: DP TwoPointer
---

[5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/){:target="_blank"}

    Given a string s, find the longest palindromic substring in s.
    You may assume that the maximum length of s is 1000.

1. Two Pointer Version

expand from center

```java
public String longestPalindrome(String s) {
    if(s.length()==0) return s;
    int left = 0, right = 0;
    for(int i = 0; i < s.length(); i++) {
        int[] single = check(i, i, s);
        int[] pair = {0, 0};
        if(i+1 < s.length() && s.charAt(i) == s.charAt(i+1)) {
            pair = check(i, i+1, s);
        }
        if(single[1]-single[0] > right - left) {
            right = single[1];
            left = single[0];
        }
        if(pair[1]-pair[0] > right - left) {
            right = pair[1];
            left = pair[0];
        }
    }
    return s.substring(left+1, right);
}

public int[] check(int left, int right, String s) {
    while(right >= left && right < s.length() && left >= 0) {
        if(s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        } else {
            break;
        }
    }
    return new int[]{left, right};
}
```
2. Manachers's Algorithm

```java
public String longestPalindrome(String s) {
    StringBuilder sb = new StringBuilder();
    for(char c : s.toCharArray()) {
        sb.append('#').append(c);
    }
    sb.append('#');
    s = sb.toString();
    int max = 0, axis = 0;
    int left = 0, right = 0;
    int[] dp = new int[s.length()];
    for(int i = 0; i < dp.length; i++) {
        int len = 0;
        if(i < max) {
            int mirrorIndex = 2 * axis - i;
            int mirrorLen = dp[mirrorIndex];
            len = Math.min(max-i, mirrorLen);
        }
        // starting from i + len, we expand the palindrome
        // becasue we know the substring between i and i + len is a palindrome
        int r = i + len, l = i - len;
        while(r + 1 < s.length() && l - 1 >= 0 && s.charAt(r+1) == s.charAt(l-1)) {
            r++;
            l--;
        }
        if(r - l > right - left) { // update result
            right = r;
            left = l;
        }
        if(r > max) { // expand right most
            max = r;
            axis = i;
        }
        dp[i] = r - i; // update dp array
    }
    sb.setLength(0);
    for(char c : s.substring(left, right+1).toCharArray()) {
        if(c != '#') sb.append(c);
    }

    return sb.toString();
}
```

3. Dynamic Programming

Define boolean dp[i][j] (if string(i,j) is a palindrome)
Increase window size from 1 to n
