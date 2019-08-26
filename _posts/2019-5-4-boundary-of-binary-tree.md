---
title:  "545. Boundary of Binary Tree"
date:   2019-05-04 12:04:00 +0930
categories: Leetcode
tags: Easy String Palindrome
---

[{{page.title}}](https://leetcode.com/problems/boundary-of-binary-tree/){:target="_blank"}

    Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. 
    Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.  (The values
    of the nodes may still be duplicates.)

    Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the
    path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the
    root itself is left boundary or right boundary. Note this definition only applies to the input binary
    tree, and not applies to any subtrees.

    The left-most node is defined as a leaf node you could reach when you always firstly travel to the left
    subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

    The right-most node is also defined by the same way with left and right exchanged.

    Example 1

    Input:
      1
       \
        2
       / \
      3   4

    Ouput:
    [1, 3, 4, 2]

    Explanation:
    The root doesn't have left subtree, so the root itself is left boundary.
    The leaves are node 3 and 4.
    The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed
    right boundary.
    So order them in anti-clockwise without duplicates and we have [1,3,4,2].



    Example 2

    Input:
        ____1_____
       /          \
      2            3
     / \          /
    4   5        6
       / \      / \
      7   8    9  10

    Ouput:
    [1,2,4,7,8,9,10,6,3]

    Explanation:
    The left boundary are node 1,2,4. (4 is the left-most node according to definition)
    The leaves are node 4,7,8,9,10.
    The right boundary are node 1,3,6,10. (10 is the right-most node).
    So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].


* A fast coded answer

Searching for leftmost and rightmost and leaves are overlapped, so i'll try to optimize the solution. Hope to solve it with one pass inorder traverse

```java
class Solution {
    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<>();
        if(root == null) return result;
        HashSet<TreeNode> added = new HashSet<>();
        // left boundary
        TreeNode curr = root;
        added.add(curr);
        result.add(curr.val);
        if(curr.left != null) {
            curr = curr.left;
            while(curr != null) {
                added.add(curr);
                result.add(curr.val);
                if(curr.left != null) curr = curr.left;
                else curr = curr.right;
            }
        }
        // right boundary
        ArrayList<Integer> temp = new ArrayList<>();
        curr = root;
        if(curr.right != null) {
            curr = curr.right;
            while(curr != null) {
                if(!added.contains(curr)) {
                    temp.add(curr.val);
                    added.add(curr);
                }
                curr = curr.right != null ? curr.right : curr.left;
            }
        }
        // collect leaves
        collect(root, added, result);
        for(int i = temp.size()-1; i >= 0; i--) result.add(temp.get(i));
        return result;

    }
    public void collect(TreeNode root, HashSet<TreeNode> added, ArrayList<Integer> result) {
        if(root == null) return;
        if(root.left == null && root.right == null && !added.contains(root)) {
            result.add(root.val);
            added.add(root);
        }
        collect(root.left, added, result);
        collect(root.right, added, result);
    }
}
```
