---
title:  "264. Ugly Number II"
date:   2019-05-29 11:02:00 +0930
categories: Leetcode
tags: Medium DynamicProgramming Math
---

[{{page.title}}](https://leetcode.com/problems/ugly-number-ii/){:target="_blank"}

    Write a program to find the n-th ugly number.

    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

    Example:

    Input: n = 10
    Output: 12
    Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

    Note:

        1 is typically treated as an ugly number.
        n does not exceed 1690.

* pre computation

 three pointers a, b and c, to mark the last ugly number which was multiplied by 2, 3 and 5, correspondingly.

```java

class Solution {
    static int[] arr = new int[1690];
    {
        arr[0] = 1;
        int a = 0, b = 0, c = 0;
        for(int i = 1; i < arr.length; i++) {
            arr[i] = Math.min(Math.min(arr[a]*2, arr[b]*3), arr[c]*5);
            if(arr[i] == arr[a]*2) a++;
            if(arr[i] == arr[b]*3) b++;
            if(arr[i] == arr[c]*5) c++;
        }
    }
    public int nthUglyNumber(int n) {
        return arr[n-1];
    }
  }
```
