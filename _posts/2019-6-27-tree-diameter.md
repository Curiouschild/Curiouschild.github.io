---
title:  "1245. Tree Diameter"
date:   2019-06-27 15:15:00 +0930
categories: Leetcode
tags: Medium DFS Tree
---

[{{page.title}}](https://leetcode.com/problems/tree-diameter/){:target="_blank"}

    Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

    The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

    Example 1:

    Input: edges = [[0,1],[0,2]]
    Output: 2
    Explanation:
    A longest path of the tree is the path 1 - 0 - 2.

    Example 2:

    Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
    Output: 4
    Explanation:
    A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.

    Constraints:

        0 <= edges.length < 10^4
        edges[i][0] != edges[i][1]
        0 <= edges[i][j] <= edges.length
        The given edges form an undirected tree.

* DP

```java

public int minimumMoves(int[] arr) {
    int N = arr.length;
    int[][] dp = new int[N+1][N];
    for(int w = 1; w <= N; w++) { // w: window size
        for(int i = 0; i+w-1 < N; i++) {
            int j = i+w-1;
            if(w == 1) {
                dp[i][j] = 1;
            } else {
                dp[i][j] = 1 + dp[i+1][j]; // remove i
                if(arr[i] == arr[i+1]) {
                    dp[i][j] = Math.min(dp[i][j], 1 + dp[i+2][j]); // remove i and i+1
                }
                for(int k = i+2; k <= j; k++) {
                    if(arr[k] == arr[i]) { // remove i and k alone with substring between them
                        dp[i][j] = Math.min(dp[i][j], dp[i+1][k-1] + dp[k+1][j]);
                    }
                }
            }
        }
    }
    return dp[0][N-1];
}
```
