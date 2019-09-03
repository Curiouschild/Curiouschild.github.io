---
title:  "222. Count Complete Tree Nodes"
date:   2019-05-11 10:44:00 +0930
categories: Leetcode
tags: Medium Recursion
---

[{{page.title}}](https://leetcode.com/problems/count-complete-tree-nodes/){:target="_blank"}

    Given a complete binary tree, count the number of nodes.

    Note:

    Definition of a complete binary tree from Wikipedia:
    In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

    Example:

    Input:
        1
       / \
      2   3
     / \  /
    4  5 6

    Output: 6




* Divide and conquer

```java

public int countNodes(TreeNode root) {
    if(root == null) return 0;
    int l = getH(root.left), r = getH(root.right);
    if(l > r) { // r is complete
        return 1 + height2count(r) + countNodes(root.left);
    } else { // l is complete
        return 1 + height2count(l) + countNodes(root.right);
    }
}

public int getH(TreeNode root) {
    if(root == null) return -1;
    return 1 + getH(root.left);
}

public int height2count(int h) {
    return (int)Math.pow(2, h+1) - 1;
}
```
