---
title:  "340. Longest Substring with At Most K Distinct Characters"
date:   2019-3-19 22:11:01 +0930
categories: Leetcode
tags: HashMap TwoPointers SlidingWindow
---

[{{page.title}}](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/){:target="_blank"}

    Given a string, find the length of the longest substring T that contains at most k
    distinct characters.

    Example 1:

    Input: s = "eceba", k = 2
    Output: 3
    Explanation: T is "ece" which its length is 3.


```java
  public int lengthOfLongestSubstringKDistinct(String s, int k) {
      if(k == 0) return 0;
      HashMap<Character, Integer> map = new HashMap<>();
      int l = 0, r = 0, result = 0;
      while(r < s.length()) {
          while(map.size() == k && !map.containsKey(s.charAt(r))) {
              int v = map.get(s.charAt(l));
              if(v == 1) map.remove(s.charAt(l));
              else map.put(s.charAt(l), v-1);
              l++;
          }
          map.put(s.charAt(r), map.getOrDefault(s.charAt(r), 0) + 1);
          result = Math.max(result, r - l + 1);
          r++;
      }
      return result;
  }
```
