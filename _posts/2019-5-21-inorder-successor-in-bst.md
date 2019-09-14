---
title:  "285. Inorder Successor in BST"
date:   2019-05-21 16:29:00 +0930
categories: Leetcode
tags: Medium Array
---

[{{page.title}}](https://leetcode.com/problems/inorder-successor-in-bst/){:target="_blank"}

    Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

    The successor of a node p is the node with the smallest key greater than p.val.

    Example 1:

    Input: root = [2,1,3], p = 1
    Output: 2
    Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.


```java
class Solution {
    TreeNode result;
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        traverse(root, p.val);
        return result;
    }

    public void traverse(TreeNode root, int v) {
        if(root == null) return;
        if(result != null) return;
        traverse(root.left, v);
        if(result == null && root.val > v)
            result = root;
        if(result != null) return;
        traverse(root.right, v);
    }
}
```
