---
title:  "94. Binary Tree Inorder Traversal"
date:   2019-4-30 12:19:00 +0930
categories: Leetcode
tags: Medium Tree
---

[{{page.title}}](https://leetcode.com/problems/binary-tree-inorder-traversal/){:target="_blank"}

    Given a binary tree, return the inorder traversal of its nodes' values.

    Example:

    Input: [1,null,2,3]
       1
        \
         2
        /
       3

    Output: [1,3,2]

    Follow up: Recursive solution is trivial, could you do it iteratively?


```java

public List<Integer> inorderTraversal(TreeNode root) {
    Stack<TreeNode> stack = new Stack<>();
    TreeNode curr = root;
    ArrayList<Integer> result = new ArrayList<>();
    while(curr != null || !stack.isEmpty()) {
        while(curr != null) {
            stack.push(curr);
            curr = curr.left;
        }
        curr = stack.pop();
        result.add(curr.val);
        curr = curr.right;
    }
    return result;
}
```
