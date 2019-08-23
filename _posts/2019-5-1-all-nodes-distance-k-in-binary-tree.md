---
title:  "863. All Nodes Distance K in Binary Tree"
date:   2019-05-01 14:21:00 +0930
categories: Leetcode
tags: Medium Tree
---

[{{page.title}}](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/){:target="_blank"}

    We are given a binary tree (with root node root), a target node, and an integer value K.

    Return a list of the values of all nodes that have a distance K from the target node.  The answer can be
    returned in any order.



    Example 1:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

    Output: [7,4,1]

    Explanation:
    The nodes that are a distance 2 from the target node (with value 5)
    have values 7, 4, and 1.



    Note that the inputs "root" and "target" are actually TreeNodes.
    The descriptions of the inputs above are just serializations of these objects.



    Note:

        The given tree is non-empty.
        Each node in the tree has unique values 0 <= node.val <= 500.
        The target node is a node in the tree.
        0 <= K <= 1000.




```java
class Solution {
    // f(root.parent, K-1) + f(root.child, K-1)
    Stack<TreeNode> stack = new Stack<>();

    public List<Integer> distanceK(TreeNode root, TreeNode target, int K) {
        List<Integer> result = new ArrayList<Integer>();
        find(root, target);
        System.out.println(stack.size());
        stack.push(target);
        HashSet<TreeNode> visited = new HashSet<>();
        while(!stack.isEmpty() && K >= 0) {
            collect(stack.pop(), result, visited, K);
            K--;
        }
        return result;
    }

    public void collect(TreeNode root, List<Integer> result, HashSet<TreeNode> visited, int K) {
        if(root == null) return;
        if(visited.contains(root)) return;
        visited.add(root);
        if(K == 0) result.add(root.val);
        else {
            collect(root.left, result, visited, K-1);
            collect(root.right, result, visited, K-1);
        }
    }

    public boolean find(TreeNode root, TreeNode target) {
        if(root == null) return false;
        if(root == target) return true;
        stack.push(root);
        boolean onLeft = find(root.left, target);
        boolean onRight = find(root.right, target);
        if(!onLeft && !onRight) stack.pop();
        return onLeft || onRight;
    }
}
```
