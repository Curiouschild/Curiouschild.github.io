---
title:  "528. Random Pick with Weight"
date:   2019-3-24 23:31:00 +0930
categories: Leetcode
tags: BinarySearch
---

[{{page.title}}](https://leetcode.com/problems/subarray-sums-divisible-by-k/){:target="_blank"}

    Given an array w of positive integers, where w[i] describes the weight of index i,
    write a function pickIndex which randomly picks an index in proportion to its weight.

    Note:

        1 <= w.length <= 10000
        1 <= w[i] <= 10^5
        pickIndex will be called at most 10000 times.

    Example 1:

    Input:
    ["Solution","pickIndex"]
    [[[1]],[]]
    Output: [null,0]


```java

class Solution {
    int[] arr;
    Random random = new Random();
    public Solution(int[] w) {
        arr = new int[w.length];
        arr[0] = w[0];
        for(int i = 1; i < arr.length; i++)
            arr[i] = arr[i-1] + w[i];
    }

    public int pickIndex() {
        int target = 1 + random.nextInt(arr[arr.length-1]);
        int l = 0, r = arr.length;
        while(l < r) {
            int mid = l + (r-l) / 2;
            if(arr[mid] >= target) r = mid;
            else l = mid + 1;
        }
        return l;
    }
  }
```
