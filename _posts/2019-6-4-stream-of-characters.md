---
title:  "1032. Stream of Characters"
date:   2019-06-04 15:38:00 +0930
categories: Leetcode
tags: Hard DataStructure
---

[{{page.title}}](https://leetcode.com/problems/stream-of-characters/){:target="_blank"}

    Implement the StreamChecker class as follows:

        StreamChecker(words): Constructor, init the data structure with the given words.
        query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order
        from oldest to newest, including this letter just queried) spell one of the words in the given list.



    Example:

    StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
    streamChecker.query('a');          // return false
    streamChecker.query('b');          // return false
    streamChecker.query('c');          // return false
    streamChecker.query('d');          // return true, because 'cd' is in the wordlist
    streamChecker.query('e');          // return false
    streamChecker.query('f');          // return true, because 'f' is in the wordlist
    streamChecker.query('g');          // return false
    streamChecker.query('h');          // return false
    streamChecker.query('i');          // return false
    streamChecker.query('j');          // return false
    streamChecker.query('k');          // return false
    streamChecker.query('l');          // return true, because 'kl' is in the wordlist



    Note:

        1 <= words.length <= 2000
        1 <= words[i].length <= 2000
        Words will only consist of lowercase English letters.
        Queries will only consist of lowercase English letters.
        The number of queries is at most 40000.



* Trie
  - keep a collection of candidate Tier nodes

```java

class StreamChecker {
    int max;
    ArrayList<Node> arr = new ArrayList<>();
    Node root;
    public StreamChecker(String[] words) {
        root = new Node();
        max = 0;
        for(String s : words) {
            max = Math.max(max, s.length());
            Node n = root;
            for(char c : s.toCharArray()) {
                if(n.arr[c-'a'] == null) n.arr[c-'a'] = new Node();
                n = n.arr[c-'a'];
            }
            n.isWord = true;
        }
    }

    public boolean query(char c) {
        boolean result = false;
        ArrayList<Node> temp = new ArrayList<>();
        arr.add(root);
        for(Node n : arr) {
            if(n.arr[c-'a'] == null) continue;
            temp.add(n.arr[c-'a']);
            if(n.arr[c-'a'].isWord) result = true;
        }
        arr = temp;
        return result;
    }

    class Node {
        Node[] arr = new Node[26];
        boolean isWord;
    }
}
```
