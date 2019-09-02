---
title:  "253. Meeting Rooms II"
date:   2019-3-7 08:30:31 +0930
categories: Leetcode
tags: PriorityQueue Sort
---

[{{page.title}}](https://leetcode.com/problems/meeting-rooms-ii/){:target="_blank"}

    Given an array of meeting time intervals consisting of
    start and end times [[s1,e1],[s2,e2],...] (si < ei),
    find the minimum number of conference rooms required.

    Example 1:

    Input: [[0, 30],[5, 10],[15, 20]]
    Output: 2


Consider a ended room first when trying to start a new meeting.

* PriorityQueue

```java
public int minMeetingRoomsPriorityQueue(int[][] intervals) {
    PriorityQueue<int[]> q = new PriorityQueue<>(new Comparator<int[]>() {
        public int compare(int[] x, int[] y) {
            return Integer.compare(x[1], y[1]);
        }
    });
    Arrays.sort(intervals, new Comparator<int[]>(){
        public int compare(int[] x, int[] y) {
            return Integer.compare(x[0], y[0]);
        }
    });
    for(int[] i : intervals) {
        if(q.isEmpty()) q.offer(i);
        else {
            if(q.peek()[1] <= i[0]) q.poll();
            q.offer(i);
        }
    }
    return q.size();
}
```

* Two sorted Arrays

```java
public int minMeetingRoomsArraySort(int[][] intervals) {
    int[] starts = new int[intervals.length], ends = new int[intervals.length];
    for(int i = 0; i < intervals.length; i++) {
        starts[i] = intervals[i][0];
        ends[i] = intervals[i][1];
    }
    Arrays.sort(starts);
    Arrays.sort(ends);
    int s = 0, e = 0, cnt = 0;
    while(s < starts.length) {
        if(starts[s] >= ends[e]) {
            cnt--;
            e++;
        }
        s++;
        cnt++;
    }
    return cnt;
}
```
