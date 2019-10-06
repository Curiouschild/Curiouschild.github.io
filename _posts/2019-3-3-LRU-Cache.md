---
title:  "146. LRU Cache"
date:   2019-3-3 10:04:03 +0930
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

public class LRUCache {
    HashMap<Integer, Node> map = new HashMap<>();
    Node sentinel, tail;
    int size;
    private final int capacity;
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        sentinel = new Node(-1,-1);
    }
    public int get(int key) {
        if(!map.containsKey(key)) return -1;
        Node n = map.get(key);
        moveToTail(n);
        return n.value;
    }

    public void moveToTail(Node n) {
        if(n == tail) return;
        Node p = n.prev, next = n.next;
        p.next = next;
        next.prev = p;

        tail.next = n;
        n.prev = tail;

        tail = n;

    }

    public void put(int key, int value) {
        if(this.capacity == 0) return;
        if(map.containsKey(key)) {
            Node n = map.get(key);
            n.value = value;
            moveToTail(n);
        } else {
            Node n = new Node(key, value);
            map.put(key, n);
            if(tail == null) {
                sentinel.next = n;
                n.prev = sentinel;
            } else {
                tail.next = n;
                n.prev = tail;
            }
            tail = n;
            size++;
            if(size > this.capacity) {
                map.remove(sentinel.next.key);
                sentinel.next = sentinel.next.next;
                sentinel.next.prev = sentinel;
                size--;
            }
        }


    }
    class Node {
        int key, value;
        Node prev, next;
        public Node(int k, int v) {
            key = k;
            value = v;
        }
    }
}
```
