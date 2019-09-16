---
title:  "307. Range Sum Query - Mutable"
date:   2019-05-23 11:34:00 +0930
categories: Leetcode
tags: Medium SegmentTree
---

[{{page.title}}](https://leetcode.com/problems/range-sum-query-mutable/){:target="_blank"}

    Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

    The update(i, val) function modifies nums by updating the element at index i to val.

    Example:

    Given nums = [1, 3, 5]

    sumRange(0, 2) -> 9
    update(1, 2)
    sumRange(0, 2) -> 8

    Note:

        The array is only modifiable by the update function.
        You may assume the number of calls to update and sumRange function is distributed evenly.

* Segment Tree

My first time to implement the segment tree.

```java

class NumArray {
    int[] arr;
    int[] nums;
    public NumArray(int[] nums) {
        if(!(nums == null || nums.length == 0)) {
        this.nums = nums;
        int n = nums.length;
        int h = (int)Math.ceil(Math.log(n) / Math.log(2));
        int len = (int)Math.pow(2, h+1) - 1;
        this.arr = new int[len];
        build(0, n-1, 0);
        }
    }

    public int build(int start, int end, int index) {
        if(start == end) {
            arr[index] = nums[start];
        } else {
            int mid = start + (end-start) / 2;
            arr[index] = build(start, mid, 2 * index + 1)
                        + build(mid+1, end, 2 * index + 2);
        }
        return arr[index];
    }

    public int query(int i, int j, int start, int end, int index) {
        if(start > j || end < i) return 0;
        if(start >= i && end <= j) return arr[index];
        int mid = start + (end-start) / 2;
        return query(i, j, start, mid, 2 * index + 1)
                + query(i, j, mid+1, end, 2 * index + 2);
    }

    public void update(int start, int end, int index, int targetIndex, int diff) {
        arr[index] += diff;
        if(start == end) {
            return;
        }
        int mid = start + (end-start) / 2;
        if(targetIndex <= mid) update(start, mid, 2 * index + 1, targetIndex, diff);
        else update(mid+1, end, 2 * index + 2, targetIndex, diff);
    }

    public void update(int i, int val) {
        if(nums == null) return;
        int diff = val - nums[i];
        nums[i] = val;
        update(0, nums.length-1, 0, i, diff);
    }

    public int sumRange(int i, int j) {
        if(nums == null) return 0;
        return query(i, j, 0, nums.length-1, 0);
    }
}
```
