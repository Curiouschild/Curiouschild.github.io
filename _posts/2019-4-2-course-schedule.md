---
title:  "207. Course Schedule"
date:   2019-4-2 21:01:00 +0930
categories: Leetcode
tags: TopographicSorting
---

[{{page.title}}](https://leetcode.com/problems/course-schedule/){:target="_blank"}

    There are a total of n courses you have to take, labeled from 0 to n-1.

    Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
    which is expressed as a pair: [0,1]

    Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish
    all courses?

    Example 1:

    Input: 2, [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take.
                 To take course 1 you should have finished course 0. So it is possible.

    Example 2:

    Input: 2, [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take.
                 To take course 1 you should have finished course 0, and to take course 0 you should
                 also have finished course 1. So it is impossible.


```java
public boolean canFinish(int n, int[][] ps) {
    int[] in = new int[n];
    HashSet<Integer>[] out = new HashSet[n];
    for(int i = 0; i < n; i++)
        out[i] = new HashSet<Integer>();
    for(int[] p : ps) {
        in[p[0]]++;
        out[p[1]].add(p[0]);
    }

    ArrayDeque<Integer> q = new ArrayDeque<>();
    for(int i = 0; i < n; i++)
        if(in[i] == 0)
            q.offer(i);

    int cnt = 0;
    while(!q.isEmpty()) {
        int i = q.poll();
        System.out.print(i);
        cnt++;
        for(int j : out[i]) {
            in[j]--;
            if(in[j] == 0)
                q.offer(j);
        }
    }
    return cnt == n;
}
```
