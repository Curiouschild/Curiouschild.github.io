---
title:  "680. Valid Palindrome II"
date:   2019-05-03 21:49:00 +0930
categories: Leetcode
tags: Hard PriorityQueue
---

[{{page.title}}](https://leetcode.com/problems/trapping-rain-water-ii/){:target="_blank"}


    Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

    Note:

    Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

    Example:

    Given the following 3x6 height map:
    [
      [1,4,3,1,3,2],
      [3,2,1,3,2,4],
      [2,3,3,2,3,1]
    ]

    Return 4.

    The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.

![img1](/img/posts/trapping-rain-water-ii-1.png)

    After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

![img2](/img/posts/trapping-rain-water-ii-2.png)


* 地方包围中央，不断垒高墙

build a wall surround the matrix, and push the boundary toward the center. The forwarding direction
is the neighbors of the lowest point of the wall, because the water volume of these points are available.

```java
class Solution {
    public int trapRainWater(int[][] matrix) {
        if(matrix == null || matrix.length == 0 || matrix[0] == null || matrix[0].length == 0) return 0;
        PriorityQueue<int[]> q = new PriorityQueue<>((x,y)->(matrix[x[0]][x[1]]-matrix[y[0]][y[1]]));
        boolean[][] visited = new boolean[matrix.length][matrix[0].length];
        for(int i = 0; i < matrix.length; i++) {
            q.offer(new int[]{i, 0});
            q.offer(new int[]{i, matrix[0].length-1});
            visited[i][0] = true;
            visited[i][matrix[0].length-1] = true;
        }
        for(int j = 1; j < matrix[0].length-1; j++) {
            q.offer(new int[]{0, j});
            q.offer(new int[]{matrix.length-1, j});
            visited[0][j] = true;
            visited[matrix.length-1][j] = true;
        }
        int max = 0; // monotonic increase
                    // the point with the lowest height of the wall
        int result = 0;
        int[] xs = {0,0,1,-1}, ys = {1,-1,0,0};
        while(!q.isEmpty()) {
            int[] n = q.poll();
            int lowest = matrix[n[0]][n[1]];
            if(lowest > max) max = lowest;
            for(int k = 0; k < 4; k++) {
                int i = xs[k] + n[0], j = ys[k] + n[1];
                if(i < 0 || j < 0 || i >= matrix.length || j >= matrix[0].length || visited[i][j]) continue;
                int neighbor = matrix[i][j];
                if(neighbor < max) result += max-neighbor;
                q.offer(new int[]{i, j});
                visited[i][j] = true;
            }
        }
        return result;
    }
}
```
