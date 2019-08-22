---
title:  "977. Squares of a Sorted Array"
date:   2019-4-30 15:45:00 +0930
categories: Leetcode
tags: Easy BinarySearch TwoPointers
---

[{{page.title}}](https://leetcode.com/problems/squares-of-a-sorted-array/){:target="_blank"}


    Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number,
    also in sorted non-decreasing order.

    Example 1:

    Input: [-4,-1,0,3,10]
    Output: [0,1,9,16,100]

    Example 2:

    Input: [-7,-3,2,3,11]
    Output: [4,9,9,49,121]



    Note:

        1 <= A.length <= 10000
        -10000 <= A[i] <= 10000
        A is sorted in non-decreasing order.


* TwoPointers

```java
public int[] sortedSquares(int[] A) {
    int[] result = new int[A.length];
    int k = A.length-1;
    int l = 0, r = A.length-1;
    while(l <= r) {
        int left = Math.abs(A[l]);
        int right = Math.abs(A[r]);
        if(left > right) {
            result[k] = left * left;
            l++;
        } else {
            result[k] = right * right;
            r--;
        }
        k--;
    }
    return result;
}
```

* The first time I just start search from around 0 ... why have i done that ???
```java

public int[] sortedSquares(int[] A) {
    if(A.length == 1) return new int[] {A[0]*A[0]};
    int l = 0, r = A.length-1;
    while(l + 1 < r) {
        int mid = l + (r-l) / 2;
        if(A[mid] > 0) r = mid;
        else l = mid;
    }
    int[] result = new int[A.length];
    int k = 0;
    while(l >= 0 || r < A.length) {
        int left = l >= 0 ? Math.abs(A[l]) : Integer.MAX_VALUE;
        int right = r < A.length ? Math.abs(A[r]) : Integer.MAX_VALUE;
        if(left < right) {
            result[k] = left * left;
            l--;
        } else {
            result[k] = right * right;
            r++;
        }
        k++;
    }
    return result;
}
```
