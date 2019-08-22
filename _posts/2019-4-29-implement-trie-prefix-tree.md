---
title:  "69. Sqrt(x)"
date:   2019-4-29 23:17:00 +0930
categories: Leetcode
tags: Medium Tier String
---

[{{page.title}}](https://leetcode.com/problems/implement-trie-prefix-tree/){:target="_blank"}



* Too simple.

Reminds me the dame problem Palindrome Pairs

```java

class Trie {
    Node head;
    class Node {
        Node[] arr = new Node[26];
        String w;
    }

    /** Initialize your data structure here. */
    public Trie() {
        head = new Node();
    }

    /** Inserts a word into the trie. */
    public void insert(String word) {
        Node n = head;
        for(char c : word.toCharArray()) {
            if(n.arr[c-'a'] == null) n.arr[c-'a'] = new Node();
            n = n.arr[c-'a'];
        }
        n.w = word;
    }

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        Node n = head;
        for(char c : word.toCharArray()) {
            n = n.arr[c-'a'];
            if(n == null) return false;
        }
        return n.w != null;

    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        Node n = head;
        for(char c : prefix.toCharArray()) {
            n = n.arr[c-'a'];
            if(n == null) return false;
        }
        return true;
    }
}
```
