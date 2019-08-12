---
title:  "199. Binary Tree Right Side View"
date:   2019-4-21 13:53:00 +0930
categories: Leetcode
tags: Recursive
---

[{{page.title}}](https://leetcode.com/problems/binary-tree-right-side-view/){:target="_blank"}

    Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you
    can see ordered from top to bottom.

    Example:

    Input: [1,2,3,null,5,null,4]
    Output: [1, 3, 4]
    Explanation:

       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---



* preorder traverse; right -> left
```java
class Solution {
    int deepest = 0;
     public List<Integer> rightSideView(TreeNode root) {
         ArrayList<Integer> result = new ArrayList<>();
         traverse(root, result, 1);
         return result;
     }

    public void traverse(TreeNode root, ArrayList<Integer> result, int level) {
        if(root == null) return;
        if(level == deepest + 1) {
            result.add(root.val);
            deepest = level;
        }
        traverse(root.right, result, level+1);
        traverse(root.left, result, level+1);
    }
  }
```
