---
title:  "95. Unique Binary Search Trees II"
date:   2019-05-01 21:40:00 +0930
categories: Leetcode
tags: Medium Tree Recursive
---

[{{page.title}}](https://leetcode.com/problems/unique-binary-search-trees-ii/){:target="_blank"}

    Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

    Example:

    Input: 3
    Output:
    [
      [1,null,3,2],
      [3,2,null,1],
      [3,1,null,null,2],
      [2,1,3],
      [1,null,2,null,3]
    ]
    Explanation:
    The above output corresponds to the 5 unique BST's shown below:

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3

```java
class Solution {

    public List<TreeNode> generateTrees(int n) {
        if(n == 0) return new ArrayList<>();
        return generate(1, n);
    }
    
    public List<TreeNode> generate(int l, int r) {
        List<TreeNode> result = new ArrayList<TreeNode>();
        if(l > r) result.add(null);
        for(int i = l; i <= r; i++) {
            List<TreeNode> left = generate(l, i-1), right = generate(i+1, r);
            for(TreeNode ln : left) {
                for(TreeNode rn : right) {
                    TreeNode root = new TreeNode(i);
                    root.left = ln;
                    root.right = rn;
                    result.add(root);
                }
            }
        }
        return result;
    }
  }
```
