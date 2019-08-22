---
title:  "30. Substring with Concatenation of All Words"
date:   2019-4-28 21:43:00 +0930
categories: Leetcode
tags: Hard HashMap
---

[{{page.title}}](https://leetcode.com/problems/substring-with-concatenation-of-all-words/){:target="_blank"}

    You are given a string, s, and a list of words, words, that are all of the same length. Find all starting
    indices of substring(s) in s that is a concatenation of each word in words exactly once and without any
    intervening characters.

    Example 1:

    Input:
      s = "barfoothefoobarman",
      words = ["foo","bar"]
    Output: [0,9]
    Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
    The output order does not matter, returning [9,0] is fine too.

    Example 2:

    Input:
      s = "wordgoodgoodgoodbestword",
      words = ["word","good","best","word"]
    Output: []



* HashMap

```java

public List<Integer> findSubstring(String s, String[] words) {
    if(s.length() == 0 || words.length == 0) return new ArrayList<>();
    int wl = words[0].length(), len = words.length * wl;
    ArrayList<Integer> result = new ArrayList<>();
    for(int i = 0; i < s.length() - len + 1; i++) {
        if(check(s.substring(i, i+len), words, wl)) result.add(i);
    }
    return result;
}

public boolean check(String s, String[] words, int wl) {
    HashMap<String, Integer> map = new HashMap<>(), dict = new HashMap<>();
    for(String w : words) dict.put(w, dict.getOrDefault(w, 0)+1);
    int cnt = 0;
    for(int i = 0; i < words.length; i++) {
        String w = s.substring(i*wl, (i+1)*wl);
        if(dict.containsKey(w)) {
            map.put(w, map.getOrDefault(w,0)+1);
            if(map.get(w) > dict.get(w)) return false;
        } else return false;
    }
    return true;
}
```
