---
title:  "987. Vertical Order Traversal of a Binary Tree"
date:   2019-05-10 19:11:00 +0930
categories: Leetcode
tags: Medium Tree
---

[{{page.title}}](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/){:target="_blank"}

    Given a binary tree, return the vertical order traversal of its nodes values.

    For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1)
    and (X+1, Y-1).

    Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes,
    we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

    If two nodes have the same position, then the value of the node that is reported first is the value that is
    smaller.

    Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of
    nodes.

    Example 1:

    Input: [3,9,20,null,null,15,7]
    Output: [[9],[3,15],[20],[7]]
    Explanation:
    Without loss of generality, we can assume the root node is at position (0, 0):
    Then, the node with value 9 occurs at position (-1, -1);
    The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
    The node with value 20 occurs at position (1, -1);
    The node with value 7 occurs at position (2, -2).

![img1](/img/posts/vertical-order-traversal-of-a-binary-tree-1.png)

* Sorting

```java

public List<List<Integer>> verticalTraversal(TreeNode root) {
    PriorityQueue<Node> q = new PriorityQueue<>((a,b)->{
        int c = Integer.compare(a.c, b.c);
        if(c != 0) return c;
        int r = Integer.compare(a.r, b.r);
        if(r != 0) return r;
        return Integer.compare(a.v, b.v);
    });
    traverse(root, q, 0, 0);
    List<List<Integer>> result = new ArrayList<>();
    Node pre = null;
    ArrayList<Integer> line = null;
    while(!q.isEmpty()) {
        if(pre == null || pre.c != q.peek().c) {
            if(pre != null) result.add(line);
            line = new ArrayList<>();
        }
        pre = q.poll();
        line.add(pre.v);
        if(q.isEmpty()) {
            result.add(line);
        }
    }
    return result;

}
public void traverse(TreeNode root, PriorityQueue<Node> q, int r, int c) {
    if(root == null) return;
    q.offer(new Node(root.val, r, c));
    traverse(root.left, q, r+1, c-1);
    traverse(root.right, q, r+1, c+1);
}
class Node {
    int v;
    int r;
    int c;
    public Node(int v, int r, int c) {
        this.v = v;
        this.r = r;
        this.c = c;
    }
}
```
