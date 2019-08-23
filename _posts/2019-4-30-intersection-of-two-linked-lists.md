---
title:  "160. Intersection of Two Linked Lists"
date:   2019-4-30 20:25:00 +0930
categories: Leetcode
tags: Easy LinkedList TwoPointers
---

[{{page.title}}](https://leetcode.com/problems/intersection-of-two-linked-lists/){:target="_blank"}

    Write a program to find the node at which the intersection of two singly linked lists begins.

    For example, the following two linked lists:

    begin to intersect at node c1.

    Example 1:

    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
    Output: Reference of the node with value = 8
    Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists
    intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5].
    There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

* Easy

Two pointers is a good friends of LinkedList

```java

public ListNode getIntersectionNode(ListNode a, ListNode b) {
    if(a == null || b == null) return null;
    ListNode result = null;
    int l1 = 0, l2 = 0;
    ListNode aa = a, bb = b, pa = null, pb = null;
    while(aa != null) {
        pa = aa;
        aa = aa.next;
        l1++;
    }
    while(bb != null) {
        pb = bb;
        bb = bb.next;
        l2++;
    }
    if(pa != pb) return null;

    ListNode lo = l1 > l2 ? a : b, sh = lo == a ? b : a;
    int offset = Math.abs(l1-l2);
    for(int i = 0; i < offset; i++) {
        lo = lo.next;
    }
    while(lo != null) {
        if(lo == sh) return lo;
        lo = lo.next;
        sh = sh.next;
    }
    return null;
}
```
