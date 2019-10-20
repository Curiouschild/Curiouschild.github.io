---
title:  "meeting-scheduler"
date:   2019-06-21 20:30:00 +0930
categories: Leetcode
tags: Medium Interval
---

[{{page.title}}](https://leetcode.com/problems/meeting-scheduler/){:target="_blank"}

    Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration,
    return the earliest time slot that works for both of them and is of duration duration.

    If there is no common time slot that satisfies the requirements, return an empty array.

    The format of a time slot is an array of two elements [start, end] representing an inclusive time range
    from start to end.

    It is guaranteed that no two availability slots of the same person intersect with each other. That is, for
    any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 >
    end1.

    Example 1:

    Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
    Output: [60,68]

    Example 2:

    Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
    Output: []

    Constraints:

        1 <= slots1.length, slots2.length <= 10^4
        slots1[i].length, slots2[i].length == 2
        slots1[i][0] < slots1[i][1]
        slots2[i][0] < slots2[i][1]
        0 <= slots1[i][j], slots2[i][j] <= 10^9
        1 <= duration <= 10^6

* Two pointers

```java

public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
    Arrays.sort(slots1, (a,b)->(a[0]-b[0]));
    Arrays.sort(slots2, (a,b)->(a[0]-b[0]));
    int i = 0, j = 0;
    while(i < slots1.length && j < slots2.length) {
        int[] s1 = slots1[i], s2 = slots2[j];
        int l1 = s1[0], r1 = s1[1], l2 = s2[0], r2 = s2[1];
        int d = Math.min(r1, r2) - Math.max(l1, l2);
        if(d >= duration) {
            return Arrays.asList(Math.max(l1, l2), Math.max(l1, l2)+duration);
        }
        if(r1 < r2) {
            i++;
        } else {
            j++;
        }
    }
    return Arrays.asList();
}
```

* Preprocessing and priorityqueue

```java
public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
    PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparing(a -> a[0]));
    for (int[] s : slots1) if (s[1] - s[0] >= duration) pq.offer(s);
    for (int[] s : slots2) if (s[1] - s[0] >= duration) pq.offer(s);
    while (pq.size() > 1) {
        if (pq.poll()[1] >= pq.peek()[0] + duration)
            return Arrays.asList(pq.peek()[0], pq.peek()[0] + duration);
    }
    return Arrays.asList();
}
```
