---
title:  "1192. Critical Connections in a Network"
date:   2019-06-18 12:20:00 +0930
categories: Leetcode
tags: Hard Graph
---

[{{page.title}}](https://leetcode.com/problems/critical-connections-in-a-network/){:target="_blank"}

    There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a
    network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach
    any other server directly or indirectly through the network.

    A critical connection is a connection that, if removed, will make some server unable to reach some other
    server.

    Return all critical connections in the network in any order.

    Example 1:

    Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
    Output: [[1,3]]
    Explanation: [[3,1]] is also accepted.

    Constraints:

        1 <= n <= 10^5
        n-1 <= connections.length <= 10^5
        connections[i][0] != connections[i][1]
        There are no repeated connections.

```java

class Solution {
    List<List<Integer>> r;
    int[] id;
    int[] low;
    boolean[] onStack;
    Stack<Integer> stack;
    List<Integer>[] graph;
    int n;
    int index;
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        this.n = n;
        id = new int[n];
        Arrays.fill(id, -1);
        low = new int[n];
        onStack = new boolean[n];
        stack = new Stack<>();
        r = new ArrayList<>();

        graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        // build graph
        for (int i = 0; i < connections.size(); i++) {
            int from = connections.get(i).get(0), to = connections.get(i).get(1);
            graph[from].add(to);
            graph[to].add(from);
        }

        dfs(0, -1);
        return r;
    }

    public void dfs(int i, int prev) {
        stack.push(i);
        onStack[i] = true;
        low[i] = id[i] = index++;
        for(int j : graph[i]) {
            if(id[j] == -1) dfs(j, i);
            if(j != prev && onStack[j])
                low[i] = Math.min(low[i], low[j]);
        }
        // find a strongly connected part
        if(low[i] == id[i]) {
            while(true) {
                int p = stack.pop();
                onStack[p] = false;
                if(p == i) break; // end of current subgraph
            }
            if(prev!= -1) {
                r.add(Arrays.asList(i, prev));
            }
        }
    }

}
```
