---
title:  "680. Valid Palindrome II"
date:   2019-05-03 12:12:00 +0930
categories: Leetcode
tags: Easy String Palindrome
---

[{{page.title}}](https://leetcode.com/problems/valid-palindrome-ii/){:target="_blank"}

    Given a non-empty string s, you may delete at most one character. Judge whether you can make it a
    palindrome.

    Example 1:

    Input: "aba"
    Output: True

    Example 2:

    Input: "abca"
    Output: True
    Explanation: You could delete the character 'c'.

    Note:

        The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


* easy

```java
class Solution {
    public boolean validPalindrome(String s) {
        int l = 0, r = s.length()-1;
        boolean deleted = false;
        while(l < r) {
            if(s.charAt(l) == s.charAt(r)) {
                l++;
                r--;
            } else {
                break;
            }
        }
        if(l >= r) return true;
        return check(s, l+1, r) || check(s, l, r-1);
    }

    public boolean check(String s, int l, int r) {
        while(l < r) {
            if(s.charAt(l++) != s.charAt(r--)) return false;
        }
        return true;
    }
}
```
