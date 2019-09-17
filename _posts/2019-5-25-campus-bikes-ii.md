---
title:  "1066. Campus Bikes II"
date:   2019-05-25 14:15:00 +0930
categories: Leetcode
tags: Medium Array Backtrack
---

[{{page.title}}](https://leetcode.com/problems/campus-bikes-ii/){:target="_blank"}

    On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is
    a 2D coordinate on this grid.

    We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and
    their assigned bike is minimized.

    The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

    Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

    Example 1:

    Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
    Output: 6
    Explanation:
    We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.

    Note:

        0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000
        All worker and bike locations are distinct.
        1 <= workers.length <= bikes.length <= 10

* DP with state mask

```java 
public int assignBikes(int[][] workers, int[][] bikes) {
    int N = workers.length, M = bikes.length;
    int[][] dp = new int[N+1][1<<M];
    for(int i = 1; i < dp.length; i++)
        Arrays.fill(dp[i], 2000 * 10);
    int result = Integer.MAX_VALUE;
    for(int i = 1; i < dp.length; i++) {
        for(int s = 0; s < dp[0].length; s++) {
            for(int j = 0; j < M; j++) {
                if(((1 << j) & s) != 0) { // find a 1 to remove
                    int p = (1 << j) ^ s; // previous state; reomve a 1 from current state --> remove a used bike
                    int d = Math.abs(workers[i-1][0]-bikes[j][0]) + Math.abs(workers[i-1][1]-bikes[j][1]);
                    dp[i][s] = Math.min(dp[i][s], dp[i-1][p] + d);
                    if(i == dp.length-1) // all N worker, time to record the result
                        result = Math.min(result, dp[i][s]);
                }
            }
        }
    }
    return result;
}
```

* Backtrack with pruning


```java

int result = Integer.MAX_VALUE;
public int assignBikes(int[][] workers, int[][] bikes) {
    backtrack(workers, bikes, 0, new boolean[bikes.length], 0);
    return result;
}
public void backtrack(int[][] ws, int[][] bs, int index, boolean[] vb, int sum) {
    if(index == ws.length) {
        result = Math.min(result, sum);
        return;
    }
    if(sum >= result) return; // pruning
    for(int i = 0; i < bs.length; i++) {
        if(vb[i]) continue;
        vb[i] = true;
        int d = Math.abs(ws[index][0]-bs[i][0]) + Math.abs(ws[index][1]-bs[i][1]);
        backtrack(ws, bs, index+1, vb, sum+d);
        vb[i] = false;
    }
}
```
