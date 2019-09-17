---
title:  "113. Path Sum II"
date:   2019-05-24 22:12:00 +0930
categories: Leetcode
tags: Medium Tree Recursive
---

[{{page.title}}](https://leetcode.com/problems/path-sum-ii/){:target="_blank"}

    Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

    Note: A leaf is a node with no children.

    Example:

    Given the below binary tree and sum = 22,

          5
         / \
        4   8
       /   / \
      11  13  4
     /  \    / \
    7    2  5   1

    Return:

    [
       [5,4,11,2],
       [5,8,4,5]
    ]

```java

public List<List<Integer>> pathSum(TreeNode root, int sum) {
    List<List<Integer>> result = new ArrayList<>();
    pathSum(result, new ArrayList<Integer>(), root, sum);
    return result;
}

public void pathSum(List<List<Integer>> result, ArrayList<Integer> temp, TreeNode root, int target) {
    if(root == null) return;
    if(root.val == target && root.left == null && root.right == null) {
        temp.add(root.val);
        result.add(new ArrayList<>(temp));
        temp.remove(temp.size()-1);
        return;
    }
    temp.add(root.val);
    pathSum(result, temp, root.left, target-root.val);
    pathSum(result, temp, root.right, target-root.val);
    temp.remove(temp.size()-1);
}
```
