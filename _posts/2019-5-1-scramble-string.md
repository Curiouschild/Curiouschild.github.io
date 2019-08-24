---
title:  "87. Scramble String"
date:   2019-05-01 10:22:00 +0930
categories: Leetcode
tags: Hard DivideAndConquer
---

[{{page.title}}](https://leetcode.com/problems/scramble-string/){:target="_blank"}

    Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings
    recursively.

    Below is one possible representation of s1 = "great":

        great
       /    \
      gr    eat
     / \    /  \
    g   r  e   at
               / \
              a   t

    To scramble the string, we may choose any non-leaf node and swap its two children.

    For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

        rgeat
       /    \
      rg    eat
     / \    /  \
    r   g  e   at
               / \
              a   t

    We say that "rgeat" is a scrambled string of "great".

    Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

        rgtae
       /    \
      rg    tae
     / \    /  \
    r   g  ta  e
           / \
          t   a

    We say that "rgtae" is a scrambled string of "great".

    Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

    Example 1:

    Input: s1 = "great", s2 = "rgeat"
    Output: true

    Example 2:

    Input: s1 = "abcde", s2 = "caebd"
    Output: false


Here is a iterative DP solution
https://leetcode.com/problems/scramble-string/discuss/29396/Simple-iterative-DP-Java-solution-with-explanation

for some 1 <= q < k we have:
  F(i, j, k) = (F(i, j, q) AND F(i + q, j + q, k - q)) OR (F(i, j + k - q, q) AND F(i + q, j, k - q))

* Recursive

```java
class Solution {
    public boolean isScramble(String s1, String s2) {
        if(s1.length() != s2.length()) return false;
        if(s1.equals(s2)) return true;
        if(s1.length() == 1) return false;
        int[] cnt = new int[26];
        for(char c : s1.toCharArray()) cnt[c-'a']++;
        for(char c : s2.toCharArray()) cnt[c-'a']--;
        for(int i : cnt) if(i != 0) return false;

        for(int i = 1; i < s1.length(); i++) {
            String s11 = s1.substring(0, i), s12 = s1.substring(i);
            String s21 = s2.substring(0, i), s22 = s2.substring(i);
            boolean r1 = isScramble(s11, s21) && isScramble(s12, s22);
            if(r1) return true;
            s21 = s2.substring(0, s1.length()-i);
            s22 = s2.substring(s1.length()-i);
            boolean r2 = isScramble(s11, s22) && isScramble(s12, s21);
            if(r2) return true;
        }
        return false;
    }
}
```
