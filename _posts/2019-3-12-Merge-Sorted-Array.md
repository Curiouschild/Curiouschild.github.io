---
title:  "380. Insert Delete GetRandom O(1)"
date:   2019-3-12 19:28:10 +0930
categories: Leetcode
tags: HashMap ArrayList DataStructure
---

[{{page.title}}](https://leetcode.com/problems/insert-delete-getrandom-o1/){:target="_blank"}

    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

    Note:

        The number of elements initialized in nums1 and nums2 are m and n respectively.
        You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

    Example:

    Input:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3

    Output: [1,2,2,3,5,6]


* In place

```java
public void merge(int[] nums1, int m, int[] nums2, int n) {
    System.arraycopy(nums1, 0, nums1, n, m);
    int i = 0, p = n, q = 0;
    while(p < nums1.length && q < nums2.length)
        nums1[i++] = nums1[p] < nums2[q] ? nums1[p++] : nums2[q++];
    while(p < nums1.length) nums1[i++] = nums1[p++];
    while(q < nums2.length) nums1[i++] = nums2[q++];
}
```
