---
title:  "206. Reverse Linked List"
date:   2019-3-6 023:55:25 +0930
categories: Leetcode
tags: LinkedList
---

[{{page.title}}](https://leetcode.com/problems/reverse-linked-list/){:target="_blank"}

    Reverse a singly linked list.

    Example:

    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL


1. Recursive

```java
public ListNode reverseList(ListNode head) {
    if(head == null || head.next == null) return head;
    ListNode newHead = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return newHead;
}
```
2. Iterative

```java
public ListNode reverseListIterative(ListNode head) {
    ListNode sentinel = new ListNode(0), curr = head;
    sentinel.next = curr;
    while(curr != null && curr.next != null) {
        ListNode next = curr.next;
        curr.next = next.next;
        next.next = sentinel.next;
        sentinel.next = next;
    }
    return sentinel.next;
}

```
