---
title:  "236. Lowest Common Ancestor of a Binary Tree"
date:   2019-4-7 22:28:00 +0930
categories: Leetcode
tags: DataStructure Tree
---

[{{page.title}}](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/){:target="_blank"}


```java

class Solution {
    public Result search(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null) return new Result();

        Result left = search(root.left, p, q);
        if(left.ancestor != null) return left;
        if(left.p && root == q || left.q && root == p) return new Result(root, true, true);

        Result right = search(root.right, p, q);
        if(right.ancestor != null) return right;
        if(right.p && root == q || right.q && root == p) return new Result(root, true, true);

        if(left.q && right.p || left.p && right.q) return new Result(root, true, true);

        return new Result(null, left.p || right.p || root == p, left.q || right.q || root == q);
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        Result r = search(root, p, q);
        return r.ancestor;
    }

    class Result {
        TreeNode ancestor;
        boolean p;
        boolean q;
        public Result() {}
        public Result(TreeNode n, boolean p, boolean q) {
            this.ancestor = n;
            this.p = p;
            this.q = q;
        }
    }
  }

```
