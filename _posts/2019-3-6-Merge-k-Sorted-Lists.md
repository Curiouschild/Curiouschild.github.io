---
title:  "23. Merge k Sorted Lists"
date:   2019-3-6 15:22:31 +0930
categories: Leetcode
tags: PriorityQueue
---

[{{page.title}}](https://leetcode.com/problems/merge-k-sorted-lists/){:target="_blank"}

    Merge k sorted linked lists and return it as one sorted list.
    Analyze and describe its complexity.

1. PriorityQueue

```java
public ListNode mergeKLists(ListNode[] lists) {
    PriorityQueue<ListNode> q = new PriorityQueue<>(new Comparator<ListNode>() {
        public int compare(ListNode x, ListNode y) {
            return Integer.compare(x.val, y.val);
        }
    });
    ListNode sentinel = new ListNode(0), curr = sentinel;
    for(ListNode root : lists) {
        if(root != null) q.offer(root);
    }
    while(!q.isEmpty()) {
        ListNode poped = q.poll();
        curr.next = poped;
        curr = curr.next;
        if(poped.next != null) q.offer(poped.next);
    }
    return sentinel.next;
}
```
2. One Pass

```java
public int maxSubArray(int[] nums) {
    int result = Integer.MIN_VALUE, sum = 0;
    for(int n : nums) {
        sum = sum + n < 0 ? 0 : sum + n; // reset sum when it becoming negative
        result = n < 0 ? Math.max(result, n) : Math.max(result, sum); // imaging an array with only negative elements
    }
    return result;
}
```
