---
title:  "951. Flip Equivalent Binary Trees"
date:   2019-05-25 21:21:00 +0930
categories: Leetcode
tags: Medium Recursive Tree
---

[{{page.title}}](https://leetcode.com/problems/flip-equivalent-binary-trees/){:target="_blank"}

    For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and
    right child subtrees.

    A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some
    number of flip operations.

    Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root
    nodes root1 and root2.

    Example 1:

    Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
    Output: true
    Explanation: We flipped at nodes with values 1, 3, and 5.
    Flipped Trees Diagram

![img](/img/posts/flip-equivalent-binary-trees.png)

    Note:

        Each tree will have at most 100 nodes.
        Each value in each tree will be a unique integer in the range [0, 99].




* Easy Divide and Conquer

Another approach:
Since the values in the tree are unique. We can also convert two trees to a canonical representation, then
compare equality. (eg. always visit the smaller node of a pair of sister nodes)

```java

public boolean flipEquiv(TreeNode root1, TreeNode root2) {
    if(root1 == null && root2 == null) return true;
    if(root1 == null || root2 == null || root1.val != root2.val) return false;
    return flipEquiv(root1.left, root2.left) && flipEquiv(root1.right, root2.right)
        || flipEquiv(root1.left, root2.right) && flipEquiv(root1.right, root2.left);
}
```
