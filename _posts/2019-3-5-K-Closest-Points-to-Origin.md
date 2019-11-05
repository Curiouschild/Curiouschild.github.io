---
title:  "973. K Closest Points to Origin"
date:   2019-3-5 21:20:51 +0930
categories: Leetcode
tags: PriorityQueue QuickSelect DivideAndConquer
---

[{{page.title}}](https://leetcode.com/problems/k-closest-points-to-origin/){:target="_blank"}

    We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

    (Here, the distance between two points on a plane is the Euclidean distance.)

    You may return the answer in any order.  The answer is guaranteed to be unique
    (except for the order that it is in.)

* QuickSelect
  - O(N)

```java

public int[][] kClosest(int[][] points, int K) {
    quickSelect(points, K, 0, points.length-1);
    int[][] result = new int[K][2];
    for(int i = 0; i < K; i++) result[i] = points[i];
    return result;
}

public void quickSelect(int[][] points, int K, int start, int end) {
    if(start > end) return;
    int pivot = getDS(points[start]);
    int i = start + 1, j = i;
    while(i <= end) {
        int d = getDS(points[i]);
        if(d <= pivot) {
            swap(points, i, j);
            j++;
        }
        i++;
    }
    j--;
    swap(points, start, j);
    if(K == j+1) return;
    else if(K > j+1) {
        quickSelect(points, K, j+1, end);
    } else {
        quickSelect(points, K, start, j);
    }
}

public void swap(int[][] points, int i, int j) {
    int[] temp = points[i];
    points[i] = points[j];
    points[j] = temp;
}

public int getDS(int[] p) {
    return p[0] * p[0] + p[1] * p[1];
}

```

* PriorityQueue
  - NlogK
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
