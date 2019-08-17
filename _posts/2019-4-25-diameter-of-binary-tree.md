---
title:  "543. Diameter of Binary Tree"
date:   2019-4-25 19:19:00 +0930
categories: Leetcode
tags: Tree Easy
---

[{{page.title}}](https://leetcode.com/problems/diameter-of-binary-tree/){:target="_blank"}

    Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary
    tree is the length of the longest path between any two nodes in a tree. This path may or may not pass
    through the root.

    Example:
    Given a binary tree

              1
             / \
            2   3
           / \
          4   5

    Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

    Note: The length of path between two nodes is represented by the number of edges between them.

* pre order traverse

```java

int result = 0;
public int diameterOfBinaryTree(TreeNode root) {
    if(root == null) return 0;
    traverse(root);
    return result-1;
}

public int traverse(TreeNode root) {
    if(root == null) return 0;
    int left = traverse(root.left);
    int right = traverse(root.right);
    result = Math.max(result, 1+right+left);
    return Math.max(left, right) + 1;
}
```
