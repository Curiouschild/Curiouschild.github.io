---
title:  "290. Word Pattern"
date:   2019-05-26 12:05:00 +0930
categories: Leetcode
tags: Medium Array
---

[{{page.title}}](https://leetcode.com/problems/word-pattern/){:target="_blank"}

    Given a pattern and a string str, find if str follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty
    word in str.

    Example 1:

    Input: pattern = "abba", str = "dog cat cat dog"
    Output: true

    Example 2:

    Input:pattern = "abba", str = "dog cat cat fish"
    Output: false

    Example 3:

    Input: pattern = "aaaa", str = "dog cat cat dog"
    Output: false

    Example 4:

    Input: pattern = "abba", str = "dog dog dog dog"
    Output: false

    Notes:
    You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.


```java

public boolean wordPattern(String pattern, String str) {
    HashMap<String, Character> map = new HashMap<>();
    HashSet<Character> used = new HashSet<>();
    int p = 0;
    String[] arr = str.split(" ");
    if(arr.length != pattern.length()) return false;
    for(String s : arr) {
        if(p == pattern.length()) return false;
        if(map.containsKey(s) && map.get(s) != pattern.charAt(p)) {
            return false;
        }
        if(!map.containsKey(s) && used.contains(pattern.charAt(p))) {
            return false;
        }
        map.put(s, pattern.charAt(p));
        used.add(pattern.charAt(p));
        p++;
    }
    return true;
}
```
