---
title:  "1004. Max Consecutive Ones III"
date:   2019-06-25 15:53:00 +0930
categories: Leetcode
tags: Medium SlidingWindow
---

[{{page.title}}](https://leetcode.com/problems/max-consecutive-ones-iii/){:target="_blank"}

    Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

    Return the length of the longest (contiguous) subarray that contains only 1s.



    Example 1:

    Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
    Output: 6
    Explanation:
    [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

    Example 2:

    Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
    Output: 10
    Explanation:
    [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

    Note:

      1 <= A.length <= 20000
      0 <= K <= A.length
      A[i] is 0 or 1

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
