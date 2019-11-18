---
title:  "382. Linked List Random Node"
date:   2019-11-17 19:09:00 +0930
categories: Leetcode
tags: Medium Randomness
---

[{{page.title}}](https://leetcode.com/problems/linked-list-random-node/){:target="_blank"}

    Given a singly linked list, return a random node's value from the linked list. Each node must have the same
    probability of being chosen.

    Follow up:
    What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently
    without using extra space?

    Example:

    // Init a singly linked list [1,2,3].
    ListNode head = new ListNode(1);
    head.next = new ListNode(2);
    head.next.next = new ListNode(3);
    Solution solution = new Solution(head);

    // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
    solution.getRandom();


```java

class Solution {
    ListNode head;
    Random random = new Random();
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    public Solution(ListNode head) {
        this.head = head;
    }

    /** Returns a random node's value. */
    public int getRandom() {
        ListNode curr = head;
        int r = curr.val;
        for(int i=1; curr.next != null; i++){
            curr = curr.next;
            if(random.nextInt(i + 1) == i)
                r = curr.val;
        }
        return r;
    }
}
```
