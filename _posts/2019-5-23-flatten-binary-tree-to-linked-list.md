---
title:  "114. Flatten Binary Tree to Linked List"
date:   2019-05-23 23:04:00 +0930
categories: Leetcode
tags: Medium Tree
---

[{{page.title}}](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/){:target="_blank"}

    Given a binary tree, flatten it to a linked list in-place.

    For example, given the following tree:

        1
       / \
      2   5
     / \   \
    3   4   6

    The flattened tree should look like:

    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6


* Return tail of the flattened subtree

```java

class Solution {
    public void flatten(TreeNode root) {
        go(root);
    }

    public TreeNode go(TreeNode root) {
        if(root == null) return null;
        if(root.left == null && root.right == null) {
            return root;
        }
        TreeNode tl = go(root.left);
        TreeNode tr = go(root.right);
        if(tr == null) {
            root.right = root.left;
            root.left = null;
            return tl;
        } else if(tl == null) {
            return tr;
        } else {
            tl.right = root.right;
            root.right = root.left;
            root.left = null;
            return tr;
        }
    }
}
```
