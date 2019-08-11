---
title:  "92. Reverse Linked List II"
date:   2019-4-19 21:17:00 +0930
categories: Leetcode
tags: List DataStructure
---

[{{page.title}}](https://leetcode.com/problems/reverse-linked-list-ii/){:target="_blank"}

    Reverse a linked list from position m to n. Do it in one-pass.

    Note: 1 ≤ m ≤ n ≤ length of list.

    Example:

    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL

```java
public ListNode reverseBetween(ListNode head, int m, int n) {
    int cnt = 1;
    ListNode sentinel = new ListNode(0), prev = sentinel, curr = head;
    prev.next = curr;
    while(cnt < m) {
        prev = curr;
        curr = curr.next;
        cnt++;
    }
    while(cnt < n) {
        ListNode moved = curr.next;
        curr.next = moved.next;
        moved.next = prev.next;
        prev.next = moved;
        cnt++;
    }
    return sentinel.next;
}
```
