---
title:  "333. Largest BST Subtree"
date:   2019-05-27 15:58:00 +0930
categories: Leetcode
tags: Medium Tree
---

[{{page.title}}](https://leetcode.com/problems/largest-bst-subtree/){:target="_blank"}

    Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means
    subtree with largest number of nodes in it.

    Note:
    A subtree must include all of its descendants.

    Example:

    Input: [10,5,15,1,8,null,7]

       10
       / \
      5  15
     / \   \
    1   8   7

    Output: 3
    Explanation: The Largest BST Subtree in this case is the highlighted one.
                 The return value is the subtree's size, which is 3.

    Follow up:
    Can you figure out ways to solve it with O(n) time complexity?


```java

class Solution {
    int result = 0;
    public int largestBSTSubtree(TreeNode root) {
        find(root);
        return result;
    }

    // return {max, min, cnt}
    // {0, 0, -1} invalid substree
    public int[] find(TreeNode root) {
        if(root == null) return null;
        int[] l = find(root.left), r = find(root.right);
        if(l != null && (l[2] == -1 || root.val <= l[0]) || r != null && (r[2] == -1 || root.val >= r[1])) {
            return new int[]{0,0,-1}; // subtree or the curr tree is invalid
        }
        int max = root.val, min = root.val, cnt = 1;
        if(l != null) {
            max = Math.max(max, l[0]);
            min = Math.min(min, l[1]);
            cnt += l[2];
        }
        if(r != null) {
            max = Math.max(max, r[0]);
            min = Math.min(min, r[1]);
            cnt += r[2];
        }

        result = Math.max(result, cnt);
        return new int[] {max, min, cnt};
    }
  }
```

* More concise version

```java

class Solution {
    int result = 0;
    public int largestBSTSubtree(TreeNode root) {
        find(root);
        return result;
    }

    // return {max, min, cnt}
    // {0, 0, -1} invalid substree
    public int[] find(TreeNode root) {
        if(root == null) return new int[]{Integer.MIN_VALUE,Integer.MAX_VALUE,0};
        int[] l = find(root.left), r = find(root.right);
        if(l[2] == -1 || r[2] == -1 || root.val <= l[0] || root.val >= r[1]) {
            return new int[]{0,0,-1}; // invalid subtree or current root
        }
        int cnt = 1 + l[2] + r[2];
        result = Math.max(result, cnt);
        return new int[] {Math.max(root.val, r[0]), Math.min(root.val, l[1]), cnt};
    }
}

```
