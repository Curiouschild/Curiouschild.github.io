---
title:  "200. Number of Islands"
date:   2019-3-5 20:18:53 +0930
categories: Leetcode
tags: Graph UnionFind DFS
---

[200. Number of Islands](https://leetcode.com/problems/number-of-islands/){:target="_blank"}

    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally
    or vertically. You may assume all four edges of the grid are all surrounded by water.

1. DFS

```java
int[] xs = {0,0,1,-1};
int[] ys = {1,-1,0,0};
public int numIslands(char[][] grid) {
    int result = 0;
    for(int i = 0; i < grid.length; i++) {
        for(int j = 0; j < grid[0].length; j++) {
            if(grid[i][j] == '1') {
                result++;
                dfs(grid, i, j);
            }
        }
    }
    return result;
}

public void dfs(char[][] grid, int i, int j) {
    grid[i][j] = '#';
    for(int k = 0; k < 4; k++) {
        int nx = i + xs[k], ny = j + ys[k];
        if(nx >= 0 && nx < grid.length && ny >=0 && ny < grid[0].length && grid[nx][ny] == '1') {
            dfs(grid, nx, ny);
        }
    }
}
```

2. Union Find with rank

```java

class UnionFind {
    int[] arr;
    int[] rank;
    int count;
    public UnionFind(char[][] grid) {
        int n = grid.length, m = grid[0].length;
        arr = new int[n * m];
        rank = new int[n * m];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(grid[i][j] == '1') {
                    arr[i*m+j] = i*m+j;
                    rank[i*m+j] = 1;
                    count++;
                }
            }
        }
    }
    public int find(int x) {
        if(arr[x] != x) {
            return find(arr[x]);
        }
        return x;
    }
    public void union(int x1, int x2) {
        int r1 = find(x1), r2 = find(x2);
        if(r1 != r2) {
            count--;
            if(rank[r1] >= rank[r2]) {
                arr[r2] = r1;
                rank[r1] += rank[r2];
            } else {
                arr[r1] = r2;
                rank[r2] += rank[r1];
            }
        }
    }
}

int[] xs = {0,0,1,-1};
int[] ys = {1,-1,0,0};
public int numIslands(char[][] grid) {
    if(grid.length == 0 || grid[0].length == 0) return 0;
    UnionFind uf = new UnionFind(grid);
    int numPerRow = grid[0].length;
    for(int i = 0; i < grid.length; i++) {
        for(int j = 0; j < grid[0].length; j++) {
            if(grid[i][j] == '1') {
                for(int k = 0; k < 4; k++) {
                   int nx = i + xs[k], ny = j + ys[k];
                   if(nx >= 0 && nx < grid.length && ny >=0 && ny < grid[0].length && grid[nx][ny] == '1') {
                        uf.union(i*numPerRow+j, nx*numPerRow+ny);
                   }
                }
            }
        }
    }
    return uf.count;
}
```
