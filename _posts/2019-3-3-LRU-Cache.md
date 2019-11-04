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

class LRUCache {
    int capacity;
    int size;
    Node sentinel, tail;
    HashMap<Integer, Node> map = new HashMap<>(); // key->Node
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.sentinel = new Node(0, 0);
    }
    
    public int get(int key) {
        if(!map.containsKey(key)) return -1;
        Node curr = map.get(key);
        if(curr != this.tail) {
            Node prev = curr.prev, next = curr.next;
            prev.next = next;
            next.prev = prev;
            this.tail.next = curr;
            curr.prev = this.tail;
            this.tail = curr;
        }
        return curr.val;
    }

    public void put(int key, int val) {
        if(this.capacity == 0) return;
        Node n;
        if(map.containsKey(key)) {
            n = map.get(key);
            n.val = val;
            this.get(key);
        } else { // add to list and map
            n = new Node(key, val);
            map.put(key, n);
            if(this.tail == null) {
                sentinel.next = n;
                n.prev = sentinel;
            } else {
                this.tail.next = n;
                n.prev = tail;
            }
            tail = n;
            this.size++;
            if(this.size > this.capacity) {
                // remove from list and map
                Node removed = sentinel.next;
                sentinel.next = removed.next;
                removed.next.prev = sentinel;
                map.remove(removed.key);
                this.size--;
            }
        }
    }

    class Node {
        Node next, prev;
        int key, val;
        public Node(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }
}
```
