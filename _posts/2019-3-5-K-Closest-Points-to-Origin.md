---
title:  "973. K Closest Points to Origin"
date:   2019-3-5 021:20:51 +0930
categories: Leetcode
tags: PriorityQueue
---

[{{page.title}}](https://leetcode.com/problems/k-closest-points-to-origin/){:target="_blank"}

    We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

    (Here, the distance between two points on a plane is the Euclidean distance.)

    You may return the answer in any order.  The answer is guaranteed to be unique
    (except for the order that it is in.)

```java
public int[][] kClosest(int[][] points, int K) {
    PriorityQueue<int[]> q = new PriorityQueue<>(new Comparator<int[]>() {
        public int compare(int[] p1, int[] p2) {
            return getDS(p2) - getDS(p1);
        }
    });
    for(int[] p : points) {
        if(q.size() < K) q.offer(p);
        else {
            int[] top = q.peek();
            if(getDS(top) > getDS(p)) {
                q.poll();
                q.offer(p);
            }
        }
    }
    int[][] r = new int[K][];
    for(int i = 0; i < K; i++) r[i] = q.poll();
    return r;
}

public int getDS(int[] p) {
    return p[0] * p[0] + p[1] * p[1];
}

```
