---
title:  "745. Prefix and Suffix Search"
date:   2019-05-19 16:16:00 +0930
categories: Leetcode
tags: Hard Tier
---

[{{page.title}}](https://leetcode.com/problems/prefix-and-suffix-search/){:target="_blank"}

    Given many words, words[i] has weight i.

    Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will
    return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

    Examples:

    Input:
    WordFilter(["apple"])
    WordFilter.f("a", "e") // returns 0
    WordFilter.f("b", "") // returns -1

    Note:

        words has length in range [1, 15000].
        For each test case, up to words.length queries WordFilter.f may be made.
        words[i] has length in range [1, 10].
        prefix, suffix have lengths in range [0, 10].
        words[i] and prefix, suffix queries consist of lowercase letters only.

* Preprocess word to suffix + { + word

The trick: { ascill code --> 'z' + 1
           [ ---> 'Z' + 1
           becoming the 27th node of the tier

O(NK^2 + QK)

```java

class WordFilter {
    Node root;
    public WordFilter(String[] words) {
        root = new Node();
        root.index = words.length-1;
        for(int i = 0; i < words.length; i++) {
            for(int j = words[i].length(); j >= 0; j--) {
                String s = words[i].substring(j);
                String w =  s + "{" + words[i];
                Node curr = root;
                for(int k = 0; k < w.length(); k++) {
                    char c = w.charAt(k);
                    if(curr.arr[c-'a'] == null) curr.arr[c-'a'] = new Node();
                    curr = curr.arr[c-'a'];
                    curr.index = i;
                }
            }
        }
    }

    public int f(String prefix, String suffix) {
        String w = suffix + "{" + prefix;
        Node n = root;
        for(int i = 0; i < w.length(); i++) {
            char c = w.charAt(i);
            if(n.arr[c-'a'] == null) return -1;
            n = n.arr[c-'a'];
        }
        return n.index;
    }


    class Node {
        Node[] arr = new Node[27];
        int index = -1;
    }
}
```

* Two Tier

Intersection of two sets, pick the largest index

O(KN + Q(K+N))

```java
class WordFilter {
    Node pre, suf;
    public WordFilter(String[] words) {
        // System.out.println(Arrays.toString(words));
        pre = new Node();
        suf = new Node();
        HashSet<Integer> all = new HashSet<>();
        for(int i = 0; i < words.length; i++) all.add(i);
        pre.set = all;
        suf.set = all;
        for(int i = 0; i < words.length; i++) {
            String w = words[i];
            Node pc = pre, sc = suf;
            for(int j = 0; j < w.length(); j++) {
                char c = w.charAt(j);
                if(pc.arr[c-'a'] == null) pc.arr[c-'a'] = new Node();
                pc = pc.arr[c-'a'];
                pc.set.add(i);
            }
            for(int j = w.length()-1; j >= 0; j--) {
                char c = w.charAt(j);
                if(sc.arr[c-'a'] == null) sc.arr[c-'a'] = new Node();
                sc = sc.arr[c-'a'];
                sc.set.add(i);
            }

        }
    }

    public int f(String prefix, String suffix) {
        Node pc = pre, sc = suf;
        for(int i = 0; i < prefix.length(); i++) {
            char c = prefix.charAt(i);
            if(pc.arr[c-'a'] == null) return -1;
            pc = pc.arr[c-'a'];
        }
        for(int i = suffix.length()-1; i >= 0; i--) {
            char c = suffix.charAt(i);
            if(sc.arr[c-'a'] == null) return -1;
            sc = sc.arr[c-'a'];
        }

        int result = -1;
        for(int i : pc.set) {
            if(sc.set.contains(i)) {
                result = Math.max(result, i);
            }
        }
        return result;
    }

    class Node {
        Node[] arr = new Node[26];
        HashSet<Integer> set = new HashSet<>();
    }
}
```
