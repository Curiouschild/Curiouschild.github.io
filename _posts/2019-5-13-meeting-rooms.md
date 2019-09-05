---
title:  "252. Meeting Rooms"
date:   2019-05-13 13:08:00 +0930
categories: Leetcode
tags: Easy Sorting
---

[{{page.title}}](https://leetcode.com/problems/meeting-rooms/){:target="_blank"}


    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
    determine if a person could attend all meetings.

    Example 1:

    Input: [[0,30],[5,10],[15,20]]
    Output: false

    Example 2:

    Input: [[7,10],[2,4]]
    Output: true


```java

public boolean canAttendMeetings(int[][] intervals) {
    Arrays.sort(intervals, (a,b)->(Integer.compare(a[0], b[0])));
    for(int i = 1; i < intervals.length; i++) {
        if(intervals[i-1][1] > intervals[i][0]) return false;
    }
    return true;
}
```
