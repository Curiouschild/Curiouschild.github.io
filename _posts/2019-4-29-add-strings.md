---
title:  "415. Add Strings"
date:   2019-4-29 19:43:00 +0930
categories: Leetcode
tags: Easy Math
---

[{{page.title}}](https://leetcode.com/problems/add-strings/){:target="_blank"}

    Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

    Note:

        The length of both num1 and num2 is < 5100.
        Both num1 and num2 contains only digits 0-9.
        Both num1 and num2 does not contain any leading zero.
        You must not use any built-in BigInteger library or convert the inputs to integer directly.

* TwoPointers

```java

public String addStrings(String num1, String num2) {
    int i = num1.length()-1, j = num2.length()-1, carry = 0;
    String result = "";
    while(i >= 0 || j >= 0) {
        int sum = (i >= 0 ? (num1.charAt(i--)-'0') : 0) + (j >= 0 ? (num2.charAt(j--)-'0') : 0) + carry;
        result = (sum % 10) + result;
        carry = sum / 10;
    }
    return carry == 1 ? '1' + result : result;
}
```
