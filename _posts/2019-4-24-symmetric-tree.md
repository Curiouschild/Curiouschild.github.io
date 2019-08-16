---
title:  "101. Symmetric Tree"
date:   2019-4-24 11:58:00 +0930
categories: Leetcode
tags: Tree Easy
---

[{{page.title}}](https://leetcode.com/problems/symmetric-tree/){:target="_blank"}

    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

    For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

        1
       / \
      2   2
     / \ / \
    3  4 4  3



    But the following [1,2,2,null,3,null,3] is not:

        1
       / \
      2   2
       \   \
       3    3




* Iterative

```java

class Solution {
    public boolean isSymmetric(TreeNode root) {
        if(root == null) return true;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root.left);
        q.offer(root.right);
        while(!q.isEmpty()) {
            TreeNode x = q.poll(), y = q.poll();
            if(x == null && y == null) continue;
            if(x == null || y == null || x.val != y.val) return false;
            q.offer(x.left);
            q.offer(y.right);
            q.offer(x.right);
            q.offer(y.left);
        }
        return true;
    }
  }
```

* Recursive

```java
    public boolean isSymmetric2(TreeNode root) {
        if(root == null) return true;
        return check(root.left, root.right);
    }

    public boolean check(TreeNode x, TreeNode y) {
        if(x == null && y == null) return true;
        if(x == null || y == null) return false;
        if(x.val != y.val) return false;
        return check(x.left, y.right) && check(x.right, y.left);
    }
```
