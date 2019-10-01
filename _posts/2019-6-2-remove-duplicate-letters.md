---
title:  "316. Remove Duplicate Letters"
date:   2019-06-02 09:48:00 +0930
categories: Leetcode
tags: Hard String
---

[{{page.title}}](https://leetcode.com/problems/remove-duplicate-letters/){:target="_blank"}

    Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears
    once and only once. You must make sure your result is the smallest in lexicographical order among all
    possible results.

    Example 1:

    Input: "bcabc"
    Output: "abc"

    Example 2:

    Input: "cbacdcbc"
    Output: "acdb"

* Using stack
  - easier than Hard

```java

public String removeDuplicateLetters(String s) {
    int[] cnt = new int[26];
    for(char c : s.toCharArray()) cnt[c-'a']++;
    HashSet<Character> set = new HashSet<>();
    Stack<Character> stack = new Stack<>();
    for(char c : s.toCharArray()) {
        if(!set.contains(c)) {
            while(!stack.isEmpty() && c < stack.peek() && cnt[stack.peek()-'a'] > 0) {
                set.remove(stack.pop());
            }
            stack.push(c);
            set.add(c);
        }
        cnt[c-'a']--;
    }
    StringBuilder sb = new StringBuilder();
    for(char c : stack) sb.append(c);
    return sb.toString();
}
```
