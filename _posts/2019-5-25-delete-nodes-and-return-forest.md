---
title:  "1110. Delete Nodes And Return Forest"
date:   2019-05-25 10:53:00 +0930
categories: Leetcode
tags: Easy Math
---

[{{page.title}}](https://leetcode.com/problems/delete-nodes-and-return-forest/){:target="_blank"}

    Given the root of a binary tree, each node in the tree has a distinct value.

    After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

    Return the roots of the trees in the remaining forest.  You may return the result in any order.



    Example 1:

    Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
    Output: [[1,2,null,4],[6],[7]]



    Constraints:

        The number of nodes in the given tree is at most 1000.
        Each node has a distinct value between 1 and 1000.
        to_delete.length <= 1000
        to_delete contains distinct values between 1 and 1000.


* The boolean value is true when the node is a root of a tree in the forest

```java

public List<TreeNode> delNodes(TreeNode root, int[] toDelete) {
    HashSet<Integer> set = new HashSet<>();
    for(int i : toDelete) set.add(i);
    return dfs(root, set, true);
}

public List<TreeNode> dfs(TreeNode root, HashSet<Integer> set, boolean isRoot) {
    List<TreeNode> result = new ArrayList<>();
    if(root == null) return result;
    if(set.contains(root.val)) {
        result = dfs(root.left, set, true);
        result.addAll(dfs(root.right, set, true));
        root.left = null;
        root.right = null;
    } else {
        if(isRoot) result.add(root);
        result.addAll(dfs(root.left, set, false));
        result.addAll(dfs(root.right, set, false));
        if(root.left != null && set.contains(root.left.val)) root.left = null;
        if(root.right != null && set.contains(root.right.val)) root.right = null;
    }
    return result;
}
```
