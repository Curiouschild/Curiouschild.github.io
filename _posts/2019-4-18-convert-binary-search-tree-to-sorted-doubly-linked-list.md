---
title:  "426. Convert Binary Search Tree to Sorted Doubly Linked List"
date:   2019-4-18 19:16:00 +0930
categories: Leetcode
tags: Tree DataStructure
---

[{{page.title}}](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/){:target="_blank"}

    Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as
    synonymous to the previous and next pointers in a doubly-linked list.

    Let's take the following BST as an example, it may help you understand the problem better:

![p1](/img/posts/convert-binary-search-tree-to-sorted-doubly-linked-list-1.png)



    We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a
    predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

    The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.

![p2](/img/posts/convert-binary-search-tree-to-sorted-doubly-linked-list-2.png)



    Specifically, we want to do the transformation in place. After the transformation, the left pointer of
    the tree node should point to its predecessor, and the right pointer should point to its successor. We
    should return the pointer to the first element of the linked list.

    The figure below shows the transformed BST. The solid line indicates the successor relationship, while
    the dashed line means the predecessor relationship.


![p3](/img/posts/convert-binary-search-tree-to-sorted-doubly-linked-list-3.png)



* Recursive

```java
class Solution {
    Node head;
    Node prev;
    public Node treeToDoublyList(Node root) {
        if(root == null) return null;
        traverse(root);
        head.left = prev;
        prev.right = head;
        return head;
    }

    public void traverse(Node root) {
        if(root == null) return;
        traverse(root.left);
        if(prev != null) {
            prev.right = root;
            root.left = prev;
        } else {
            head = root;
        }
        prev = root;
        traverse(root.right);
    }
  }
```

* Iterative

```java
public Node treeToDoublyListIterative(Node root) {
    if(root == null) return root;
    Node curr = root, prev = null, head = null;
    LinkedList<Node> stack = new LinkedList<>();
    while(!stack.isEmpty() || curr != null) {
        while(curr != null) {
            stack.push(curr);
            curr = curr.left;
        }
        curr = stack.pop();
        if(prev == null) head = curr;
        else {
            prev.right = curr;
            curr.left = prev;
        }
        prev = curr;
        curr = curr.right;
    }
    head.left = prev;
    prev.right = head;
    return head;
}
```
