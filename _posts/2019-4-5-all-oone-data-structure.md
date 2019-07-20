---
title:  "432. All O`one Data Structure"
date:   2019-4-5 23:35:00 +0930
categories: Leetcode
tags: DataStructure
---

[{{page.title}}](https://leetcode.com/problems/all-oone-data-structure/){:target="_blank"}


    Implement a data structure supporting the following operations:

      Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed
      to be a non-empty string.
      Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing
      key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a
      non-empty string.
      GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty
      string "".
      GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty
      string "".

    Challenge: Perform all these in O(1) time complexity.




```java
class AllOne {
    HashMap<String, Integer> map = new HashMap<>();
    TreeMap<Integer, HashSet<String>> v2k = new TreeMap<>();
    int min;
    int max;
    public AllOne() {

    }

    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    public void inc(String key) {
        map.put(key, map.getOrDefault(key, 0)+1);
        int v = map.get(key);
        if(!v2k.containsKey(v)) v2k.put(v, new HashSet<String>());
        v2k.get(v).add(key);
        if(v > 1) {
            v2k.get(v-1).remove(key);
            if(v2k.get(v-1).isEmpty()) v2k.remove(v-1);
        }

        max = Math.max(max, v);
        if(v-1 == min && !v2k.containsKey(v-1)) min++;
        if(v-1 == 0) min = 1;
    }

    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    public void dec(String key) {
        if(!map.containsKey(key)) return;
        map.put(key, map.get(key)-1);
        int v = map.get(key);
        v2k.get(v+1).remove(key);
        if(v2k.get(v+1).isEmpty()) v2k.remove(v+1);

        if(v == 0) map.remove(key);
        if(!v2k.containsKey(v) && v != 0) v2k.put(v, new HashSet<String>());
        if(v != 0) v2k.get(v).add(key);

        if(v2k.isEmpty()) {
            max = 0;
            min = 0;
        } else {
            if(v+1 == max && !v2k.containsKey(v+1)) max--;
            if(v == 0) {
                min = v2k.ceilingKey(1);
            } else if(v+1 == min && !v2k.containsKey(v+1)) {
                min--;
            }
        }
    }

    /** Returns one of the keys with maximal value. */
    public String getMaxKey() {
        if(v2k.get(max) == null || v2k.get(max).isEmpty()) return "";
        return v2k.get(max).iterator().next();
    }

    /** Returns one of the keys with Minimal value. */
    public String getMinKey() {
        if(v2k.get(min) == null || v2k.get(min).isEmpty()) return "";
        return v2k.get(min).iterator().next();
    }
  }
```
