---
title:  "7. Reverse Integer"
date:   2019-3-7 10:09:31 +0930
categories: Leetcode
tags: Math
---

[{{page.title}}](https://leetcode.com/problems/reverse-integer/){:target="_blank"}

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
of this problem, assume that your function returns 0 when the reversed integer overflows.


```java
public int reverse(int n) {
    int negative = n < 0 ? -1 : 1;
    long x = Math.abs(n), r = 0;
    while(x > 0) {
        r *= 10;
        r += x % 10;
        x /= 10;
    }
    return r > Integer.MAX_VALUE ? 0 : negative * (int)r;
}
```
