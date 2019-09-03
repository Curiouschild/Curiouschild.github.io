---
title:  "947. Most Stones Removed with Same Row or Column"
date:   2019-05-11 11:10:00 +0930
categories: Leetcode
tags: Medium UnionFind DFS
---

[{{page.title}}](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/){:target="_blank"}


    On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most
    one stone.

    Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

    What is the largest possible number of moves we can make?



    Example 1:

    Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    Output: 5

    Example 2:

    Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    Output: 3

    Example 3:

    Input: stones = [[0,0]]
    Output: 0

* UnionFind

```java

public int removeStones(int[][] stones) {
    UnionFind uf = new UnionFind(stones);
    for(int[] s : stones) {
        uf.union(s[0], s[1]+10000);
    }
    int cnt = 0;
    for(int i = 0; i < 20000; i++) {
        if(uf.arr[i] == i) cnt++;
    }
    return stones.length - cnt;
}

class UnionFind {
    int[] arr;
    public UnionFind(int[][] stones) {
        arr = new int[20000];
        Arrays.fill(arr, -1);
        for(int[] s : stones) {
            int x = s[0], y = s[1];
            arr[x] = x;
            arr[y+10000] = y+10000;
        }
    }
    public int find(int x) {
        if(arr[x] != x) {
            arr[x] = find(arr[x]);
        }
        return arr[x];
    }
    public void union(int x, int y) {
        int a = find(x), b = find(y);
        if(a != b) {
            arr[a] = b;
        }
    }
}
```

* DFS

```java

public int removeStones(int[][] stones) {
    ArrayList<int[]>[] xs = new ArrayList[10000], ys = new ArrayList[10000];
    for(int[] s : stones) {
        int x = s[0], y = s[1];
        if(xs[x] == null) xs[x] = new ArrayList<>();
        if(ys[y] == null) ys[y] = new ArrayList<>();
        xs[x].add(s);
        ys[y].add(s);
    }
    HashSet<int[]> visited = new HashSet<int[]>();
    int cnt = 0;
    for(int[] s : stones) {
        if(!visited.contains(s)) {
            cnt++;
            visited.add(s);
            mark(s, visited, xs, ys);
        }
    }
    return stones.length - cnt;
}
public void mark(int[] curr, HashSet<int[]> visited, ArrayList<int[]>[] xs, ArrayList<int[]>[] ys) {
    int x = curr[0], y = curr[1];
    for(int[] neighbor : xs[x]) {
        if(!visited.contains(neighbor)) {
            visited.add(neighbor);
            mark(neighbor, visited, xs, ys);
        }
    }
    for(int[] neighbor : ys[y]) {
        if(!visited.contains(neighbor)) {
            visited.add(neighbor);
            mark(neighbor, visited, xs, ys);
        }
    }
}
```
