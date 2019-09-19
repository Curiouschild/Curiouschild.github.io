---
title:  "298. Binary Tree Longest Consecutive Sequence"
date:   2019-05-26 16:37:00 +0930
categories: Leetcode
tags: Medium Tree Recursive
---

[{{page.title}}](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/){:target="_blank"}

    Given a binary tree, find the length of the longest consecutive sequence path.

    The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-
    child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

    Example 1:

    Input:

       1
        \
         3
        / \
       2   4
            \
             5

    Output: 3

    Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

    Example 2:

    Input:

       2
        \
         3
        /
       2
      /
     1

    Output: 2

    Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

```java

int result = 0;
public int longestConsecutive(TreeNode root) {
    traverse(root);
    return result;
}
public int traverse(TreeNode root) {
    if(root == null) return 0;
    int left = traverse(root.left), right = traverse(root.right);
    int max = 1;
    if(root.left != null && root.val+1 == root.left.val) {
        max = left + 1;
    }
    if(root.right != null && root.val+1 == root.right.val) {
        max = Math.max(max, right+1);
    }
    result = Math.max(max, result);
    return max;
}
```
