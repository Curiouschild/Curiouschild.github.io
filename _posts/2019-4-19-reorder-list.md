---
title:  "143. Reorder List"
date:   2019-4-18 21:06:00 +0930
categories: Leetcode
tags: List DataStructure
---

[{{page.title}}](https://leetcode.com/problems/reorder-list/){:target="_blank"}


    Given a singly linked list L: L0→L1→…→Ln-1→Ln,
    reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

    You may not modify the values in the list's nodes, only nodes itself may be changed.

    Example 1:

    Given 1->2->3->4, reorder it to 1->4->2->3.

    Example 2:

    Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

* Reverse the Second half of the list

```java
class Solution { // middle reverse and reorder

    public void reorderList(ListNode head) {
        if(head == null || head.next == null) return;
        ListNode fast = head, slow = head;
        while(fast != null) {
            fast = fast.next;
            if(fast != null) {
                fast = fast.next;
                slow = slow.next;
            }
        }
        ListNode sentinel = new ListNode(0), curr = slow;
        sentinel.next = curr;
        while(curr.next != null) {
            ListNode moved = curr.next;
            curr.next = moved.next;
            moved.next = sentinel.next;
            sentinel.next = moved;
        }

        ListNode l1 = head, l2 = sentinel.next;
        curr = sentinel;
        while(l1 != slow) {
            curr.next = l1;
            l1 = l1.next;
            curr = curr.next;
            curr.next = l2;
            l2 = l2.next;
            curr = curr.next;
        }
        if(l2 != null) curr.next = l2;
        sentinel.next = null;
    }
  }
```

* Stack
```java
public void reorderList2(ListNode head) {
    if(head == null || head.next == null) return;
    ListNode fast = head, slow = head;
    while(fast != null) {
        fast = fast.next;
        if(fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
    }

    LinkedList<ListNode> stack = new LinkedList<>();
    ListNode curr = slow;
    while(curr != null) {
        stack.push(curr);
        curr = curr.next;
    }

    ListNode prev = new ListNode(0);
    ListNode l1 = head, l2 = null;
    while(l1 != slow) {
        prev.next = l1;
        l1 = l1.next;
        prev = prev.next;
        l2 = stack.pop();
        prev.next = l2;
        prev = prev.next;
    }
    if(!stack.isEmpty()) {
        prev.next = stack.pop();
        prev = prev.next;
    }
    prev.next = null;
}
```
