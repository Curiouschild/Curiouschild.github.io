---
title:  "205. Isomorphic Strings"
date:   2019-05-11 13:47:00 +0930
categories: Leetcode
tags: Easy String
---

[{{page.title}}](https://leetcode.com/problems/isomorphic-strings/){:target="_blank"}

    Given two strings s and t, determine if they are isomorphic.

    Two strings are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of
    characters. No two characters may map to the same character but a character may map to itself.

    Example 1:

    Input: s = "egg", t = "add"
    Output: true

    Example 2:

    Input: s = "foo", t = "bar"
    Output: false

    Example 3:

    Input: s = "paper", t = "title"
    Output: true

    Note:
    You may assume both s and t have the same length.


* HashMap

```java

public boolean isIsomorphic(String s, String t) {
    HashSet<Character> used = new HashSet<>();
    HashMap<Character, Character> map = new HashMap<>();
    for(int i = 0; i < s.length(); i++) {
        char a = s.charAt(i), b = t.charAt(i);
        if(!map.containsKey(a)) {
            if(used.contains(b)) return false;
            used.add(b);
            map.put(a, b);
        }
        else if(map.get(a) != b) return false;
    }
    return true;
}
```
