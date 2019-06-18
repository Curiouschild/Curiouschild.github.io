---
title:  "269. Alien Dictionary"
date:   2019-3-8 11:15:11 +0930
categories: Leetcode
tags: TopographicSort
---

[{{page.title}}](https://leetcode.com/problems/alien-dictionary/){:target="_blank"}

There is a new alien language which uses the latin alphabet. However, the order
among letters are unknown to you. You receive a list of non-empty words from the
dictionary, where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.


    Example 1:

    Input:
    [
      "wrt",
      "wrf",
      "er",
      "ett",
      "rftt"
    ]

    Output: "wertf"

    Input:
    [
      "z",
      "x",
      "z"
    ]

    Output: ""

    Explanation: The order is invalid, so return "".

```java
public String alienOrder(String[] words) {
    HashMap<Character, HashSet<Character>> map = new HashMap<>(); // chars with neighbors
    HashSet<Character> allChars = new HashSet<>();
    for(Character ch : words[0].toCharArray()) allChars.add(ch);
    for(int i = 1; i < words.length; i++) {
        String p = words[i-1], c = words[i];
        for(Character ch : c.toCharArray()) allChars.add(ch);
        for(int j = 0; j < Math.min(p.length(), c.length()); j++) {
            if(p.charAt(j) != c.charAt(j)) {
                HashSet<Character> set = map.getOrDefault(p.charAt(j), new HashSet<Character>());
                set.add(c.charAt(j));
                map.put(p.charAt(j), set);
                break;
            }
        }
    }

    HashMap<Character, Integer> inDegree = new HashMap<>();
    for(Character c : allChars) inDegree.put(c, 0);
    for(HashSet<Character> set : map.values()) {
        for(Character c : set)
            inDegree.put(c, inDegree.get(c) + 1);
    }

    Queue<Character> q = new LinkedList<>();
    for(Character c : allChars) {
        if(inDegree.get(c) == 0)
            q.offer(c);
    }

    StringBuilder sb = new StringBuilder();
    while(!q.isEmpty()) {
        char c = q.poll();
        sb.append(c);
        if(map.containsKey(c)) {
            for(Character next : map.get(c)) {
                int v = inDegree.get(next);
                inDegree.put(next, v - 1);
                if(v - 1 == 0) q.offer(next);
            }
        }
    }
    return sb.length() == allChars.size() ? sb.toString() : "";
}
```
