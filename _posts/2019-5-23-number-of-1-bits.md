---
title:  "191. Number of 1 Bits"
date:   2019-05-23 11:09:00 +0930
categories: Leetcode
tags: Easy BitManipulation
---

[{{page.title}}](https://leetcode.com/problems/number-of-1-bits/){:target="_blank"}

    Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the
    Hamming weight).

    Example 1:

    Input: 00000000000000000000000000001011
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

    Example 2:

    Input: 00000000000000000000000010000000
    Output: 1
    Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

    Example 3:

    Input: 11111111111111111111111111111101
    Output: 31
    Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.


```java
public int hammingWeight2(int n) {
    int result = 0;
    for(int i = 0; i < 32; i++) {
        result += ((n >>> i) & 1);
    }
    return result;
}
```

```java
public int hammingWeight(int n) {
    int result = 0;
    while(n != 0) {
        n &= (n-1);
        result++;
    }
    return result;
}
```
