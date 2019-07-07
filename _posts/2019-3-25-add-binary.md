---
title:  "67. Add Binary"
date:   2019-3-25 14:13:00 +0930
categories: Leetcode
tags: TwoPointers
---

[{{page.title}}](https://leetcode.com/problems/add-binary/){:target="_blank"}

    Given two binary strings, return their sum (also a binary string).

    The input strings are both non-empty and contains only characters 1 or 0.

    Example 1:

    Input: a = "11", b = "1"
    Output: "100"

    Example 2:

    Input: a = "1010", b = "1011"
    Output: "10101"




The same with adding two linkedlist:
[2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/){:target="_blank"}


```java
public String addBinary(String a, String b) {
    int carry = 0;
    int x = a.length()-1, y = b.length()-1;
    StringBuilder sb = new StringBuilder();
    while(x >= 0 || y >= 0) {
        int i = (x >= 0 && a.charAt(x) == '1') ? 1 : 0;
        int j = (y >= 0 && b.charAt(y) == '1') ? 1 : 0;
        int sum = i + j + carry;
        sb.insert(0, sum % 2);
        carry = sum / 2;
        x--;
        y--;
    }
    if(carry == 1) sb.insert(0, 1);
    return sb.toString();
}
```
