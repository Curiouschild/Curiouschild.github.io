---
title:  "3. Longest Substring Without Repeating Characters"
date:   2019-3-6 08:55:53 +0930
categories: Leetcode
tags: TwoPointer HashMap HashSet
---

[{{page.title}}](https://leetcode.com/problems/longest-substring-without-repeating-characters/){:target="_blank"}

    Given a string, find the length of the longest substring without repeating characters.

1. TwoPointer with HashSet

```java
public int lengthOfLongestSubstring(String s) {
    HashSet<Character> set = new HashSet<>();
    int result = 0, left = 0;
    for(int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        while(set.contains(c)) {
            set.remove(s.charAt(left++));
        }
        set.add(c);
        result = Math.max(set.size(), result);
    }
    return result;
}
```

2. TwoPointer with HashMap

```java
public int lengthOfLongestSubstring(String s) {
    HashMap<Character,Integer> map = new HashMap<>();
    int result = 0, left = 0;
    for(int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if(map.containsKey(c)) {
            left = Math.max(left, map.get(c)+1);
        }
        result = Math.max(result, i-left+1);
        map.put(c, i);
    }
    return result;
}
```
