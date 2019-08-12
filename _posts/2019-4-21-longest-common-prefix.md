---
title:  "14. Longest Common Prefix"
date:   2019-4-21 14:11:00 +0930
categories: Leetcode
tags: String
---

[{{page.title}}](https://leetcode.com/problems/longest-common-prefix/){:target="_blank"}

    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:

    Input: ["flower","flow","flight"]
    Output: "fl"

    Example 2:

    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

    Note:

    All given inputs are in lowercase letters a-z.



```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String result = "";
        int i = 0;
        out:while(strs.length > 0) {
            if(i == strs[0].length()) break out;
            char curr = strs[0].charAt(i);
            for(String s : strs) {
                if(i == s.length() || s.charAt(i) != curr) break out;
            }
            i++;
            result += curr;
        }
        return result;
    }
  }
```
