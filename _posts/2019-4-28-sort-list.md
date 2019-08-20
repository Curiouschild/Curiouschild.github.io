---
title:  "148. Sort List"
date:   2019-4-28 10:36:00 +0930
categories: Leetcode
tags: Medium LinkedList
---

[{{page.title}}](https://leetcode.com/problems/sort-list/){:target="_blank"}

    Sort a linked list in O(n log n) time using constant space complexity.

    Example 1:

    Input: 4->2->1->3
    Output: 1->2->3->4

    Example 2:

    Input: -1->5->3->4->0
    Output: -1->0->3->4->5

```java

public ListNode sortList(ListNode head) {
    if(head == null || head.next == null) return head;
    return mergeSort(head);
}

public ListNode mergeSort(ListNode head) {
    if(head == null || head.next == null) return head;
    ListNode fast = head, slow = head, prev = head;
    while(fast != null) {
        fast = fast.next;
        if(fast != null) {
            fast = fast.next;
            prev = slow;
            slow = slow.next;
        }
    }
    prev.next = null;
    ListNode h1 = mergeSort(head);
    ListNode h2 = mergeSort(slow);

    ListNode curr;
    if(h1.val < h2.val) {
        curr = h1;
        h1 = h1.next;
    } else {
        curr = h2;
        h2 = h2.next;
    }
    ListNode newHead = curr;

    while(h1 != null && h2 != null) {
        if(h1.val < h2.val) {
            curr.next = h1;
            h1 = h1.next;
        } else {
            curr.next = h2;
            h2 = h2.next;
        }
        curr = curr.next;
    }
    ListNode h = h1 != null ? h1 : h2;
    while(h != null) {
        curr.next = h;
        h = h.next;
        curr = curr.next;
    }
    return newHead;
}
```
