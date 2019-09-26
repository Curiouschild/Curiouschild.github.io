---
title:  "787. Cheapest Flights Within K Stops"
date:   2019-05-01 23:59:00 +0930
categories: Leetcode
tags: Medium DFS Graph Dijkstra
---

[{{page.title}}](https://leetcode.com/problems/cheapest-flights-within-k-stops/){:target="_blank"}

    There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

    Now given all the cities and flights, together with starting city src and the destination dst, your task is
    to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

    Example 1:
    Input:
    n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0, dst = 2, k = 1
    Output: 200
    Explanation:
    The graph looks like this:


    The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

    Example 2:
    Input:
    n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0, dst = 2, k = 0
    Output: 500
    Explanation:
    The graph looks like this:


    The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

    Note:

        The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
        The size of flights will be in range [0, n * (n - 1) / 2].
        The format of each flight will be (src, dst, price).
        The price of each flight will be in the range [1, 10000].
        k is in the range of [0, n - 1].
        There will not be any duplicated flights or self cycles.



The first idea came to my mind is dijkstra + limit.
I did implement a dijkstra, but fail to record the steps from the src to each node because my code overwrote
the steps when arrived at a node from different sources (some nodes exceed the step limits).

* Failed Dijkstra

```java
public int findCheapestPriceFailed(int n, int[][] flights, int src, int dst, int K) {
    ArrayList<int[]>[] to = new ArrayList[n];
    for(int i = 0; i < n; i++) to[i] = new ArrayList<int[]>();
    for(int[] f : flights) {
        to[f[0]].add(new int[] {f[1], f[2]});
    }
    int[] costs = new int[n];
    Arrays.fill(costs, Integer.MAX_VALUE);
    costs[src] = 0;
    int[] steps = new int[n];
    PriorityQueue<Integer> q = new PriorityQueue<>((x,y)->(costs[x]-costs[y]));
    q.offer(src);
    while(!q.isEmpty() && q.peek() != dst) {
        int curr = q.poll();
        if(steps[curr] > K) continue;
        for(int[] f : to[curr]) {
            costs[f[0]] = Math.min(costs[f[0]], costs[curr]+f[1]); // update costs for next nodes
            steps[f[0]] = steps[curr] + 1; // !here comes the bug...
            q.offer(f[0]);
        }
    }
    return costs[dst] == Integer.MAX_VALUE ? -1 : costs[dst];
}
```

* Finally I get the correct solution. The key is put all the related information (steps, total costs, and stop id) into the pq

```java

public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
    ArrayList<int[]>[] to = new ArrayList[n]; // adjacent list: src -> (dsts and costs)s
    for(int i = 0; i < n; i++) to[i] = new ArrayList<int[]>();
    for(int[] f : flights) to[f[0]].add(new int[] {f[1], f[2]});
    PriorityQueue<int[]> q = new PriorityQueue<>((x,y)->(x[2]-y[2]));
    q.offer(new int[] {src, 0, 0});
    while(!q.isEmpty()) {
        int[] curr = q.poll();
        if(curr[0] == dst) return curr[2];
        if(curr[1] > K) continue;
        for(int[] next : to[curr[0]]) { // next: {nextStop, cost of the edge}
            q.offer(new int[]{next[0], 1+curr[1], next[1]+curr[2]});
        }
    }
    return -1;
}
```

* A more understandable version

```java

public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
    if(src == dst) return 0;
    ArrayList<int[]>[] graph = new ArrayList[n];
    for(int i = 0; i < graph.length; i++)
        graph[i] = new ArrayList<>();
    for(int[] f : flights)
        graph[f[0]].add(new int[]{f[1],f[2]});
    PriorityQueue<City> q = new PriorityQueue<>((a,b)->(a.cost-b.cost));
    for(int[] f : graph[src])
        q.offer(new City(f[0], 0, f[1]));
    while(!q.isEmpty()) {
        City curr = q.poll();
        if(curr.index == dst) {
            return curr.cost;
        } else if(curr.stop < K) {
            for(int[] f : graph[curr.index])
                q.offer(new City(f[0], curr.stop+1, curr.cost+f[1]));
        }
    }
    return -1;
}

class City {
    int index;
    int stop;
    int cost;
    public City(int index, int stop, int cost) {
        this.index = index;
        this.stop = stop;
        this.cost = cost;
    }
}

```

* DFS with early exit accepted but extremely slow

This trash might be what I came up with in an interview...

```java
class Solution {
    // dijkstra with limit steps
    int result = Integer.MAX_VALUE;
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        ArrayList<int[]>[] to = new ArrayList[n];
        for(int i = 0; i < n; i++) to[i] = new ArrayList<int[]>();
        for(int[] f : flights) {
            to[f[0]].add(new int[] {f[1], f[2]});
        }
        boolean[] visited = new boolean[n];
        find(dst, K, src, 0, to, 0, visited);
        return result == Integer.MAX_VALUE ? -1 : result;
    }

    public void find(int dst, int K, int curr, int step, ArrayList<int[]>[] to, int cost, boolean[] visited) {
        if(cost >= result) return;
        if(step > K+1) return;
        if(curr == dst) {
            result = Math.min(result, cost);
            return;
        }
        for(int[] f : to[curr]) {
            if(visited[f[0]]) continue;
            visited[f[0]] = true;
            find(dst, K, f[0], step+1, to, cost+f[1], visited);
            visited[f[0]] = false;
        }
    }
```
