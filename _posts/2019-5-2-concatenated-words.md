---
title:  "472. Concatenated Words"
date:   2019-05-02 14:38:00 +0930
categories: Leetcode
tags: Hard Tier
---

[{{page.title}}](https://leetcode.com/problems/concatenated-words/){:target="_blank"}

    Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.

    A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

    Example:

    Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

    Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

    Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
     "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
    "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

    Note:

        The number of elements of the given array will not exceed 10,000
        The length sum of elements in the given array will not exceed 600,000.
        All the input string will only include lower case letters.
        The returned elements order does not matter.


* Two heaps is a good friend of median of streaming data

Bug when tring to add memo pad

```java
class Solution {
    Node head = new Node();
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        if(words.length == 0) return new ArrayList<>();
        // build the Tier
        for(String w : words) {
            if(w.equals("")) continue;
            Node curr = head;
            for(char c : w.toCharArray()) {
                if(curr.arr[c-'a'] == null) curr.arr[c-'a'] = new Node();
                curr = curr.arr[c-'a'];
            }
            curr.w = w;
        }
        // search the Tier for every word: Backtrack
        List<String> result = new ArrayList<>();
        for(String w : words) {
            if(w.equals("")) continue;
            Node curr = head;
            for(char c : w.toCharArray())
                curr = curr.arr[c-'a'];
            curr.w = null; // the current word itself is not a legal sub word
            if(backtrack(w, map))
                result.add(w);
            curr.w = w;
        }
        return result;
    }

    public boolean backtrack(String w) {
        if(w.length() == 0) return true;
        Node curr = head;
        boolean result = false;
        for(int i = 0; i < w.length(); i++) {
            char c = w.charAt(i);
            curr = curr.arr[c-'a'];
            if(curr == null) return false;
            if(curr.w != null) {
                result |= backtrack(w.substring(i+1));
            }
            if(result) break;
        }
        return result;
    }

    class Node {
        Node[] arr = new Node[26];
        boolean isWord;
        String w;
    }
  }
```
