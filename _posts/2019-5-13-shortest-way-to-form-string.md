---
title:  "1055. Shortest Way to Form String"
date:   2019-05-13 21:29:00 +0930
categories: Leetcode
tags: Medium String
---

[{{page.title}}](https://leetcode.com/problems/shortest-way-to-form-string/){:target="_blank"}

    From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

    Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

    Example 1:

    Input: source = "abc", target = "abcbc"
    Output: 2
    Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

    Example 2:

    Input: source = "abc", target = "acdbc"
    Output: -1
    Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.

    Example 3:

    Input: source = "xyz", target = "xzyxz"
    Output: 3
    Explanation: The target string can be constructed as follows "xz" + "y" + "xz".



    Constraints:

        Both the source and target strings consist of only lowercase English letters from "a"-"z".
        The lengths of source and target string are between 1 and 1000.



```java

public int shortestWay(String source, String target) {
    HashSet<Character> set = new HashSet<>();
    for(char c : source.toCharArray()) set.add(c);
    for(char c : target.toCharArray()) {
        if(!set.contains(c)) return -1;
    }
    int j = 0, result = 0;
    for(int i = 0; i < target.length();) {
        char c = target.charAt(i);
        while(j < source.length() && source.charAt(j) != c) j++;
        if(j == source.length()) {
            j = 0;
            result++;
        } else {
            j++;
            i++;
        }
    }
    result++;
    return result;
}
```
