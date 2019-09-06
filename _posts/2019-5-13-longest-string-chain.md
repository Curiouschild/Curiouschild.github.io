---
title:  "1048. Longest String Chain"
date:   2019-05-13 23:50:00 +0930
categories: Leetcode
tags: Medium String
---

[{{page.title}}](https://leetcode.com/problems/longest-string-chain/){:target="_blank"}

    Given a list of words, each word consists of English lowercase letters.

    Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

    A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

    Return the longest possible length of a word chain with words chosen from the given list of words.



    Example 1:

    Input: ["a","b","ba","bca","bda","bdca"]
    Output: 4
    Explanation: one of the longest word chain is "a","ba","bda","bdca".



    Note:

        1 <= words.length <= 1000
        1 <= words[i].length <= 16
        words[i] only consists of English lowercase letters.



```java

public int longestStrChain(String[] words) {
    if(words.length == 0) return 0;
    ArrayList<ArrayList<String>> arr = new ArrayList<>();
    for(int i = 0; i <= 17; i++) arr.add(new ArrayList<>());
    for(String s : words) {
        arr.get(s.length()).add(s);
    }
    HashMap<String, Integer> map = new HashMap<>();
    for(int i = 16; i >= 1; i--) {
        for(String w : arr.get(i))
            map.put(w, 1);
        for(String s : arr.get(i)) {
            for(String l : arr.get(i+1)) {
                if(isValid(s, l)) {
                    map.put(s, Math.max(map.get(l)+1, map.get(s)));
                }
            }
        }
    }
    int result = 0;
    for(int v : map.values()) result = Math.max(v, result);
    return result;
}

public boolean isValid(String s, String l) {
    boolean flag = false;
    for(int i = 0, j = 0; i < s.length() && j < l.length(); i++, j++) {
        if(s.charAt(i) != l.charAt(j)) {
            if(flag) return false;
            flag = true;
            i--;
        }
    }
    return true;
}
```
