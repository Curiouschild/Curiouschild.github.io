---
title:  "138. Copy List with Random Pointer"
date:   2019-3-7 23:33:22 +0930
categories: Leetcode
tags: LinkedList Copy
---

[{{page.title}}](https://leetcode.com/problems/copy-list-with-random-pointer/){:target="_blank"}

    A linked list is given such that each node contains an additional
    random pointer which could point to any node in the list or null.

    Return a deep copy of the list.

  ![Example1](/img/posts/copy_list_with_random_pointer.png)

* Recursive

```java
public Node copyRandomList(Node head) {
    return recursive(head, new HashMap<Node, Node>());
}

public Node recursive(Node head, HashMap<Node, Node> map) {
    if(head == null) return null;
    if(map.containsKey(head)) return map.get(head);
    Node newHead = new Node();
    map.put(head, newHead);
    newHead.val = head.val;
    newHead.next = recursive(head.next, map);
    newHead.random = recursive(head.random, map);
    return newHead;
}
```
