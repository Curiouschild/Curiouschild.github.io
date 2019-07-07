---
title:  "12. Integer to Roman"
date:   2019-3-25 14:13:00 +0930
categories: Leetcode
tags: TwoPointers
---

[{{page.title}}](https://leetcode.com/problems/integer-to-roman/){:target="_blank"}

see also [{{page.title}}](https://leetcode.com/problems/roman-to-integer/){:target="_blank"}

    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    For example, two is written as II in Roman numeral, just two one's added together.
    Twelve is written as, XII, which is simply X + II. The number twenty seven is written
    as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However,
    the numeral for four is not IIII. Instead, the number four is written as IV. Because
    the one is before the five we subtract it making four. The same principle applies to
    the number nine, which is written as IX. There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.

    Given a roman numeral, convert it to an integer. Input is guaranteed to be within the
    range from 1 to 3999.

    Example 1:

    Input: "III"
    Output: 3

    Example 2:

    Input: "IV"
    Output: 4



```java
public String intToRoman(int n) {
    int[] arr = new int[] {1000,900,500,400,100,90,50,40,10,9,5,4,1};
    String[] val = new String[] {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
    int p = 0;
    String result = "";
    while(n > 0) {
        while(arr[p] > n) p++;
        result += val[p];
        n -= arr[p];
    }
    return result;
}
```
