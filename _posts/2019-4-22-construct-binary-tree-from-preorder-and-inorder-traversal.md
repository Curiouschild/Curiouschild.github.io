---
title:  "105. Construct Binary Tree from Preorder and Inorder Traversal"
date:   2019-4-22 13:28:00 +0930
categories: Leetcode
tags: Recursive
---

[{{page.title}}](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/){:target="_blank"}

    Given preorder and inorder traversal of a tree, construct the binary tree.

    Note:
    You may assume that duplicates do not exist in the tree.

    For example, given

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    Return the following binary tree:

        3
       / \
      9  20
        /  \
       15   7




* Recursive
Optimized with hashmap to store inorder element -> index

```java

class Solution {
    HashMap<Integer, Integer> map = new HashMap<>(); // inorder element -> index
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for(int i = 0; i < inorder.length; i++) map.put(inorder[i], i);
        return recursion(preorder, inorder, 0, preorder.length-1, 0, inorder.length-1);
    }

    public TreeNode recursion(int[] preorder, int[] inorder, int l, int r, int il, int ir) {
        if(preorder.length == 0) return null;
        if(l > r) return null;
        TreeNode root = new TreeNode(preorder[l]);
        if(l < r) {
            int i = map.get(preorder[l]);
            // while(i <= ir && inorder[i] != preorder[l]) i++;
            int leftLen = i - il, rightLen = ir - i;
            root.left = recursion(preorder, inorder, l+1, l+leftLen, il, i-1);
            root.right = recursion(preorder, inorder, l+leftLen+1, r, i+1, ir);
        }
        return root;
    }
```
