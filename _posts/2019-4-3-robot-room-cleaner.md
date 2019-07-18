---
title:  "489. Robot Room Cleaner"
date:   2019-4-3 23:16:00 +0930
categories: Leetcode
tags: Backtracking Graph
---

[{{page.title}}](https://leetcode.com/problems/robot-room-cleaner/){:target="_blank"}

    Given a robot cleaner in a room modeled as a grid.

    Each cell in the grid can be empty or blocked.

    The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it
    made is 90 degrees.

    When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays
    on the current cell.

    Design an algorithm to clean the entire room using only the 4 given APIs shown below.

    interface Robot {
      // returns true if next cell is open and robot moves into the cell.
      // returns false if next cell is obstacle and robot stays on the current cell.
      boolean move();

      // Robot will stay on the same cell after calling turnLeft/turnRight.
      // Each turn will be 90 degrees.
      void turnLeft();
      void turnRight();

      // Clean the current cell.
      void clean();
    }

    Example:

    Input:
    room = [
      [1,1,1,1,1,0,1,1],
      [1,1,1,1,1,0,1,1],
      [1,0,1,1,1,1,1,1],
      [0,0,0,1,0,0,0,0],
      [1,1,1,1,1,1,1,1]
    ],
    row = 1,
    col = 3

    Explanation:
    All grids in the room are marked by either 0 or 1.
    0 means the cell is blocked, while 1 means the cell is accessible.
    The robot initially starts at the position of row=1, col=3.
    From the top left corner, its position is one row below and three columns right.

    Notes:

        The input is only given to initialize the room and the robot's position internally.
        You must solve this problem "blindfolded". In other words, you must control the robot
        using only the mentioned 4 APIs, without knowing the room layout and the initial robot's
        position.
        The robot's initial position will always be in an accessible cell.
        The initial direction of the robot will be facing up.
        All accessible cells are connected, which means the all cells marked as 1 will be accessible
        by the robot.
        Assume all four edges of the grid are all surrounded by wall.


```java
int[] xs = {-1, 0, 1, 0};
int[] ys = {0, 1, 0, -1};
public void cleanRoom(Robot robot) {
    backtrack(robot, 0, 0, new HashSet<String>(), 0);
}

public void backtrack(Robot robot, int i, int j, HashSet<String> visited, int dir) {
    visited.add(i+","+j);
    robot.clean();
    for(int p = 0; p < 4; p++) {
        int d = (dir + p) % 4;
        int x = i + xs[d], y = j + ys[d];
        if(!visited.contains(x+","+y) && robot.move()) {
            backtrack(robot, x, y, visited, d);
            robot.turnRight(); // turn 180 to come back
            robot.turnRight();
            robot.move();
            robot.turnRight(); // turn to init direction
            robot.turnRight();
        }
        robot.turnRight(); // next direction
    }
}
```
