---
title:  "1197. Minimum Knight Moves"
date:   2019-05-26 10:53:00 +0930
categories: Leetcode
tags: Medium Matrix Math
---

[{{page.title}}](https://leetcode.com/problems/minimum-knight-moves/){:target="_blank"}

    In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0,
    0].

    A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal
    direction, then one square in an orthogonal direction.

    Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the
    answer exists.



    Example 1:

    Input: x = 2, y = 1
    Output: 1
    Explanation: [0, 0] → [2, 1]

    Example 2:

    Input: x = 5, y = 5
    Output: 4
    Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]



    Constraints:

        |x| + |y| <= 300

* Bidirectional bfs


```java

public int minKnightMoves(int x, int y) {
    if(x == 0 && y == 0) return 0;
    x = Math.abs(x);
    y = Math.abs(y);
    int[] xs = {1,1,2,2,-1,-1,-2,-2}, ys = {2,-2,1,-1,2,-2,1,-1};
    HashSet<String> visited = new HashSet<>();
    HashSet<String> visited2 = new HashSet<>();
    Queue<int[]> q = new LinkedList<>();
    q.offer(new int[]{0,0});
    visited.add(0 + "&" + 0);

    Queue<int[]> q2 = new LinkedList<>();
    q2.offer(new int[]{x,y});
    visited2.add(x + "&" + y);

    int l = 0, l2 = 0;

    while(!q.isEmpty()) {
        int size = q.size();
        for(int t = 0; t < size; t++) {
            int[] c = q.poll();
            for(int k = 0; k < 8; k++) {
                int nx = xs[k] + c[0], ny = ys[k] + c[1];
                String key = nx + "&" + ny;
                if(nx == x && ny == y) return l+1;
                if(visited2.contains(key)) return l + l2 + 1;
                if(nx + ny > 300 || visited.contains(key)) continue;
                if(nx > x + 2 || ny > y + 2) continue;
                visited.add(key);
                q.offer(new int[] {nx, ny});
            }

        }
        l++;

        int size2 = q2.size();
        for(int t = 0; t < size2; t++) {
            int[] c = q2.poll();
            for(int k = 0; k < 8; k++) {
                int nx = xs[k] + c[0], ny = ys[k] + c[1];
                String key = nx + "&" + ny;
                if(visited.contains(key)) return l + l2 + 1;
                if(x < -2 || y < -2) continue;
                if(nx + ny > 300 || visited2.contains(key)) continue;
                visited2.add(key);
                q2.offer(new int[] {nx, ny});
            }

        }
        l2++;
    }
    return -1;
}
```
