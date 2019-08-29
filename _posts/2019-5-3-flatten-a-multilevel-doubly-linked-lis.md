---
title:  "430. Flatten a Multilevel Doubly Linked List"
date:   2019-05-03 17:03:00 +0930
categories: Leetcode
tags: Medium LinkedList
---

[{{page.title}}](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-lis/){:target="_blank"}

    You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

    Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.



    Example:

    Input:
     1---2---3---4---5---6--NULL
             |
             7---8---9---10--NULL
                 |
                 11--12--NULL

    Output:
    1-2-3-7-8-11-12-9-10-4-5-6-NULL


* Preprocess the special case: the tail has a child.

```java
/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;

    public Node() {}

    public Node(int _val,Node _prev,Node _next,Node _child) {
        val = _val;
        prev = _prev;
        next = _next;
        child = _child;
    }
};
*/
class Solution {
    public Node flatten(Node head) {
        // System.out.println(head.val);
        build(head);
        return head;
    }
    public Node build(Node head) {
        // System.out.println(head.val);
        if(head == null) return null;
        Node tail = head, prev = head;

        while(tail != null) {
            if(tail.next == null && tail.child != null) {
                Node child = tail.child;
                tail.next = child;
                child.prev = tail;
                tail.child = null;
            }
            prev = tail;
            tail = tail.next;
        }
        tail = prev;
        Node curr = head;
        while(curr != tail) {
            Node next = curr.next;
            if(curr.child != null) {
                Node child = curr.child;
                curr.child = null;
                Node childTail = build(child);
                curr.next = child;
                child.prev = curr;
                childTail.next = next;
                next.prev = childTail;
            }
            curr = next;
        }
        return tail;
    }
}
```
