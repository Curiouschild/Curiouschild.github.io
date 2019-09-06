---
title:  "166. Fraction to Recurring Decimal"
date:   2019-05-13 10:29:00 +0930
categories: Leetcode
tags: Medium Math
---

[{{page.title}}](https://leetcode.com/problems/fraction-to-recurring-decimal/){:target="_blank"}

    Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

    If the fractional part is repeating, enclose the repeating part in parentheses.

    Example 1:

    Input: numerator = 1, denominator = 2
    Output: "0.5"

    Example 2:

    Input: numerator = 2, denominator = 1
    Output: "2"

    Example 3:

    Input: numerator = 2, denominator = 3
    Output: "0.(6)"



```java

public String fractionToDecimal(int num, int den) {
    long numerator = num, denominator = den;
    int nega = numerator * denominator >= 0 ? 1 : -1;
    numerator = Math.abs(numerator);
    denominator = Math.abs(denominator);
    long b = numerator / denominator;
    long r = numerator % denominator;
    if(r == 0) {
        return "" + (b * nega);
    }
    HashMap<Long, Integer> map = new HashMap<>();
    int p = 0;
    String result = "";
    boolean repeat = false;
    while(true) {
        if(r == 0) break;
        if(map.containsKey(r)) {
            repeat = true;
            break;
        }
        map.put(r, p++);
        r *= 10;
        while(r < denominator) {
            result += "0";
            r *= 10;
            p++;
        }
        long n = r / denominator;
        result += n;
        r = r % denominator;
    }

    if(repeat) {
        String sub = result.substring(map.get(r));
        sub = "(" + sub + ")";
        result = result.substring(0, map.get(r)) + sub;
    }
    result = b + "." + result;
    if(nega == -1) result = "-" + result;
    return result;
}
```
