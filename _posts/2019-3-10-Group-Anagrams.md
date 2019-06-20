---
title:  "49. Group Anagrams"
date:   2019-3-10 16:12:30 +0930
categories: Leetcode
tags: HashMap
---

[{{page.title}}](https://leetcode.com/problems/group-anagrams/){:target="_blank"}

    Given an array of strings, group anagrams together.

    Example:

    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]

* Comparator

```java
public List<List<String>> groupAnagrams(String[] strs) {
    HashMap<String, ArrayList<String>> map = new HashMap<>();
    for(String s : strs) {
        char[] sc = s.toCharArray();
        Arrays.sort(sc);
        String sorted = new String(sc);
        ArrayList<String> arr = map.getOrDefault(sorted, new ArrayList<String>());
        arr.add(s);
        map.put(sorted, arr);
    }
    return new ArrayList(map.values());
}
```
