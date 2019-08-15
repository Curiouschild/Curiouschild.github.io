---
title:  "547. Friend Circles"
date:   2019-4-17 21:35:00 +0930
categories: Leetcode
tags: BFS
---

[{{page.title}}](https://leetcode.com/problems/friend-circles/){:target="_blank"}

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input:
[[1,1,0],
[1,1,0],
[0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.

Example 2:

Input:
[[1,1,0],
[1,1,1],
[0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

Note:

 N is in range [1,200].
 M[i][i] = 1 for all students.
 If M[i][j] = 1, then M[j][i] = 1.


* UnionFind

```java
class UnionFind {
    int[] p;
    int cnt;
    public UnionFind(int n) {
        p = new int[n];
        for(int i = 0; i < n; i++) p[i] = i;
        cnt = n;
    }
    public int find(int x) {
        if(p[x] != x) p[x] = find(p[x]);
        return p[x];
    }
    public void union(int x, int y) {
        int i = find(x), j = find(y);
        if(i != j) {
            cnt--;
            p[i] = j;
        }
    }
}
public int findCircleNum(int[][] M) {
    UnionFind uf = new UnionFind(M.length);
    for(int i = 0; i < M.length; i++) {
        for(int j = i+1; j< M.length; j++) {
            if(M[i][j] == 1) uf.union(i, j);
        }
    }
    return uf.cnt;
}

public int findCircleNumDFS(int[][] M) {
    HashSet<Integer> visited = new HashSet<>();
    int cnt = 0;
    for(int i = 0; i < M.length; i++) {
        if(visited.contains(i)) continue;
        visited.add(i);
        cnt++;
        dfs(M, i, visited);
    }
    return cnt;
}
```
* DFS
i has been visited if M[i][i] == 1

```java
public int findCircleNum(int[][] M) {
    int ans = 0;
    for(int i = 0; i < M.length; i++) {
        ans += mark(M, i);
    }
    return ans;
}

public int mark(int[][] M, int i) {
    if(M[i][i] == 0) return 0;
    M[i][i] = 0;
    for(int j = 0; j < M.length; j++) {
        if(M[i][j] == 1) mark(M, j);
    }
    return 1;
}
```
