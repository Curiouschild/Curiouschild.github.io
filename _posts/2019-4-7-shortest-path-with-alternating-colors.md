---
title:  "1129. Shortest Path with Alternating Colors"
date:   2019-4-7 23:52:00 +0930
categories: Leetcode
tags: DataStructure Tree
---

[{{page.title}}](https://leetcode.com/problems/shortest-path-with-alternating-colors/){:target="_blank"}

    Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is
    either red or blue, and there could be self-edges or parallel edges.

    Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly,
    each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

    Return an array answer of length n, where each answer[X] is the length of the shortest path
    from node 0 to node X such that the edge colors alternate along the path (or -1 if such a
    path doesn't exist).


    Example 1:

    Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
    Output: [0,1,-1]


```java

public static final int RED = 0, BLUE = 1;

   public int[] shortestAlternatingPaths(int n, int[][] red_edges, int[][] blue_edges) {
       int[] color = new int[n], result = new int[n];
       Arrays.fill(result, -1);
       result[0] = 0;

       HashSet<Integer>[][] graph = new HashSet[2][n];
       for(int i = 0; i < n; i++) {
           graph[RED][i] = new HashSet<>();
           graph[BLUE][i] = new HashSet<>();
       }

       for(int[] e : red_edges) graph[RED][e[0]].add(e[1]);
       for(int[] e : blue_edges) graph[BLUE][e[0]].add(e[1]);
       search(result, RED, graph);

       for(int[] e : red_edges) graph[RED][e[0]].add(e[1]);
       for(int[] e : blue_edges) graph[BLUE][e[0]].add(e[1]);
       search(result, BLUE, graph);

       return result;
   }

   public void search(int[] result, int color, HashSet<Integer>[][] graph) {
       ArrayDeque<Integer> q = new ArrayDeque<>();
       q.offer(0);
       int step = 0;
       while(!q.isEmpty()) {
           int size = q.size();
           step++;
           for(int k = 0; k < size; k++) {
               int from = q.poll();
               for(int to : graph[color][from]) {
                   q.offer(to);
                   result[to] = result[to] == -1 ? step : Math.min(step, result[to]);
               }
               graph[color][from] = new HashSet<>();
           }
           color = color == RED ? BLUE : RED;
       }
   }

```
