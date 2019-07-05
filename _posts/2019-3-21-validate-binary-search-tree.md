---
title:  "98. Validate Binary Search Tree"
date:   2019-3-21 23:02:00 +0930
categories: Leetcode
tags: Recursive
---

[{{page.title}}](https://leetcode.com/problems/validate-binary-search-tree/){:target="_blank"}

    Given a binary tree, determine if it is a valid binary search tree (BST).

    Assume a BST is defined as follows:

        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.



    Example 1:

        2
       / \
      1   3

    Input: [2,1,3]
    Output: true


* Recursion

```java

public boolean isValidBST(TreeNode root) {
    return check(root, null, null);
}

public boolean check(TreeNode root, Integer min, Integer max) {
    // if current node valid
    if(root == null) return true;
    if(min != null && root.val <= min) return false;
    if(max != null && root.val >= max) return false;
    // if children valid
    return check(root.left, min, root.val) && check(root.right, root.val, max);
}```
