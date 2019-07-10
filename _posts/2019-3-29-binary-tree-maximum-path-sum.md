---
title:  "124. Binary Tree Maximum Path Sum"
date:   2019-3-29 22:50:00 +0930
categories: Leetcode
tags: Recursion Tree
---

[{{page.title}}](https://leetcode.com/problems/binary-tree-maximum-path-sum/){:target="_blank"}

    Given a non-empty binary tree, find the maximum path sum.

    For this problem, a path is defined as any sequence of nodes from some starting node to any
    node in the tree along the parent-child connections. The path must contain at least one node
    and does not need to go through the root.

    Example 1:

    Input: [1,2,3]

           1
          / \
         2   3

    Output: 6


```java
int result = Integer.MIN_VALUE;
public int maxPathSum(TreeNode root) {
    traverse(root);
    return result;
}

public int traverse(TreeNode root) {
    if(root == null) return 0;
    int curr = root.val;
    int left = traverse(root.left), right = traverse(root.right);
    int temp = Math.max(curr, Math.max(curr+left, curr+right));
    result = Math.max(result, Math.max(temp, curr+left+right));
    return temp;
}
```
