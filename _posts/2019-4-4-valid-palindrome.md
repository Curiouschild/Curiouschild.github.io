---
title:  "125. Valid Palindrome"
date:   2019-4-3 16:47:00 +0930
categories: Leetcode
tags: Palindrome TwoPointers
---

[{{page.title}}](https://leetcode.com/problems/valid-palindrome/){:target="_blank"}


    Given a string, determine if it is a palindrome, considering only alphanumeric characters
    and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid palindrome.

    Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true

    Example 2:

    Input: "race a car"
    Output: false




```java
public boolean isPalindrome(String s) {
    int l = 0, r = s.length()-1;
    while(l < r) {
        while(l < r && !Character.isLetter(s.charAt(l)) && !Character.isDigit(s.charAt(l))) {
            l++;
        }
        while(l < r && !Character.isLetter(s.charAt(r)) && !Character.isDigit(s.charAt(r))) {
            r--;
        }
        if(l < r) {
            if(Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r)) )
                return false;
            l++;
            r--;
        }
    }
    return true;
}
```
