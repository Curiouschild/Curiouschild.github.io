---
title:  "226. Invert Binary Tree"
date:   2019-05-23 23:13:00 +0930
categories: Leetcode
tags: Easy Tree
---

[{{page.title}}](https://leetcode.com/problems/invert-binary-tree/){:target="_blank"}

    Invert a binary tree.

    Example:

    Input:

         4
       /   \
      2     7
     / \   / \
    1   3 6   9

    Output:

         4
       /   \
      7     2
     / \   / \
    9   6 3   1

    Important:
    This problem was inspired by this original tweet by Max Howell:

        Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

* Easy

```java

public TreeNode invertTree(TreeNode root) {
    if(root == null) return null;
    TreeNode temp = root.left;
    root.left = root.right;
    root.right = temp;
    invertTree(root.right);
    invertTree(root.left);
    return root;
}
```
