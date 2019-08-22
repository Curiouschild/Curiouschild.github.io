---
title:  "785. Is Graph Bipartite?"
date:   2019-4-28 18:58:00 +0930
categories: Leetcode
tags: Medium Graph BFS
---

[{{page.title}}](https://leetcode.com/problems/is-graph-bipartite/){:target="_blank"}

    Given an undirected graph, return true if and only if it is bipartite.

    Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B
    such that every edge in the graph has one node in A and another node in B.

    The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes
    i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or
    parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

    Example 1:
    Input: [[1,3], [0,2], [1,3], [0,2]]
    Output: true
    Explanation:
    The graph looks like this:
    0----1
    |    |
    |    |
    3----2
    We can divide the vertices into two groups: {0, 2} and {1, 3}.

    Example 2:
    Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
    Output: false
    Explanation:
    The graph looks like this:
    0----1
    | \  |
    |  \ |
    3----2
    We cannot find a way to divide the set of nodes into two independent subsets.



* BFS

```java
class Solution {
    public boolean isBipartite(int[][] graph) {
        boolean[] visited = new boolean[graph.length];
        for(int i = 0; i < graph.length; i++) {
            if(visited[i]) continue;
            if(!checkSubGraph(graph, visited, i))
                return false;
        }
        return true;
    }
    public boolean checkSubGraph(int[][] graph, boolean[] visited, int start) {
        HashSet[] sets = new HashSet[2];
        sets[0] = new HashSet<Integer>();
        sets[1] = new HashSet<Integer>();
        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.offer(start);
        sets[0].add(start);
        boolean[][] used = new boolean[graph.length][graph.length];
        int currSet = 0, nextSet = 1;
        while(!q.isEmpty()) {
            int size = q.size();
            for(int k = 0; k < size; k++) {
                int i = q.poll();
                visited[i] = true;
                for(int j : graph[i]) {
                    if(!used[i][j]) {
                        if(sets[currSet].contains(j)) return false;
                        used[i][j] = true;
                        used[j][i] = true;
                        q.offer(j);
                        sets[nextSet].add(j);
                    }
                }
            }
            currSet = currSet == 1 ? 0 : 1;
            nextSet = currSet == 1 ? 0 : 1;
        }
        return true;
    }
  }
```
