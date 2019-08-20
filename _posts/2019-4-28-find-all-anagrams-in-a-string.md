---
title:  "438. Find All Anagrams in a String"
date:   2019-4-28 13:55:00 +0930
categories: Leetcode
tags: Medium HashMap SlidingWindow
---

[{{page.title}}](https://leetcode.com/problems/find-all-anagrams-in-a-string/){:target="_blank"}



    Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

    Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

    The order of output does not matter.

    Example 1:

    Input:
    s: "cbaebabacd" p: "abc"

    Output:
    [0, 6]

    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".

    Example 2:

    Input:
    s: "abab" p: "ab"

    Output:
    [0, 1, 2]

    Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".


* HashMap + sliding window

```java

public List<Integer> findAnagrams(String s, String p) {
    ArrayList<Integer> result = new ArrayList<>();
    if(s.length() < p.length()) return result;

    HashMap<Character, Integer> map = new HashMap<>(), dict = new HashMap<>();
    for(char c : p.toCharArray()) dict.put(c, dict.getOrDefault(c, 0)+1);
    int target = dict.size();
    int cnt = 0, len = 0;
    for(int i = 0; i < p.length(); i++) {
        char c = s.charAt(i);
        if(!dict.containsKey(c)) continue;
        map.put(c, map.getOrDefault(c, 0)+1);
        if(map.get(c).equals(dict.get(c))) cnt++;
    }

    if(cnt == target) result.add(0);
    for(int i = p.length(); i < s.length(); i++) {
        char c = s.charAt(i), prev = s.charAt(i-p.length());
        if(dict.containsKey(prev)) {
            int v = map.get(prev);
            if(v == dict.get(prev)) cnt--;
            if(v == 1) map.remove(prev);
            else map.put(prev, v-1);
        }
        if(dict.containsKey(c)) {
            map.put(c, map.getOrDefault(c, 0)+1);
            if(map.get(c).equals(dict.get(c))) cnt++;
            if(cnt == target) result.add(i-p.length()+1);
        }
    }
    return result;
}
```



* This is a bad idea. ex:
  111010   111001
  101010   101001

```java
public List<Integer> findAnagrams(String s, String p) {
    ArrayList<Integer> result = new ArrayList<>();
    int target = 0;
    for(char c : p.toCharArray()) {
        target ^= c;
    }
    int cnt = 0;
    int n = 0;
    for(int i = 0; i < s.length(); i++) {
        n ^= s.charAt(i);
        if(++cnt >= p.length()) {
            if(n == target) {
                System.out.println(i);
                if(target > 0 || target == 0 && s.substring(i-p.length()+1, i+1).equals(p))
                    result.add(i-p.length()+1);
            }
            n ^= s.charAt(i-p.length()+1);
        }
    }
    return result;
}
```
