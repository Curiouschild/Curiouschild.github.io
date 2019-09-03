---
title:  "743. Network Delay Time"
date:   2019-05-11 13:22:00 +0930
categories: Leetcode
tags: Medium PriorityQueue MST Graph
---

[{{page.title}}](https://leetcode.com/problems/network-delay-time/){:target="_blank"}

    There are N network nodes, labelled 1 to N.

    Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v
    is the target node, and w is the time it takes for a signal to travel from source to target.

    Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If
    it is impossible, return -1.

    Example 1:

    Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
    Output: 2

![img](/img/posts/network-delay-time.png)

    Note:
        N will be in the range [1, 100].
        K will be in the range [1, N].
        The length of times will be in the range [1, 6000].
        All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

* MST

```java

public int networkDelayTime(int[][] times, int N, int K) {
    int result = 0;
    ArrayList<int[]>[] ns = new ArrayList[N+1];
    for(int[] t : times) {
        if(ns[t[0]] == null) ns[t[0]] = new ArrayList<>();
        ns[t[0]].add(new int[] {t[1], t[2], 0});
    }
    PriorityQueue<int[]> q = new PriorityQueue<>((a,b)->(a[2]-b[2]));
    boolean[] visited = new boolean[N+1];
    q.offer(new int[] {K, 0, 0});
    int vCnt = 0;
    while(!q.isEmpty()) {
        int[] c = q.poll();
        if(visited[c[0]]) continue;
        visited[c[0]] = true;
        result = c[2];
        vCnt++;
        if(vCnt == N) break;
        if(ns[c[0]] == null) continue;
        for(int[] next : ns[c[0]]) {
            next[2] = c[2] + next[1]; // accumulative time
            q.offer(next);
        }
    }
    return vCnt == N ? result : -1;
}
```
