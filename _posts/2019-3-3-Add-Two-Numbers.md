---
title:  "2. Add Two Numbers"
date:   2019-3-3 09:11:03 +0930
categories: Leetcode
tags: HashMap TwoPointer
---

[2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/){:target="_blank"}

    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order and each of their nodes contain a single
    digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.


```java
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    int carry = 0;
    ListNode sentinel = new ListNode(0);
    ListNode curr = sentinel;
    while(l1 != null || l2 != null) {
        int x = l1 == null ? 0 : l1.val;
        int y = l2 == null ? 0 : l2.val;
        int sum = x + y + carry;
        carry = sum / 10;
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        l1 = l1 == null ? null : l1.next;
        l2 = l2 == null ? null : l2.next;
    }
    if(carry != 0) curr.next = new ListNode(1);
    return sentinel.next;
}
```
