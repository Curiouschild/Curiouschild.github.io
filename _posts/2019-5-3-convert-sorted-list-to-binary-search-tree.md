---
title:  "109. Convert Sorted List to Binary Search Tree"
date:   2019-05-03 13:04:00 +0930
categories: Leetcode
tags: Medium Tree
---

[{{page.title}}](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/){:target="_blank"}

    Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced
    BST.

    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

    Example:

    Given the sorted linked list: [-10,-3,0,5,9],

    One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

          0
         / \
       -3   9
       /   /
     -10  5



* Naive recursion

Another option is to convert the list into an array. Trade off space for time

```java
public TreeNode sortedListToBST(ListNode head) {
    return build(head);
}

public TreeNode build(ListNode head) {
    if(head == null) return null;
    if(head.next == null) return new TreeNode(head.val);
    ListNode fast = head, slow = head, prev = head;
    while(fast != null && fast.next != null) {
        fast = fast.next.next;
        prev = slow;
        slow = slow.next;
    }
    prev.next = null;
    TreeNode root = new TreeNode(slow.val);
    root.left = build(head);
    root.right = build(slow.next);
    return root;
}
```

* a logN space approach

```java 
class Solution {
    ListNode head;
    public TreeNode sortedListToBST(ListNode head) {
        this.head = head;
        ListNode curr = head;
        int len = 0;
        while(curr != null) {
            len++;
            curr = curr.next;
        }
        TreeNode root = build(0, len-1);
        return root;
    }

    public TreeNode build(int l, int r) {
        if(l > r) return null;
        int mid = l + (r-l) / 2;
        TreeNode left = build(l, mid-1);
        TreeNode root = new TreeNode(head.val);
        head = head.next;
        root.left = left;
        root.right = build(mid+1, r);
        return root;
    }
```
