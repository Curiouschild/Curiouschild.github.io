---
title:  "72. Edit Distance"
date:   2019-3-11 12:35:29 +0930
categories: Leetcode
tags: DynamicProgramming Recursive
---

[{{page.title}}](https://leetcode.com/problems/edit-distance/){:target="_blank"}

    Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

    You have the following 3 operations permitted on a word:

      Insert a character
      Delete a character
      Replace a character

    Example 1:

    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation:
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')

* Recursive (TLE)

```java
public int minDistance(String s, String p) {
    return minDistanceRecursive(s, p, 0);
}

public int minDistanceRecursive(String s, String p, int cnt) {
    if(s.length() == 0) return p.length() + cnt;
    if(p.length() == 0) return s.length() + cnt;
    if(s.equals(p)) return cnt;
    int result = Integer.MAX_VALUE;
    if(s.charAt(0) == p.charAt(0)) {
        int addBoth = minDistanceRecursive(s.substring(1, s.length()), p.substring(1, p.length()), cnt);
        result = Math.min(result, addBoth);
    } else {
        int addS = minDistanceRecursive(s.substring(1, s.length()), p, cnt + 1);
        int addP = minDistanceRecursive(s, p.substring(1, p.length()), cnt + 1);
        int addBoth = minDistanceRecursive(s.substring(1, s.length()), p.substring(1, p.length()), cnt + 1);
        result = Math.min(Math.min(addS, addBoth), Math.min(addP, result));
    }
    return result;
}
```


* DynamicProgramming

```java
public int minDistanceDP(String s, String p) {
    int[][] dp = new int[p.length()+1][s.length()+1];
    for(int j = 1; j <= s.length(); j++) dp[0][j] = dp[0][j-1] + 1;
    for(int i = 1; i <= p.length(); i++) {
        dp[i][0] = dp[i-1][0] + 1;
        for(int j = 1; j <= s.length(); j++) {
            int addP = dp[i-1][j] + 1, addS = dp[i][j-1] + 1, addBoth = s.charAt(j-1) == p.charAt(i-1) ? dp[i-1][j-1] : dp[i-1][j-1] + 1;
            dp[i][j] = Math.min(addP, Math.min(addS, addBoth));
}
    }
    return dp[p.length()][s.length()];
}

```
