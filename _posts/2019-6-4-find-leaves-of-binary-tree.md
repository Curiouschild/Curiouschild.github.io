---
title:  "366. Find Leaves of Binary Tree"
date:   2019-06-04 15:38:00 +0930
categories: Leetcode
tags: Medium Tree
---

[{{page.title}}](https://leetcode.com/problems/find-leaves-of-binary-tree/){:target="_blank"}

    Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.



    Example:

    Input: [1,2,3,4,5]

              1
             / \
            2   3
           / \
          4   5

    Output: [[4,5,3],[2],[1]]



    Explanation:

    1. Removing the leaves [4,5,3] would result in this tree:

              1
             /
            2



    2. Now removing the leaf [2] would result in this tree:

              1



    3. Now removing the leaf [1] would result in the empty tree:

              []


* post order traverse
  - record the height of the current subtree

```java

class Solution {
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        getH(result, root);
        return result;
    }

    public int getH(List<List<Integer>> result, TreeNode root) {
        if(root == null) return 0;
        int l = getH(result, root.left);
        int r = getH(result, root.right);
        int h = Math.max(l, r) + 1;
        if(h > result.size()) result.add(new ArrayList<>());
        result.get(h-1).add(root.val);
        return h;
    }
}
```
