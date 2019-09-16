---
title:  "395. Longest Substring with At Least K Repeating Characters"
date:   2019-05-23 12:04:00 +0930
categories: Leetcode
tags: Medium DivideAndConquer
---

[{{page.title}}](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/){:target="_blank"}

    Find the length of the longest substring T of a given string (consists of lowercase letters only) such that
    every character in T appears no less than k times.

    Example 1:

    Input:
    s = "aaabb", k = 3

    Output:
    3

    The longest substring is "aaa", as 'a' is repeated 3 times.

    Example 2:

    Input:
    s = "ababbc", k = 2

    Output:
    5

    The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.



* Find the invalid characters, and use them to divide the input string.

Original problem can be greedily shrinked into subproblems.

```java
public int longestSubstring(String s, int k) {
    return count(s, k);
}

public int count(String s, int k) {
    if(s.length() == 0) return 0;
    int[] cnt = new int[26];
    for(char c : s.toCharArray()) cnt[c-'a']++;
    boolean allValid = true;
    for(int i = 0; i < 26; i++) {
        if(cnt[i] > 0 && cnt[i] < k) {
            allValid = false;
            cnt[i] = -1;
        }
    }
    if(allValid) return s.length();
    int result = 0, l = 0, r = 0;
    while(r < s.length()) {
        if(cnt[s.charAt(r)-'a'] == -1) {
            result = Math.max(result, count(s.substring(l, r), k));
            r++;
            l = r;
        } else {
            r++;
        }
    }
    if(l < s.length())
        result = Math.max(result, count(s.substring(l, s.length()), k));
    return result;
}
```
