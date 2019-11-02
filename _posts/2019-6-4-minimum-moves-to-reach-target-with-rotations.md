---
title:  "1210. Minimum Moves to Reach Target with Rotations"
date:   2019-06-04 22:04:00 +0930
categories: Leetcode
tags: Hard BFS Matrix
---

[{{page.title}}](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/){:target="_blank"}

    In an n*n grid, there is a snake that spans 2 cells and starts moving from the top left corner at (0, 0)
    and (0, 1). The grid has empty cells represented by zeros and blocked cells represented by ones. The snake
    wants to reach the lower right corner at (n-1, n-2) and (n-1, n-1).

    In one move the snake can:

        Move one cell to the right if there are no blocked cells there. This move keeps the horizontal/
        vertical position of the snake as it is.

        Move down one cell if there are no blocked cells there. This move keeps the horizontal/vertical
        position of the snake as it is.

        Rotate clockwise if it's in a horizontal position and the two cells under it are both empty. In that
        case the snake moves from (r, c) and (r, c+1) to (r, c) and (r+1, c).

        Rotate counterclockwise if it's in a vertical position and the two cells to its right are both empty.
        In that case the snake moves from (r, c) and (r+1, c) to (r, c) and (r, c+1).

    Return the minimum number of moves to reach the target.

    If there is no way to reach the target, return -1.



    Example 1:

    Input: grid = [[0,0,0,0,0,1],
                   [1,1,0,0,1,0],
                   [0,0,0,0,1,1],
                   [0,0,1,0,1,0],
                   [0,1,1,0,0,0],
                   [0,1,1,0,0,0]]
    Output: 11
    Explanation:
    One possible solution is [right, right, rotate clockwise, right, down, down, down, down, rotate
    counterclockwise, right, down].

    Example 2:

    Input: grid = [[0,0,1,1,1,1],
                   [0,0,0,0,1,1],
                   [1,1,0,0,0,1],
                   [1,1,1,0,0,1],
                   [1,1,1,0,0,1],
                   [1,1,1,0,0,0]]
    Output: 9



    Constraints:

        2 <= n <= 100
        0 <= grid[i][j] <= 1
        It is guaranteed that the snake starts at empty cells.



* BFS

```java

class Solution {
    public int minimumMoves(int[][] grid) {
        int n = grid.length;
        LinkedList<Integer> q = new LinkedList<>();
        HashSet<Integer> visited = new HashSet<>();
        q.offer(getKey(0, 0, 0));
        int level = 0, target = getKey(n-1, n-2, 0);
        while(!q.isEmpty()) {
            int size = q.size();
            for(int p = 0; p < size; p++) {
                int num = q.poll();
                if(visited.contains(num)) continue;
                visited.add(num);
                if(num == target) return level;
                int i = num / 1000, j = (num-i*1000) / 10, d = num & 1;
                if(d == 0) { // horizontal
                    if((j+2 < n) && grid[i][j+2] == 0) // move forward (right)
                        q.offer(getKey(i, j+1, 0));
                    if(i+1 < n && j+1 < n && grid[i+1][j] == 0 && grid[i+1][j+1] == 0) {
                        q.offer(getKey(i, j, 1)); // rotate
                        q.offer(getKey(i+1, j, 0)); // move down entirely
                    }
                } else { // vertical
                    if(i+2 < n && grid[i+2][j] == 0) // move forward (down)
                        q.offer(getKey(i+1, j, 1));
                    if(i+1 < n && j+1 < n && grid[i][j+1] == 0 && grid[i+1][j+1] == 0) {
                        q.offer(getKey(i, j, 0));  // rotate
                        q.offer(getKey(i, j+1, 1)); // move right entirely
                    }
                }
            }
            level++;
        }
        return -1;
    }

	// 0 <= i , j <= 99
    public int getKey(int i, int j, int d) {
        return i * 1000 + j * 10 + d;
    }
}
```
