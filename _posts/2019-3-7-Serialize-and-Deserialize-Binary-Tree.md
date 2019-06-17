---
title:  "297. Serialize and Deserialize Binary Tree"
date:   2019-3-7 11:12:21 +0930
categories: Leetcode
tags: Serialization Tree
---

[{{page.title}}](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/){:target="_blank"}

    Serialization is the process of converting a data structure or object into a
    sequence of bits so that it can be stored in a file or memory buffer, or
    transmitted across a network connection link to be reconstructed later in
    the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no
    restriction on how your serialization/deserialization algorithm should work.
    You just need to ensure that a binary tree can be serialized to a string and
    this string can be deserialized to the original tree structure.

```java
public String serialize(TreeNode root) {
    if(root == null) return "null";
    return "" + root.val + "#" + serialize(root.left) + "#" + serialize(root.right);
}
public TreeNode deserialize(String data) {
    LinkedList<String> list = new LinkedList<>(Arrays.asList(data.split("#")));
    return ddfs(list);
}
public TreeNode ddfs(LinkedList<String> list) {
    if(list.isEmpty()) return null;
    TreeNode root = null;
    String curr = list.removeFirst();
    if(!curr.equals("null")) {
        root = new TreeNode(Integer.valueOf(curr));
        root.left = ddfs(list);
        root.right = ddfs(list);
    }
    return root;
}
```
