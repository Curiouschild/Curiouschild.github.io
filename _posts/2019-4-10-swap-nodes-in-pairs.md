---
title:  "24. Swap Nodes in Pairs"
date:   2019-4-10 22:22:00 +0930
categories: Leetcode
tags: LinkedList ReverseNodes
---

[{{page.title}}](https://leetcode.com/problems/swap-nodes-in-pairs/){:target="_blank"}

    Given a linked list, swap every two adjacent nodes and return its head.

    You may not modify the values in the list's nodes, only nodes itself may be changed.

    Example:

    Given 1->2->3->4, you should return the list as 2->1->4->3.


```java
public ListNode swapPairs(ListNode head) {
    ListNode sentinel = new ListNode(0);
    sentinel.next = head;
    ListNode curr = head, prev = sentinel;
    while(curr != null && curr.next != null) {
        ListNode n = curr.next;
        prev.next = n;
        curr.next = n.next;
        n.next = curr;
        prev = curr;
        curr = prev.next;
    }
    return sentinel.next;
}
```
