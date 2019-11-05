---
title:  "460. LFU Cache"
date:   2019-4-1 21:10:00 +0930
categories: Leetcode
tags: DataStructure HashMap LinkedHashSet
---

[{{page.title}}](https://leetcode.com/problems/lfu-cache/){:target="_blank"}

    Design and implement a data structure for Least Frequently Used (LFU) cache.
    It should support the following operations: get and put.

    get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
    otherwise return -1.
    put(key, value) - Set or insert the value if the key is not already present. When the cache
    reaches its capacity, it should invalidate the least frequently used item before inserting a
    new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that
    have the same frequency), the least recently used key would be evicted.

    Follow up:
    Could you do both operations in O(1) time complexity?

    Example:

    LFUCache cache = new LFUCache( 2 /* capacity */ );

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.get(3);       // returns 3.
    cache.put(4, 4);    // evicts key 1.
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4



```java
class LFUCache {
    int capacity;
    int min;
    int size;
    HashMap<Integer, Integer> map;
    HashMap<Integer, Integer> k2f;
    HashMap<Integer, LinkedHashSet<Integer>> f2k;
    public LFUCache(int capacity){
        this.capacity = capacity;
        map = new HashMap<>();
        k2f = new HashMap<>();
        f2k = new HashMap<>();
        f2k.put(1, new LinkedHashSet<>());
    }
    public int get(int key) {
        if(!map.containsKey(key)) return -1;
        int f = k2f.get(key);
        k2f.put(key, f+1);
        f2k.get(f).remove(key);
        f2k.put(f+1, f2k.getOrDefault(f+1, new LinkedHashSet<>()));
        f2k.get(f+1).add(key);
        if(f2k.get(min).isEmpty()) {
            min++;
        }
        return map.get(key);
    }
    public void put(int key, int val) {
        if(capacity == 0) return;
        if(map.containsKey(key)) {
            map.put(key, val);
            get(key);
        } else {
            map.put(key, val);
            k2f.put(key, 1);
            f2k.get(1).add(key);
            size++;
            if(capacity < size) {
                Iterator<Integer> it = f2k.get(min).iterator();
                int removed = it.next();
                map.remove(removed);
                k2f.remove(removed);
                it.remove();
                size--;
            }
            min = 1;
        }
    }
}
```
