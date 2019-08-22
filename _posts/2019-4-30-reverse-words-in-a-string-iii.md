---
title:  "557. Reverse Words in a String III"
date:   2019-4-30 09:12:00 +0930
categories: Leetcode
tags: Easy String
---

[{{page.title}}](https://leetcode.com/problems/reverse-words-in-a-string-iii/){:target="_blank"}

    Given a string, you need to reverse the order of characters in each word within a sentence while still
    preserving whitespace and initial word order.

    Example 1:

    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

    Note: In the string, each word is separated by single space and there will not be any extra space in the
    string.

```java

public String reverseWords(String s) {
    StringBuilder sb = new StringBuilder(s);
    int i = 0, j = 0;
    while(i < s.length()) {
        while(i < s.length() && s.charAt(i) == ' ') i++;
        j = i;
        while(j < s.length() && s.charAt(j) != ' ') j++;
        reverse(sb, i, j-1);
        i = j;
    }
    return sb.toString();

}

public void reverse(StringBuilder sb, int i, int j) {
    while(i < j) {
        char c = sb.charAt(i);
        sb.setCharAt(i, sb.charAt(j));
        sb.setCharAt(j,c);
        i++;
        j--;
    }
}
```
