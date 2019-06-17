---
title:  "56. Merge Intervals"
date:   2019-3-6 23:15:45 +0930
categories: Leetcode
tags: Interval
---

[{{page.title}}](https://leetcode.com/problems/merge-intervals/){:target="_blank"}

    Given a collection of intervals, merge all overlapping intervals.
    Example:
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

```java
public int[][] merge(int[][] intervals) {
       List<int[]> result = new ArrayList<>();
       Arrays.sort(intervals, new Comparator<int[]>() {
           public int compare(int[] x, int[] y) {
               return Integer.compare(x[0], y[0]);
           }
       });
       for(int[] i : intervals) {
           if(result.isEmpty()) result.add(i);
           else {
               int[] pre = result.get(result.size()-1);
               if(i[0] <= pre[1])
                   pre[1] = Math.max(pre[1], i[1]);
               else
                   result.add(i);
           }
       }
       int[][] arr = new int[result.size()][];
       for(int i = 0; i < result.size(); i++) arr[i] = result.get(i);
       return arr;
   }
```
