---
title:  "76. Minimum Window Substring"
date:   2019-3-7 19:45:31 +0930
categories: Leetcode
tags: String SlidingWindow
---

[{{page.title}}](https://leetcode.com/problems/minimum-window-substring/){:target="_blank"}

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "AABC"
Output: "ADOBECODEBA"


```java
public String minWindow(String s, String t) {
    HashMap<Character, Integer> targets = new HashMap<>(); // chars we want
    for(char c : t.toCharArray()) {
        int v = targets.getOrDefault(c, 0);
        targets.put(c, v + 1);
    }
    HashMap<Character, Integer> map = new HashMap<>(); // chars in hand
    int left = 0, start = 0, end = Integer.MAX_VALUE, satisfied = 0;
    for(int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if(!targets.containsKey(c)) continue;
        int v = map.getOrDefault(c, 0);
        map.put(c, v + 1);
        if(v + 1 == targets.get(c)) { // new satisfied
            satisfied++;
        }

        while(satisfied == targets.size()) { // shrink left
            if(i - left < end - start) {
                end = i;
                start = left;
            }
            char pre = s.charAt(left++);
            if(!targets.containsKey(pre)) continue;
            map.put(pre, map.get(pre) - 1);
            if(map.get(pre) < targets.get(pre)) {
               satisfied--;
               while(left < s.length() && !targets.containsKey(s.charAt(left))) {
                   left++;
               }
            }
        }
    }
    return end == Integer.MAX_VALUE ? "" : s.substring(start, end + 1);
}
```
