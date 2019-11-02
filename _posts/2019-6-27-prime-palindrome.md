---
title:  "866. Prime Palindrome"
date:   2019-06-27 15:15:00 +0930
categories: Leetcode
tags: Medium Tree
---

[{{page.title}}](https://leetcode.com/problems/prime-palindrome/){:target="_blank"}

    Find the smallest prime palindrome greater than or equal to N.

    Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1.

    For example, 2,3,5,7,11 and 13 are primes.

    Recall that a number is a palindrome if it reads the same from left to right as it does from right to left.

    For example, 12321 is a palindrome.

    Example 1:

    Input: 6
    Output: 7

    Example 2:

    Input: 8
    Output: 11

    Example 3:

    Input: 13
    Output: 101

    Note:

      1 <= N <= 10^8
      The answer is guaranteed to exist and be less than 2 * 10^8.

* Brutal Force of iterating palindromes by increasing root

```java

class Solution {
    public int primePalindrome(int N) {
        for(int i = 0; i <= 4; i++) {
            int root = (int)Math.pow(10, i), limit = root * 10;
            int temp = 0, p = 0;
            while(root < limit) {
                temp = reverseInt(root / 10);
                p = root * (int)Math.pow(10, i) + temp;
                if(p >= N && isPrime(p)) {
                    return p;
                }
                root++;
            }

            root = (int)Math.pow(10, i);
            while(root < limit) {
                temp = reverseInt(root);
                p = root * (int)Math.pow(10, i+1) + temp;
                if(p >= N && isPrime(p)) {
                    return p;
                }
                root++;
            }
        }
        return -1;
    }

    public int reverseInt(int n) {
        int r = 0;
        while(n > 0) {
            r = r * 10 + n % 10;
            n = n / 10;
        }
        return r;
    }

    public boolean isPrime(int n) {
        if(n < 2) return false;
        for(int i = 2; i <= (int)Math.sqrt(n); i++) {
            if(n % i == 0) return false;
        }
        return true;
    }
}
```
