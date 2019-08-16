---
title:  "427. Construct Quad Tree"
date:   2019-4-22 23:17:00 +0930
categories: Leetcode
tags: Recursive Medium
---

[{{page.title}}](https://leetcode.com/problems/construct-quad-tree/){:target="_blank"}


    We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false.
    The root node represents the whole grid. For each node, it will be subdivided into four children nodes
    until the values in the region it represents are all the same.

    Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a
    leaf node. The val attribute for a leaf node contains the value of the region it represents.

    Your task is to use a quad tree to represent a given grid. The following example may help you understand
    the problem better:

    Given the 8 x 8 grid below, we want to construct the corresponding quad tree:

    It can be divided according to the definition above:

![img1](/img/posts/construct-quad-tree-1.png)

    The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.

![img2](/img/posts/construct-quad-tree-2.png)

    For the non-leaf nodes, val can be arbitrary, so it is represented as *.

    Note:

        N is less than 1000 and guaranteened to be a power of 2.
        If you want to know more about the quad tree, you can refer to its wiki.


* Divide and Conquer

```java

public Node construct(int[][] grid) {
    Node root = build(grid, 0, 0, grid.length);
    return root;
}

public Node build(int[][] grid, int row, int col, int len) {
    Node n = new Node();
    int sum = 0;
    for(int i = row; i < row + len; i++) {
        for(int j = col; j < col + len; j++) {
            sum += grid[i][j];
        }
    }
    if(sum == len * len) {
        n.isLeaf = true;
        n.val = true;
    } else if(sum == 0) {
        n.isLeaf = true;
    } else {
        int half = len / 2;
        n.topLeft = build(grid, row, col, half);
        n.topRight = build(grid, row, col + half, half);
        n.bottomLeft = build(grid, row + half, col, half);
        n.bottomRight = build(grid, row + half, col + half, half);
    }
    return n;
}
```
