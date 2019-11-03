---
title:  "878. Nth Magical Number"
date:   2019-06-28 10:51:00 +0930
categories: Leetcode
tags: Hard Math BinarySearch
---

[{{page.title}}](https://leetcode.com/problems/nth-magical-number/){:target="_blank"}

    A positive integer is magical if it is divisible by either A or B.

    Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.

    Example 1:

    Input: N = 1, A = 2, B = 3
    Output: 2

    Example 2:

    Input: N = 4, A = 2, B = 3
    Output: 6

    Example 3:

    Input: N = 5, A = 2, B = 4
    Output: 10

    Example 4:

    Input: N = 3, A = 6, B = 4
    Output: 8

    Note:

        1 <= N <= 10^9
        2 <= A <= 40000
        2 <= B <= 40000


* BinarySearch

```java

class Solution {
    public int nthMagicalNumber(int N, int A, int B) {
        int lcm = lcm(A, B);
        long l = Math.min(A, B);
        long r = Long.MAX_VALUE;
        int MOD = 1_000_000_007;
        while(l < r) {
            long mid = l + (r-l) / 2;
            long v = mid / A + mid / B - mid / lcm;
            if(v > N) {
                r = mid - 1;
            } else if(v < N) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return (int) (l % MOD);
    }
    int lcm(int a, int b) {
        int gcd = gcd(a, b);
        return a * (b / gcd);
    }
    int gcd(int a, int b) {
        if(b == 0) return a;
        return gcd(b, a % b);
    }
}
```
