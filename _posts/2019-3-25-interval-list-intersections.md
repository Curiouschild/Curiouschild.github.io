---
title:  "986. Interval List Intersections"
date:   2019-3-25 13:42:00 +0930
categories: Leetcode
tags: TwoPointers Interval
---

[{{page.title}}](https://leetcode.com/problems/interval-list-intersections/){:target="_blank"}

    Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

    Return the intersection of these two interval lists.

    (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
    The intersection of two closed intervals is a set of real numbers that is either empty, or can be
    represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)


    Example 1:
    Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
    Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.

![example1](/img/posts/interval_list_intersections.png)

    Note:

        0 <= A.length < 1000
        0 <= B.length < 1000
        0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
        


```java
public int[][] intervalIntersection(int[][] A, int[][] B) {
    ArrayList<int[]> arr = new ArrayList<>();
    int pa = 0, pb = 0;
    while(pa < A.length && pb < B.length) {
        int[] a = A[pa], b = B[pb];
        if(a[1] < b[0]) pa++;
        else if(b[1] < a[0]) pb++;
        else {
            int l = a[0] > b[0] ? a[0] : b[0];
            int r = a[1] < b[1] ? a[1] : b[1];
            arr.add(new int[] {l, r});
            if(r == a[1]) {
                pa++;
            } else {
                pb++;
            }
        }
    }
    int[][] result = new int[arr.size()][];
    int p = 0;
    for(int[] pair : arr) result[p++] = pair;
    return result;
}
```

or

```java

public int[][] intervalIntersection(int[][] A, int[][] B) {
    ArrayList<int[]> arr = new ArrayList<>();
    if(A.length == 0 || B.length == 0) return new int[0][];
    int[] curr = A[0], next = B[0];
    int i = 0;
    for(int[] a : A) {
        while(i < B.length) {
            int[] b = B[i];
            if((a[0] >= b[0] && a[0] <= b[1]) || (b[0] >= a[0] && b[0] <= a[1])) {
                arr.add(new int[] {Math.max(a[0],b[0]), Math.min(a[1],b[1])});
            }
            if(b[1] > a[1]) break;
            i++;
        }
    }
    int[][] result = new int[arr.size()][];
    for(int j = 0; j < result.length; j++) result[j] = arr.get(j);
    return result;
}

```
