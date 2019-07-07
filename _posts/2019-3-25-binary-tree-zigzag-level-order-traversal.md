---
title:  "103. Binary Tree Zigzag Level Order Traversal"
date:   2019-3-25 13:57:00 +0930
categories: Leetcode
tags: Tree
---

[{{page.title}}](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/){:target="_blank"}

    Given a binary tree, return the zigzag level order traversal of its nodes' values.
    (ie, from left to right, then right to left for the next level and alternate between).

    For example:
    Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

    return its zigzag level order traversal as:

    [
      [3],
      [20,9],
      [15,7]
    ]


```java
public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if(root == null) return result;
    ArrayDeque<TreeNode> q = new ArrayDeque<>();
    q.offer(root);
    int level = 0;
    while(!q.isEmpty()) {
        int size = q.size();
        level++;
        LinkedList<Integer> temp = new LinkedList<>();
        boolean isReverse = level % 2 == 0;
        for(int i = 0; i < size; i++) {
            TreeNode curr = q.poll();
            if(isReverse) temp.addFirst(curr.val);
            else temp.add(curr.val);
            if(curr.left != null) q.offer(curr.left);
            if(curr.right != null) q.offer(curr.right);
        }
        result.add(temp);
    }
    return result;
}

```
