---
title:  "1008. Construct Binary Search Tree from Preorder Traversal"
date:   2019-05-18 20:45:00 +0930
categories: Leetcode
tags: Medium Tree Recursive
---

[{{page.title}}](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/){:target="_blank"}

    Return the root node of a binary search tree that matches the given preorder traversal.

    (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a
    value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder
    traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

    Example 1:

    Input: [8,5,1,7,10,12]
    Output: [8,5,10,1,7,null,12]

    1 <= preorder.length <= 100
    The values of preorder are distinct.

```java

public TreeNode bstFromPreorder(int[] preorder) {
    return build(preorder, 0, preorder.length-1);
}

public TreeNode build(int[] preorder, int start, int end) {
    if(start > end) return null;
    TreeNode root = new TreeNode(preorder[start]);
    int i = start + 1;
    while(i <= end && preorder[i] < root.val) i++;
    root.left = build(preorder, start+1, i-1);
    root.right = build(preorder, i, end);
    return root;
}
```
