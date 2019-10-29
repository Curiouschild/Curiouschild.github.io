---
title:  "1004. Max Consecutive Ones III"
date:   2019-06-25 15:53:00 +0930
categories: Leetcode
tags: Medium SlidingWindow
---

[{{page.title}}](https://leetcode.com/problems/max-consecutive-ones-iii/){:target="_blank"}

    Implementing the class MajorityChecker, which has the following API:

        MajorityChecker(int[] arr) constructs an instance of MajorityChecker with the given array arr;
        int query(int left, int right, int threshold) has arguments such that:
            0 <= left <= right < arr.length representing a subarray of arr;
            2 * threshold > right - left + 1, ie. the threshold is always a strict majority of the length of
            the subarray

    Each query(...) returns the element in arr[left], arr[left+1], ..., arr[right] that occurs at least
    threshold times, or -1 if no such element exists.



    Example:

    MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
    majorityChecker.query(0,5,4); // returns 1
    majorityChecker.query(0,3,3); // returns -1
    majorityChecker.query(2,3,2); // returns 2



    Constraints:

        1 <= arr.length <= 20000
        1 <= arr[i] <= 20000
        For each query, 0 <= left <= right < len(arr)
        For each query, 2 * threshold > right - left + 1
        The number of queries is at most 10000


* Sliding Window

```java

class Solution {
    public int longestOnes(int[] A, int K) {
        int l = 0, r = 0, result = 0, cnt = 0;
        while(r < A.length) {
            if(A[r++] == 0) cnt++;
            while(cnt > K) {
                if(A[l] == 0) {
                    cnt--;
                }
                l++;
            }
            result = Math.max(result, r-l);
        }
        return result;
    }
}

```
