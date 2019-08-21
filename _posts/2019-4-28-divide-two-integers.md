---
title:  "29. Divide Two Integers"
date:   2019-4-28 10:36:00 +0930
categories: Leetcode
tags: Medium BitManiputlation
---

[{{page.title}}](https://leetcode.com/problems/divide-two-integers/){:target="_blank"}


    Given two integers dividend and divisor, divide two integers without using multiplication, division and mod
    operator.

    Return the quotient after dividing dividend by divisor.

    The integer division should truncate toward zero.

    Example 1:

    Input: dividend = 10, divisor = 3
    Output: 3

    Example 2:

    Input: dividend = 7, divisor = -3
    Output: -2

    Note:

        Both dividend and divisor will be 32-bit signed integers.
        The divisor will never be 0.
        Assume we are dealing with an environment which could only store integers within the 32-bit signed
        integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231
        − 1 when the division result overflows.

* Bit

```java
public int divide(int dividend, int divisor) {
    boolean neg = (dividend ^ divisor) < 0;
    long x = dividend > 0 ? dividend : -(long)dividend, y = divisor > 0 ? divisor : -(long)divisor;

    long quotient = 0;
    while(x >= y) {
        long move = 1, temp = y;
        while((temp << 1) <= x) {
            move = move << 1;
            temp = temp << 1;
        }
        x -= temp;
        quotient += move;
    }

    quotient = !neg ? quotient : ~(quotient-1);
    if(quotient >= Integer.MAX_VALUE) return Integer.MAX_VALUE;
    if(quotient <= Integer.MIN_VALUE) return Integer.MIN_VALUE;
    return (int)quotient;
}
```
