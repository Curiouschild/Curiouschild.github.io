---
title:  "708. Insert into a Cyclic Sorted List"
date:   2019-05-04 12:45:00 +0930
categories: Leetcode
tags: Medium LinkedList
---

[{{page.title}}](https://leetcode.com/problems/insert-into-a-cyclic-sorted-list/){:target="_blank"}


    Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a
    value into the list such that it remains a cyclic sorted list. The given node can be a reference to any
    single node in the list, and may not be necessarily the smallest value in the cyclic list.

    If there are multiple suitable places for insertion, you may choose any place to insert the new value.
    After the insertion, the cyclic list should remain sorted.

    If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the
    reference to that single node. Otherwise, you should return the original given node.

    The following example may help you understand the problem better:


![img1](/img/posts/insert-into-a-cyclic-sorted-list-1.png)


    In the figure above, there is a cyclic sorted list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list.


![img1](/img/posts/insert-into-a-cyclic-sorted-list-1.png)

    The new node should insert between node 1 and node 3. After the insertion, the list should look like this,
    and we should still return node 3.


* trival



```java
class Solution {
    public Node insert(Node head, int insertVal) {
        Node n = new Node(insertVal);
        if(head == null) {
            n.next = n;
            return n;
        }
        if(head.next == head) {
            head.next = n;
            n.next = head;
            return head;
        }
        Node largest = head;
        while(largest.next.val >= largest.val && largest.next != head) largest = largest.next;
        Node smallest = largest.next;
        if(n.val <= smallest.val || n.val >= largest.val) {
            largest.next = n;
            n.next = smallest;
            return head;
        }
        Node prev = head;
        while(!(prev.val <= n.val && prev.next.val >= n.val)) {
            prev = prev.next;
            if(prev == head) break;
        }
        n.next = prev.next;
        prev.next = n;
        return head;
    }
}
```
