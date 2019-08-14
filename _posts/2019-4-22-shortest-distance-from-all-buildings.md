---
title:  "317. Shortest Distance from All Buildings"
date:   2019-4-22 23:40:00 +0930
categories: Leetcode
tags: Matrix
---

[{{page.title}}](https://leetcode.com/problems/shortest-distance-from-all-buildings/){:target="_blank"}



* Brutal BFS starting from every 0

A good comment on why don't start at 1
"Does anyone want to ask Why don't we start from '0'? This is also what I am thinking. At the first glance, the time complexity of starting from buildings O(B*M*N) (B: # of buildings) and starting from empty places O(E*M*N) (E: # of empty places) might be the same. If in an interview, I think we can ask for clarification. If the empty places are far more than buildings, ex. we have 1 million empty places and only 1 building, starting from building is better. So it depends on how many empty places and buildings that we have. We are not going to say this way or that way is better, but it's a kind of trade-off."
https://leetcode.com/problems/shortest-distance-from-all-buildings/discuss/76891/Java-solution-with-explanation-and-time-complexity-analysis/216592

```java

class Solution {
    public int shortestDistance(int[][] grid) {
        int shortest = Integer.MAX_VALUE;
        int ones = 0;
        for(int i = 0; i < grid.length; i++) {
            for(int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == 1) ones++;
            }
        }
        for(int i = 0; i < grid.length; i++) {
            for(int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == 0) {
                    int distance = bfs(grid, i, j, ones);
                    shortest = Math.min(shortest, distance);
                }
            }
        }
        return shortest == Integer.MAX_VALUE ? -1 : shortest;
    }
    int[] xs = {0,0,1,-1}, ys = {1,-1,0,0};
    public int bfs(int[][] grid, int i, int j, int ones) {
        ArrayDeque<Integer> xq = new ArrayDeque<>(), yq = new ArrayDeque<>();
        xq.offer(i);
        yq.offer(j);
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        visited[i][j] = true;
        int distance = 0;
        int level = 0;
        int oneCnt = 0;
        while(!xq.isEmpty()) {
            int size = xq.size();
            level++;
            for(int k = 0; k < size; k++) {
                int x = xq.poll(), y = yq.poll();
                for(int p = 0; p < 4; p++) {
                    int nx = xs[p] + x, ny = ys[p] + y;
                    if(nx >= 0 && ny >= 0 && nx < grid.length && ny < grid[0].length && !visited[nx][ny] && grid[nx][ny] != 2) {
                        visited[nx][ny] = true;
                        if(grid[nx][ny] == 1) {
                            distance += level;
                            oneCnt++;
                        } else {
                            xq.offer(nx);
                            yq.offer(ny);
                        }
                    }
                }
            }
        }
        return oneCnt == ones ? distance : Integer.MAX_VALUE;
    }
  }
```
