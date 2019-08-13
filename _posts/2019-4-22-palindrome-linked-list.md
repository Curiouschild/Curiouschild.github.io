---
title:  "234. Palindrome Linked List"
date:   2019-4-22 13:50:00 +0930
categories: Leetcode
tags: Recursive LinkedList
---

[{{page.title}}](https://leetcode.com/problems/palindrome-linked-list){:target="_blank"}


    Given a singly linked list, determine if it is a palindrome.

    Example 1:

    Input: 1->2
    Output: false

    Example 2:

    Input: 1->2->2->1
    Output: true

    Follow up:
    Could you do it in O(n) time and O(1) space?



* Reverse half list

```java

public boolean isPalindrome(ListNode head) {
    if(head == null) return true;
    ListNode fast = head, slow = head;
    while(fast != null) {
        fast = fast.next;
        if(fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
    }

    ListNode sentinel = new ListNode(0), curr = slow;
    sentinel.next = slow;
    while(curr.next != null) {
        ListNode moved = curr.next;
        curr.next = moved.next;
        moved.next = sentinel.next;
        sentinel.next = moved;
    }
    ListNode l1 = head, l2 = sentinel.next;
    while(l1 != slow) {
        if(l1.val != l2.val) return false;
        l1 = l1.next;
        l2 = l2.next;
    }
    return true;
}
```

* Recursive with instance fields

```java

ListNode curr;
boolean isP;
public boolean isPalindromeDFS(ListNode head) {
    curr = head;
    isP = true;
    dfs(head);
    return isP;
}

public void dfs(ListNode head) {
    if(head == null) {
        return;
    }
    dfs(head.next);
    if(curr.val != head.val) {
        isP = false;
    }
    curr = curr.next;
}
```
