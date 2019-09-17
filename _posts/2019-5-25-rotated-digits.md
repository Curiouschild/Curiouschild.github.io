---
title:  "788. Rotated Digits"
date:   2019-05-25 09:53:00 +0930
categories: Leetcode
tags: Easy Recursive
---

[{{page.title}}](https://leetcode.com/problems/rotated-digits/){:target="_blank"}

    X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is
    different from X.  Each digit must be rotated - we cannot choose to leave it alone.

    A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5
    rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other
    number and become invalid.

    Now given a positive number N, how many numbers X from 1 to N are good?

    Example:
    Input: 10
    Output: 4
    Explanation:
    There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
    Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

    Note:

      N  will be in range [1, 10000].



```java

class Solution {
    int result = 0;
    int[] arr = {0, 1, 8, 2, 5, 6, 9};
    int N;
    HashSet<Integer> set2569 = new HashSet<>(Arrays.asList(2,5,6,9));
    public int rotatedDigits(int N) {
        this.N = N;
        for(int i = 1; i < arr.length; i++) {
            count(arr[i], set2569.contains(arr[i]));
        }
        return result;
    }

    public void count(int curr, boolean has2569) {
        if(curr > N) return;
        if(has2569) result++;
        for(int i : arr) {
            count(curr * 10 + i, has2569 || set2569.contains(i));
        }
    }
}
```
