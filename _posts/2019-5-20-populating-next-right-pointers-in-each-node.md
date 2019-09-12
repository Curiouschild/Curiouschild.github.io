---
title:  "116. Populating Next Right Pointers in Each Node"
date:   2019-05-20 09:41:00 +0930
categories: Leetcode
tags: Medium Tree Recursive
---

[{{page.title}}](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/){:target="_blank"}

    You are given a perfect binary tree where all leaves are on the same level, and every parent has two
    children. The binary tree has the following definition:

    struct Node {
    int val;
    Node *left;
    Node *right;
    Node *next;
    }

    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.

![img](/img/posts/populating-next-right-pointers-in-each-node.png)

* Iterative level by level

Utilize next pointers on the upper level

```java
public Node connect(Node root) {
    if(root == null) return root;
    Node head = root, curr = head;
    while(head.left != null) {
        curr = head;
        while(curr != null) {
            curr.left.next = curr.right;
            curr.right.next = curr.next == null ? null : curr.next.left;
            curr = curr.next;
        }
        head = head.left;
    }
    return root;
}
```


* Recursion with pairs

```java

public Node connect(Node root) {
    if(root == null) return null;
    connect(root.left, root.right);
    return root;
}

public void connect(Node left, Node right) {
    if(left == null) return;
    left.next = right;
    connect(left.left, left.right);
    connect(right.left, right.right);
    connect(left.right, right.left);
}

```

* Recursion

```java

public Node connect(Node root) {
    if(root == null || root.left == null) return root;
    root.left.next = root.right;
    root.right.next = root.next == null ? null : root.next.left;
    connect(root.left);
    connect(root.right);
    return root;
}
```
