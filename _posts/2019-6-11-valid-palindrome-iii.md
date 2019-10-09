---
title:  "1216. Valid Palindrome III"
date:   2019-06-11 14:54:00 +0930
categories: Leetcode
tags: Hard DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/valid-palindrome-iii/){:target="_blank"}

    Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

    A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from
    it.

    Example 1:

    Input: s = "abcdeca", k = 2
    Output: true
    Explanation: Remove 'b' and 'e' characters.

    Constraints:

        1 <= s.length <= 1000
        s has only lowercase English letters.
        1 <= k <= s.length


* Least Common Sequece of s and the reverse of s is the longest palindrome of s.

```java

class Solution {
    public boolean isValidPalindrome(String s, int k) {
        String r = new StringBuilder(s).reverse().toString();
        int lcs = lcs(s, r);
        return lcs >= s.length() - k;
    }
    public int lcs(String s1, String s2) {
        int[][] dp = new int[s1.length()+1][s2.length()+1];
        for(int i = 1; i < dp.length; i++) {
            for(int j = 1; j < dp[0].length; j++) {
                if(s1.charAt(i-1) == s2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[dp.length-1][dp[0].length-1];
    }
}
```
