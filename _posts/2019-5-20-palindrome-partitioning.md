---
title:  "131. Palindrome Partitioning"
date:   2019-05-20 09:41:00 +0930
categories: Leetcode
tags: Medium String Backtrack
---

[{{page.title}}](https://leetcode.com/problems/palindrome-partitioning/){:target="_blank"}

    Given a string s, partition s such that every substring of the partition is a palindrome.

    Return all possible palindrome partitioning of s.

    Example:

    Input: "aab"
    Output:
    [
      ["aa","b"],
      ["a","a","b"]
    ]

* backtrack

```java

public List<List<String>> partition(String s) {
    List<List<String>> result = new ArrayList<>();
    backtrack(result, new ArrayList<String>(), s, 0);
    return result;
}

public void backtrack(List<List<String>> result, List<String> temp, String s, int start) {
    if(start == s.length()) {
        result.add(new ArrayList<>(temp));
    }
    for(int i = start; i < s.length(); i++) {
        String sub = s.substring(start, i+1);
        if(isP(sub)) {
            temp.add(sub);
            backtrack(result, temp, s, i+1);
            temp.remove(temp.size()-1);
        }
    }
}

public boolean isP(String s) {
    for(int l = 0, r = s.length()-1; l < r; l++, r--) {
        if(s.charAt(l) != s.charAt(r)) return false;
    }
    return true;
}
```
