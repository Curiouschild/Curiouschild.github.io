---
title:  "326. Power of Three; 231. Power of Two; 342. Power of Four"
date:   2019-05-23 11:34:00 +0930
categories: Leetcode
tags: Easy Math
---

[{{page.title}}](https://leetcode.com/problems/power-of-three/){:target="_blank"}

    Given an integer, write a function to determine if it is a power of three.

    Example 1:

    Input: 27
    Output: true


* Base conversion

```java
public boolean isPowerOfThree(int n) {
        return Integer.toString(n, 3).matches("^10*$");
}
```
