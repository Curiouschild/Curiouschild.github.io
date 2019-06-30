---
title:  "25. Reverse Nodes in k-Group"
date:   2019-3-19 21:38:11 +0930
categories: Leetcode
tags: LinkedList
---

[{{page.title}}](https://leetcode.com/problems/reverse-nodes-in-k-group/){:target="_blank"}

    Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

    k is a positive integer and is less than or equal to the length of the linked list.
    If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

    Example:

    Given this linked list: 1->2->3->4->5

    For k = 2, you should return: 2->1->4->3->5

    For k = 3, you should return: 3->2->1->4->5

    Note:

        Only constant extra memory is allowed.
        You may not alter the values in the list's nodes, only nodes itself may be changed.

* Iterative

```java
public ListNode reverseKGroup(ListNode head, int k) {
    int len = 0;
    ListNode curr = head;
    while(curr != null) {
        len++;
        curr = curr.next;
    }

    ListNode sentinel = new ListNode(0), pre = sentinel;
    curr = head;
    pre.next = curr;

    for(int i = 0; i < len / k; i++) {
        for(int j = 0; j < k - 1; j++) {
            ListNode moved = curr.next;
            curr.next = moved.next;
            moved.next = pre.next;
            pre.next = moved;
        }
        pre = curr;
        curr = curr.next;
    }
    return sentinel.next;
}
```
