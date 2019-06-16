---
title:  "146. LRU Cache"
date:   2019-3-3 010:04:03 +0930
categories: Leetcode
tags: LinkedHashMap DataStructure
---

[146. LRU Cache](https://leetcode.com/problems/lru-cache/){:target="_blank"}

    Design and implement a data structure for Least Recently Used (LRU) cache.
    It should support the following operations: get and put.

    get(key) - Get the value (will always be positive) of the key if the key exists
     in the cache, otherwise return -1.
    put(key, value) - Set or insert the value if the key is not already present.
    When the cache reached its capacity, it should invalidate the least recently used
     item before inserting a new item.

    The cache is initialized with a positive capacity.

1. Ordered Map Version
```java
class LRUCache extends LinkedHashMap<Integer, Integer> {
    int capacity;
    public LRUCache(int capacity) {
        super(capacity, 0.75f, true);
        this.capacity = capacity;
    }
    public boolean removeEldestEntry(Map.Entry<Integer,Integer> en) {
        return this.size() > capacity;
    }
    public int get(int key) {
        return super.getOrDefault(key, -1);
    }

    public void put(int key, int value) {
        super.put(key, value);
    }
}
```
2. HashMap + Doubly LinkedList Version

```java
class LRUCache {
    int capacity;
    int size;
    HashMap<Integer, Node> map = new HashMap<>();
    Node head;
    Node tail;
    public LRUCache(int capacity) {
        this.capacity = capacity;
    }
    public int get(int key) {
        Node n = this.map.getOrDefault(key, null);
        if(n == null) return -1;
        moveToTail(n);
        return n.val;
    }

    public void removeHead() {
        Node newHead = head.next;
        newHead.pre = null;
        head.next = null;
        map.remove(head.key);
        head = newHead;
        size--;
    }

    public void put(int key, int val) {
        Node n = null;
        if(map.containsKey(key)) {
            n = map.get(key);
            n.val = val;
            moveToTail(n);
        } else {
            size++;
            n = new Node(key, val);
            map.put(key, n);
            if(tail != null) {
                tail.next = n;
                n.pre = tail;
                tail = n;
            } else {
                head = n;
                tail = n;
            }
            if(size > capacity) removeHead();
        }
    }

    public void moveToTail(Node n) {
        if(n == tail) return;
        if(n != head) {
            Node pre = n.pre;
            pre.next = n.next;
            n.next.pre = pre;
            n.next = null;
            n.pre = null;
        } else {
            head = n.next;
            head.pre = null;
            n.next = null;
        }
        tail.next = n;
        n.pre = tail;
        tail = n;
    }

    class Node {
        int val;
        int key;
        Node pre;
        Node next;
        public Node(int k, int v) { val = v; key = k;}
    }
}
```
