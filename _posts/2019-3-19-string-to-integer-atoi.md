---
title:  "904. Fruit Into Baskets"
date:   2019-3-19 23:00:00 +0930
categories: Leetcode
tags: String
---

[{{page.title}}](https://leetcode.com/problems/string-to-integer-atoi/){:target="_blank"}

    Implement atoi which converts a string to an integer.

    The function first discards as many whitespace characters as necessary until the first
    non-whitespace character is found. Then, starting from this character, takes an optional
    initial plus or minus sign followed by as many numerical digits as possible, and interprets
    them as a numerical value.

    The string can contain additional characters after those that form the integral number,
    which are ignored and have no effect on the behavior of this function.

    If the first sequence of non-whitespace characters in str is not a valid integral number,
    or if no such sequence exists because either str is empty or it contains only whitespace
    characters, no conversion is performed.

    If no valid conversion could be performed, a zero value is returned.

    Note:

        Only the space character ' ' is considered as whitespace character.
        Assume we are dealing with an environment which could only store integers within the 32-bit
        signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of
        representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

    Example 1:

    Input: "42"
    Output: 42

    Example 2:

    Input: "   -42"
    Output: -42
    Explanation: The first non-whitespace character is '-', which is the minus sign.
                 Then take as many numerical digits as possible, which gets 42.



```java

public int myAtoi(String str) {
    double result = 0;
    int l = 0, r = 0, sign = 1;
    while(r < str.length() && str.charAt(r) == ' ') r++;
    if(r == str.length()) return 0;
    char first = str.charAt(r);
    if(first == '-' || first == '+') {
        if(first == '-') sign = -1;
        r++;
    } else if(!Character.isDigit(first))  {
        return 0;
    }

    l = r;
    // time to pick digits
    while(r < str.length() && Character.isDigit(str.charAt(r))) {
        r++;
    }
    // r stops at the first character that is not a digit
    String num = str.substring(l, r);
    if(num.length() != 0) result = Double.valueOf(num);

    result = result * sign;
    if(result > Integer.MAX_VALUE) result = Integer.MAX_VALUE;
    else if(result < Integer.MIN_VALUE) result = Integer.MIN_VALUE;
    return (int)result;
}
```