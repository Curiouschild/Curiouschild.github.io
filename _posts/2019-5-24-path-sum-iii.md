---
title:  "437. Path Sum III"
date:   2019-05-24 21:11:00 +0930
categories: Leetcode
tags: Easy Tree Recursive
---

[{{page.title}}](https://leetcode.com/problems/path-sum-iii/){:target="_blank"}

    You are given a binary tree in which each node contains an integer value.

    Find the number of paths that sum to a given value.

    The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

    The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

    Example:

    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1

    Return 3. The paths that sum to 8 are:

    1.  5 -> 3
    2.  5 -> 2 -> 1
    3. -3 -> 11


```java
// path sum of this tree
public int pathSum(TreeNode root, int sum) {
    if(root == null) return 0;
    return withRoot(root, sum) + pathSum(root.left, sum) + pathSum(root.right, sum);
}
// path sum of this tree must include the root
public int withRoot(TreeNode root, int sum) {
    if(root == null) return 0;
    return (root.val == sum ? 1 : 0) + withRoot(root.left, sum-root.val) + withRoot(root.right, sum-root.val);
}
```

* Return all sums with current root

```java

int result = 0;
public int pathSum(TreeNode root, int sum) {
    traverse(root, sum);
    return result;
}

public ArrayList<Integer> traverse(TreeNode root, int sum) {
    if(root == null) return new ArrayList<>();
    ArrayList<Integer> left = traverse(root.left, sum);
    ArrayList<Integer> right = traverse(root.right, sum);
    ArrayList<Integer> total = new ArrayList<>();
    total.addAll(left);
    total.addAll(right);

    for(int i = 0; i < total.size(); i++) {
        total.set(i, total.get(i)+root.val);
        if(total.get(i) == sum) result++;
    }
    total.add(root.val);
    if(root.val == sum) result++;
    return total;
}
```
