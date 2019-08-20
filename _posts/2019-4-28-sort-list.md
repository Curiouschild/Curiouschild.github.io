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

    
* Iterative MergeSort

```java
public ListNode sortList(ListNode head) {
    ListNode n = head;
    int cnt = 0;
    while(n != null) {
        n = n.next;
        cnt++;
    }
    ListNode sentinel = new ListNode(0), sent = null, prev = null, h1 = null, h2 = null, curr = null;
    sentinel.next = head;

    for(int len = 1; len < cnt; len *= 2) {
        sent = sentinel;
        h1 = sent.next;
        h2 = h1;
        while(true) {
            for(int k = 0; k < len && h2 != null; k++) {
                prev = h2;
                h2 = h2.next;
            }
            if(h2 == null) {
                sent.next = h1;
                break;
            }
            prev.next = null;
            ListNode copyH2 = h2;
            for(int k = 0; k < len-1 && copyH2 != null; k++) copyH2 = copyH2.next;
            ListNode nextH1 = null;
            if(copyH2 != null) {
                nextH1 = copyH2.next;
                copyH2.next = null;
            }

            if(h1.val < h2.val) {
                curr = h1;
                h1 = h1.next;
            } else {
                curr = h2;
                h2 = h2.next;
            }
            sent.next = curr;

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

            sent = curr;
            h1 = nextH1;
            h2 = h1;
        }
    }
    return sentinel.next;

}
```

* Recursive MergeSort
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
