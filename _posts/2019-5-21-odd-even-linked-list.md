---
title:  "328. Odd Even Linked List"
date:   2019-05-21 16:29:00 +0930
categories: Leetcode
tags: Medium Array
---

[{{page.title}}](https://leetcode.com/problems/odd-even-linked-list/){:target="_blank"}

    Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we
    are talking about the node number and not the value in the nodes.

    You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time
    complexity.

    Example 1:

    Input: 1->2->3->4->5->NULL
    Output: 1->3->5->2->4->NULL

    Example 2:

    Input: 2->1->3->5->6->4->7->NULL
    Output: 2->3->6->7->1->5->4->NULL

    Note:

        The relative order inside both the even and odd groups should remain as it was in the input.
        The first node is considered odd, the second node even and so on ...

* One pass

```java
public ListNode oddEvenList(ListNode head) {
    if(head == null || head.next == null || head.next.next == null) return head;
    ListNode odd = head, prev = head.next, curr = head.next.next;
    // prev always even, curr always odd
    // move curr behind the odd
    while(curr != null) {
        prev.next = curr.next;
        curr.next = odd.next;
        odd.next = curr;
        odd = odd.next;
        prev = prev.next;
        if(prev == null) break;
        curr = prev.next;
    }
    return head;
}
```

* Move odd to left for one step in a single traverse O(N2)

This approach is a trash...

```java
public ListNode oddEvenList(ListNode head) {
    if(head == null) return null;
    ListNode curr = head, prev = null;
    int len = 1;
    while(curr.next != null) {
        prev = curr;
        curr = curr.next;
        len++;
    }
    ListNode tail = null;
    if(len % 2 == 1) {
        len--;
        if(len > 1) {
            tail = curr;
            prev.next = null;
        }
    }
    curr = head;
    ListNode n = null;
    while(len >= 4) {
        int i = len - 2;
        prev = curr;
        n = prev.next;
        while(i > 0) {
            prev.next = n.next;
            n.next = n.next.next;
            prev.next.next = n;
            prev = prev.next.next;
            n = prev.next;
            i -= 2;
        }
        curr = curr.next;
        len -= 2;
    }
    if(tail != null) {
        tail.next = curr.next;
        curr.next = tail;
    }
    return head;
}
```
