---
title:  "86. Partition List"
date:   2019-05-29 12:04:00 +0930
categories: Leetcode
tags: Medium LinkedList
---

[{{page.title}}](https://leetcode.com/problems/partition-list/){:target="_blank"}


    Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater
    than or equal to x.

    You should preserve the original relative order of the nodes in each of the two partitions.

    Example:

    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5

```java

public ListNode partition(ListNode head, int x) {
    ListNode sentinel = new ListNode(0);
    sentinel.next = head;
    ListNode boundary = sentinel, prev = sentinel, curr = head;
    while(curr != null) {
        if(curr.val < x && boundary != prev) {
            prev.next = curr.next;
            curr.next = boundary.next;
            boundary.next = curr;
            boundary = boundary.next;
            curr = prev.next;
        } else {
            if(curr.val < x && boundary == prev)
                boundary = boundary.next;
            prev = prev.next;
            curr = curr.next;
        }
    }
    return sentinel.next;
}
```
