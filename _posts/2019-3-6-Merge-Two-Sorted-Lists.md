---
title:  "21. Merge Two Sorted Lists"
date:   2019-3-6 010:15:23 +0930
categories: Leetcode
tags: LinkedList Recursive
---

[{{page.title}}](https://leetcode.com/problems/merge-two-sorted-lists/){:target="_blank"}

    Merge two sorted linked lists and return it as a new list.
    The new list should be made by splicing together the nodes of the first two lists.

1. Recursive

```java
public ListNode mergeTwoListsRecursive(ListNode l1, ListNode l2) {
    if(l1 == null) return l2;
    if(l2 == null) return l1;
    ListNode root, next;
    if(l1.val < l2.val) {
        root = l1;
        next = mergeTwoLists(l1.next, l2);
    } else {
        root = l2;
        next = mergeTwoLists(l1, l2.next);
    }
    root.next = next;
    return root;
}
```
2. Iterative

```java
public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    ListNode sentinel = new ListNode(0), curr = sentinel;
    while(l1 != null && l2 != null) {
        if(l1.val < l2.val) {
            curr.next = l1;
            l1 = l1.next;
        } else {
            curr.next = l2;
            l2 = l2.next;
        }
        curr = curr.next;
    }
    curr.next = l1 == null ? l2 : l1; // l1 and l2 are of different length
    return sentinel.next;
}
```
