---
title:  "1031. Maximum Sum of Two Non-Overlapping Subarrays"
date:   2019-06-01 13:22:00 +0930
categories: Leetcode
tags: Medium Array
---

[{{page.title}}](https://leetcode.com/problems/stone-game/){:target="_blank"}

    Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping
    (contiguous) subarrays, which have lengths L and M.  (For clarification, the L-length subarray could occur
    before or after the M-length subarray.)

    Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... +
    A[j+M-1]) and either:

        0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
        0 <= j < j + M - 1 < i < i + L - 1 < A.length.


    Example 1:

    Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
    Output: 20
    Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

    Example 2:

    Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
    Output: 29
    Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

    Example 3:

    Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
    Output: 31
    Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.



    Note:

        L >= 1
        M >= 1
        L + M <= A.length <= 1000
        0 <= A[i] <= 1000

* O(N)
  - cache the largest array in A[0:j] and A[i:] with two arrays

```java

public int maxSumTwoNoOverlap(int[] A, int L, int M) {
    int[] prefix = new int[A.length+1];
    for(int i = 1; i < prefix.length; i++)
        prefix[i] = A[i-1] + prefix[i-1];
    int[] dp1 = new int[A.length]; // Largest subarray with length M in A[0:i]
    int[] dp2 = new int[A.length]; // Largest subarray with length M in A[i:]
    int sum = prefix[M] - prefix[0];
    dp1[M-1] = sum;
    for(int i = M; i < A.length; i++) {
        sum += (A[i]-A[i-M]);
        dp1[i] = Math.max(sum, dp1[i-1]);
    }
    sum = prefix[A.length] - prefix[A.length-M];
    dp2[A.length-M] = sum;
    for(int i = A.length-M-1; i >= 0; i--) {
        sum += (A[i]-A[i+M]);
        dp2[i] = Math.max(sum, dp2[i+1]);
    }
    int result = 0;
    for(int i = 0; i + L - 1 < A.length; i++) {
        int j = i + L - 1;
        int sumL = prefix[j+1] - prefix[i];
        int sumM = Math.max(i>1 ? dp1[i-1] : 0, j+1 < A.length ? dp2[j+1] : 0);
        result = Math.max(result, sumM + sumL);
    }
    return result;
}

```


* Brutal Force

```java

public int maxSumTwoNoOverlap(int[] A, int L, int M) {
    int[] prefix = new int[A.length+1];
    for(int i = 1; i < prefix.length; i++)
        prefix[i] = A[i-1] + prefix[i-1];
    int result = 0;
    for(int i = 0; i + L - 1 < A.length; i++) {
        int j = i + L - 1;
        int sumL = prefix[j+1] - prefix[i];
        int sumM = Integer.MIN_VALUE;
        for(int l = 0; l + M - 1 < i; l++) {
            int r = l + M - 1;
            sumM = Math.max(sumM, prefix[r+1]-prefix[l]);
        }
        for(int l = j+1; l + M - 1 < A.length; l++) {
            int r = l + M - 1;
            sumM = Math.max(sumM, prefix[r+1]-prefix[l]);
        }
        result = Math.max(result, sumM + sumL);
    }
    return result;
}
```
