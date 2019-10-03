---
title:  "1092. Shortest Common Supersequence"
date:   2019-06-06 17:05:00 +0930
categories: Leetcode
tags: Hard DynamicProgramming SubSequence
---

[{{page.title}}](https://leetcode.com/problems/shortest-common-supersequence/){:target="_blank"}


    Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.
    If multiple answers exist, you may return any of them.

    (A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the
    characters are chosen anywhere from T) results in the string S.)

    Example 1:

    Input: str1 = "abac", str2 = "cab"
    Output: "cabac"
    Explanation:
    str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
    str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
    The answer provided is the shortest such string that satisfies these properties.


    Note:

        1 <= str1.length, str2.length <= 1000
        str1 and str2 consist of lowercase English letters.


* find the LCS

```java

String[][] memo;
public String shortestCommonSupersequence(String s1, String s2) {
    memo = new String[s1.length()][s2.length()];
    String lcs = lcs(s1, s2);
    // System.out.println(lcs);
    int[] a1 = new int[lcs.length()], a2 = new int[lcs.length()];
    mark(a1, s1, lcs);
    mark(a2, s2, lcs);
    StringBuilder sb = new StringBuilder();
    for(int i = 0; i < lcs.length(); i++) {
        if(i == 0) sb.append(s1.substring(0, a1[0])).append(s2.substring(0, a2[0]));
        sb.append(s1.charAt(a1[i]));
        if(i+1 < lcs.length()) sb.append(s1.substring(a1[i]+1, a1[i+1])).append(s2.substring(a2[i]+1, a2[i+1]));
        if(i == lcs.length()-1) sb.append(s1.substring(a1[i]+1)).append(s2.substring(a2[i]+1));
    }
    return sb.toString();
}
public void mark(int[] arr, String s, String lcs) {
    int i = 0, j = 0;
    while(j < lcs.length()) {
        while(i < s.length() && s.charAt(i) != lcs.charAt(j)) i++;
        arr[j] = i;
        i++;
        j++;
    }
}
public String lcs(String s1, String s2) {
    int i = s1.length()-1, j = s2.length()-1;
    if(i == -1 || j == -1) return "";
    if(memo[i][j] != null) return memo[i][j];
    char c1 = s1.charAt(i), c2 = s2.charAt(j);
    String result = null;
    if(c1 == c2) {
        result = lcs(s1.substring(0, i), s2.substring(0, j)) + c1;
    } else {
        String sub1 = lcs(s1.substring(0, i), s2);
        String sub2 = lcs(s1, s2.substring(0, j));
        result = sub1.length() > sub2.length() ? sub1 : sub2;
    }
    memo[i][j] = result;
    return result;
}
```
