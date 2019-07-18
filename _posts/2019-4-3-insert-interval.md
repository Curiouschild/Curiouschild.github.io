---
title:  "57. Insert Interval"
date:   2019-4-3 22:03:00 +0930
categories: Leetcode
tags: Interval
---

[{{page.title}}](https://leetcode.com/problems/insert-interval/){:target="_blank"}

    Given a set of non-overlapping intervals, insert a new interval into the intervals
    (merge if necessary).

    You may assume that the intervals were initially sorted according to their start times.

    Example 1:

    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

    Example 2:

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

```java
public int[][] insert(int[][] intervals, int[] newInterval) {
    List<int[]> result = new ArrayList<>();
    int i = 0;
    while(i < intervals.length && intervals[i][1] < newInterval[0]) {
        result.add(intervals[i++]);
    }
    result.add(newInterval);
    while(i < intervals.length && intervals[i][0] <= result.get(result.size()-1)[1]) {
        int[] pre = result.get(result.size()-1), curr = intervals[i];
        pre[1] = Math.max(pre[1], curr[1]);
        pre[0] = Math.min(pre[0], curr[0]);
        i++;
    }
    while(i < intervals.length) result.add(intervals[i++]);
    int[][] lists = new int[result.size()][2];
    for(int j = 0; j < lists.length; j++) lists[j] = result.get(j);
    return lists;
}
```
