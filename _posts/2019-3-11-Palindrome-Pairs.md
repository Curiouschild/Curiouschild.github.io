---
title:  "336. Palindrome Pairs"
date:   2019-3-11 15:00:11 +0930
categories: Leetcode
tags: Tier String DataStructure
---

[{{page.title}}](https://leetcode.com/problems/palindrome-pairs/){:target="_blank"}

    Given a list of unique words, find all pairs of distinct indices (i, j) in the
    given list, so that the concatenation of the two words, i.e. words[i] + words[j]
    is a palindrome.

    Example 1:

    Input: ["abcd","dcba","lls","s","sssll"]
    Output: [[0,1],[1,0],[3,2],[2,4]]
    Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

    Example 2:

    Input: ["bat","tab","cat"]
    Output: [[0,1],[1,0]]
    Explanation: The palindromes are ["battab","tabbat"]


* Tier Tree

```java
public List<List<Integer>> palindromePairs(String[] words) {
    List<List<Integer>> result = new ArrayList<>();
    Tier dict = new Tier(words);
    for(int i = 0; i < words.length; i++) {
        String w = words[i];
        Node curr = dict.head;
        int j = w.length() - 1;
        while(j >= 0) {
            if(curr.i != -1 && curr.i != i && isPalindrome(w, 0, j)) {
                // we find a word is a palindrome with substring(j, w.length()),
                // so we only need to check whether the substring in the mid is also a palindrome
                result.add(new ArrayList(Arrays.asList(curr.i, i)));
            }
            char c = w.charAt(j--);
            curr = curr.next[c-'a'];
            if(curr == null) break;
        }

        if(j == -1 && curr != null) {
            // Word j run out, add all indexs at current node
            for(int k : curr.indexs) {
                if(k != i) result.add(new ArrayList(Arrays.asList(k, i)));
            }
        }
    }
    return result;
}

class Tier {
    Node head = new Node();
    public Tier(String[] words) {
        for(int i = 0; i < words.length; i++) {
            Node curr = head;
            for(int j = 0; j < words[i].length(); j++) {
                if(isPalindrome(words[i], j, words[i].length()-1)) curr.indexs.add(i);
                char c = words[i].charAt(j);
                if(curr.next[c-'a'] == null) curr.next[c-'a'] = new Node();
                curr = curr.next[c-'a'];
            }
            curr.indexs.add(i); // empty string is a valid P
            curr.i = i; // index of word ends at this node
        }
    }
}
class Node {
    int i = -1; // -1 means no words end at this node (letter)
    ArrayList<Integer> indexs = new ArrayList<>(); // a word with an index in this arraylist has a substring Palindrome from the char represented by this node to the end of this word
    Node[] next = new Node[26];
}

public boolean isPalindrome(String w, int i, int j) {
    while(i < j) {
        if(w.charAt(i++) != w.charAt(j--)) return false;
    }
    return true;
}
```
