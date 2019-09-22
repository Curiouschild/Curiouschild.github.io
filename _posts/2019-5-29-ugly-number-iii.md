---
title:  "1201. Ugly Number III"
date:   2019-05-29 12:04:00 +0930
categories: Leetcode
tags: Medium BinarySearch Math
---

[{{page.title}}](https://leetcode.com/problems/ugly-number-iii/){:target="_blank"}

    Write a program to find the n-th ugly number.

    Ugly numbers are positive integers which are divisible by a or b or c.

    Example 1:

    Input: n = 3, a = 2, b = 3, c = 5
    Output: 4
    Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.

    Example 2:

    Input: n = 4, a = 2, b = 3, c = 4
    Output: 6
    Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 12... The 4th is 6.

    Example 3:

    Input: n = 5, a = 2, b = 11, c = 13
    Output: 10
    Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.

    Example 4:

    Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
    Output: 1999999984

    Constraints:

        1 <= n, a, b, c <= 10^9
        1 <= a * b * c <= 10^18
        It's guaranteed that the result will be in range [1, 2 * 10^9]


* Binray search & Math

remember how to calculate gcd and lcm.

    Euclid’s algorithm is based on the following property: if p>q then the gcd of p and q is the same as the
    gcd of p%q and q. p%q is the remainder of p which cannot be divided by q, e.g. 33 % 5 is 3. This is based
    on the fact that the gcd of p and q also must divided (p-q) or (p-2q) or (p-3q) .... Therefore you can subtract the maximum of a multitude q from p which is p%q.

    Then lcm can be calculated with gcd
    =>  a * b = x * gcd * y * gcd
    =>  lcm = x * y * gcd = a * b / gcd

    Math is beautiful.

```java

class Solution {
    public int nthUglyNumber(int k, int a, int b, int c) {
        long ab = lcm(a, b), bc = lcm(b,c), ac = lcm(a,c), abc = lcm(ab, c);
        int l = 0, r = 2 * (int)Math.pow(10, 9)+1;
        while(l < r) {
            int mid = l + (r-l) / 2;
            long order = getOrder(mid, a, b, c, ab, ac, bc, abc);
            if(order > k) {
                r = mid - 1;
            } else if(order < k) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }
    public long gcd(long a, long b) {
        if(b == 0) return a;
        return gcd(b, a % b); // a % b = a - n * b which can be divided by the gcd of a and b
                              // so the a, b, and a % b share the same gcd, and a > b && b > a % b
    }
    public long lcm(long a, long b) {
        long high = a > b ? a : b;
        long low = high == a ? b : a;
        return a * b / gcd(high, low);
    }
    public long getOrder(int n, int a, int b, int c, long ab, long ac, long bc, long abc) {
        return n/a + n/b + n/c - n/ab - n/ac - n/bc + n/abc;
    }
}
```
