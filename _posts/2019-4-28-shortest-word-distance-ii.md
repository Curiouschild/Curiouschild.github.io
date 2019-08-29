---
title:  "244. Shortest Word Distance II"
date:   2019-4-28 22:01:00 +0930
categories: Leetcode
tags: Medium TwoPointers
---

[{{page.title}}](https://leetcode.com/problems/shortest-word-distance-ii/){:target="_blank"}


    Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters.

    Example:
    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

    Input: word1 = “coding”, word2 = “practice”
    Output: 3

    Input: word1 = "makes", word2 = "coding"
    Output: 1

    Note:
    You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


```java
class WordDistance {
    HashMap<String, ArrayList<Integer>> map = new HashMap<>();
    public WordDistance(String[] words) {
        for(int i = 0; i < words.length; i++) {
            String s = words[i];
            ArrayList<Integer> arr = map.getOrDefault(s, new ArrayList<Integer>());
            arr.add(i);
            map.put(s, arr);
        }
    }

    public int shortest(String word1, String word2) {
        int x = 0, y = 0, result = Integer.MAX_VALUE;
        ArrayList<Integer> a = map.get(word1), b = map.get(word2);
        while(x < a.size() && y < b.size()) {
            result = Math.min(result, Math.abs(a.get(x)-b.get(y)));
            if(a.get(x) < b.get(y)) x++;
            else y++;
        }
        return result;
    }
}
```
