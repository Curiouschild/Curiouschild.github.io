---
title:  "572. Subtree of Another Tree"
date:   2019-05-26 23:45:00 +0930
categories: Leetcode
tags: Easy Tree
---

[{{page.title}}](https://leetcode.com/problems/subtree-of-another-tree/){:target="_blank"}

    Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node
    values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's
    descendants. The tree s could also be considered as a subtree of itself.

    Example 1:
    Given tree s:

         3
        / \
       4   5
      / \
     1   2

    Given tree t:

       4
      / \
     1   2

    Return true, because t has the same structure and node values with a subtree of s.

    Example 2:
    Given tree s:

         3
        / \
       4   5
      / \
     1   2
        /
       0

    Given tree t:

       4
      / \
     1   2

    Return false.


```java

public boolean isSubtree(TreeNode s, TreeNode t) {
     if(s == null) return false;
     boolean root = false;
     if(s.val == t.val) root = check(s, t);
     if(root) return true;
     boolean left = isSubtree(s.left, t);
     if(left) return true;
     boolean right = isSubtree(s.right, t);
     return right;
 }

 public boolean check(TreeNode s, TreeNode t) {
     if(s == null && t == null) return true;
     if(s == null || t == null) return false;
     if(s.val != t.val) return false;
     return check(s.left, t.left) && check(s.right, t.right);
 }
```
