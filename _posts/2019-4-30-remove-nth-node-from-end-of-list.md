---
title:  "19. Remove Nth Node From End of List"
date:   2019-4-30 09:35:00 +0930
categories: Leetcode
tags: Medium LinkedList TwoPointers
---

[{{page.title}}](https://leetcode.com/problems/remove-nth-node-from-end-of-list/){:target="_blank"}


    Given a linked list, remove the n-th node from the end of list and return its head.

    Example:

    Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list becomes 1->2->3->5.

    Note:

    Given n will always be valid.

    Follow up:

    Could you do this in one pass?



* TowPointers

```java

public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode fast = head, slow = null;
    for(int i = 0; i <= n; i++) {
        if(fast == null) return head.next;
        fast = fast.next;
    }
    slow = head;
    while(fast != null) {
        fast = fast.next;
        slow = slow.next;
    }
    slow.next = slow.next.next;
    return head;
}
```

* Recursive
```java

public ListNode removeNthFromEndRecursive(ListNode head, int n) {
    ListNode sentinel = new ListNode(0);
    sentinel.next = head;
    dfs(sentinel, n);
    return sentinel.next;
}

public Result dfs(ListNode head, int target) {
    if(head == null) return new Result(null, 0);
    Result result = dfs(head.next, target);
    if(result.cnt == target) {
        head.next = result.n.next;
        result.n.next = null;
    }
    result.n = head;
    result.cnt++;
    return result;
}

class Result {
    ListNode n;
    int cnt;
    public Result(ListNode n, int cnt) {
        this.n = n;
        this.cnt = cnt;
    }
}
```
