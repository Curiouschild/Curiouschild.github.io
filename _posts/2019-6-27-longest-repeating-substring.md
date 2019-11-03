---
title:  "1062. Longest Repeating Substring"
date:   2019-06-27 17:33:00 +0930
categories: Leetcode
tags: Medium BinarySearch
---

[{{page.title}}](https://leetcode.com/problems/longest-repeating-substring/){:target="_blank"}

    Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring
    exists.

    Example 1:

    Input: "abcd"
    Output: 0
    Explanation: There is no repeating substring.

    Example 2:

    Input: "abbaba"
    Output: 2
    Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.

    Example 3:

    Input: "aabcaabdaab"
    Output: 3
    Explanation: The longest repeating substring is "aab", which occurs 3 times.

    Example 4:

    Input: "aaaaa"
    Output: 4
    Explanation: The longest repeating substring is "aaaa", which occurs twice.

    Note:

      The string S consists of only lowercase English letters from 'a' - 'z'.
      1 <= S.length <= 1500


* Binary Search + HashSet

```java

public int longestRepeatingSubstring(String S) {
    int l = 0, r = S.length()-1;
    while(l+1 < r) {
        int mid = l + (r-l) / 2;
        boolean valid = search(S, mid);
        if(valid) {
            l = mid;
        } else {
            r = mid;
        }
    }
    if(search(S, r)) return r;
    return l;
}

public boolean search(String S, int L) {
    HashSet<Integer> set = new HashSet<>();
    for(int i = 0; i+L-1 < S.length(); i++) {
        int j = i+L-1;
        int hash = S.substring(i, j+1).hashCode();
        if(set.contains(hash)) return true;
        set.add(hash);
    }
    return false;
}
}
```
