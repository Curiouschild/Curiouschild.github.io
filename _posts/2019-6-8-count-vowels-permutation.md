---
title:  "1220. Count Vowels Permutation"
date:   2019-06-08 20:00 +0930
categories: Leetcode
tags: Hard DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/count-vowels-permutation/){:target="_blank"}

    Given an integer n, your task is to count how many strings of length n can be formed under the following
    rules:

        Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
        Each vowel 'a' may only be followed by an 'e'.
        Each vowel 'e' may only be followed by an 'a' or an 'i'.
        Each vowel 'i' may not be followed by another 'i'.
        Each vowel 'o' may only be followed by an 'i' or a 'u'.
        Each vowel 'u' may only be followed by an 'a'.

    Since the answer may be too large, return it modulo 10^9 + 7.

    Example 1:

    Input: n = 1
    Output: 5
    Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

    Example 2:

    Input: n = 2
    Output: 10
    Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

    Example 3:

    Input: n = 5
    Output: 68

    Constraints:

        1 <= n <= 2 * 10^4

* DP

```java

class Solution {
    public static int MOD = 1000000007;
    public int countVowelPermutation(int n) {
        long[] arr = new long[5]; // 0 -> 4 : 'a' -> 'u'
        // similar to 935. Knight Dialer
        Arrays.fill(arr, 1);
        for(int i = 2; i <= n; i++) {
            long[] temp = new long[5];
            for(int j = 0; j < 5; j++) {
                long v = arr[j];
                if(j == 0)
                    temp[1] += v;
                if(j == 1) {
                    temp[0] += v;
                    temp[2] += v;
                }
                if(j == 2) {
                    for(int k = 0; k < 5; k++)
                        if(k != 2) temp[k] += v;
                }
                if(j == 3) {
                    temp[2] += v;
                    temp[4] += v;
                }
                if(j == 4) temp[0] += v;
            }
            for(int j = 0; j < 5; j++) {
                temp[j] %= MOD;
            }
            arr = temp;
        }
        long result = 0;
        for(long i : arr) {
            result += i;
            result %= MOD;
        }
        return (int)result;
    }
}
```
