---
title:  "28. Implement strStr()"
date:   2019-05-01 15:58:00 +0930
categories: Leetcode
tags: Easy String
---

[{{page.title}}](https://leetcode.com/problems/implement-strstr/){:target="_blank"}

    Implement strStr().

    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Example 1:

    Input: haystack = "hello", needle = "ll"
    Output: 2

    Example 2:

    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

    Clarification:

    What should we return when needle is an empty string? This is a great question to ask during an interview.

    For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

* TODO: implement KMP


* Brutal Force
```java
public int strStr(String s, String w) {
    if(w.length()==0) return 0;
    for(int i = 0; i < s.length() - w.length()+1 ; i++) {
        for(int j = 0; j < w.length(); j++) {
            if(s.charAt(i+j) != w.charAt(j))
                break;
            if(j == w.length()-1)
                return i;
        }
    }
    return -1;
}
```
