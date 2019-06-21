---
title:  "380. Insert Delete GetRandom O(1)"
date:   2019-3-12 19:28:10 +0930
categories: Leetcode
tags: HashMap ArrayList DataStructure
---

[{{page.title}}](https://leetcode.com/problems/insert-delete-getrandom-o1/){:target="_blank"}

    Given an array of integers nums, sort the array in ascending order.

    Design a data structure that supports all following operations in average O(1) time.

        insert(val): Inserts an item val to the set if not already present.
        remove(val): Removes an item val from the set if present.
        getRandom: Returns a random element from current set of elements. Each element
                   must have the same probability of being returned.


```java
class RandomizedSet {

    // RANDOM ACCESS --> ARRAY ARRAYLIST
    // O(1) INSERT REMOVE --> HASHMAP
    // MAP<VAL, INDEX>->ARRAYLIST
    // ARRAYLIST<INDEX->VALUE> -> MAP

    HashMap<Integer, Integer> v2i = new HashMap<>();
    ArrayList<Integer> vs = new ArrayList<>();
    Random r = new Random();
    /** Initialize your data structure here. */
    public RandomizedSet() {

    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if(v2i.containsKey(val)) return false;
        v2i.put(val, vs.size());
        vs.add(val);
        return true;
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if(!v2i.containsKey(val)) return false;
        int i = v2i.remove(val);
        int lastV = vs.get(vs.size()-1);
        if(i != vs.size()-1) v2i.put(lastV, i); // rmove the only element in the array, don't update the map
        vs.set(i, lastV);
        vs.remove(vs.size()-1);
        return true;
    }

    /** Get a random element from the set. */
    public int getRandom() {
        int i = vs.size() > 0 ? r.nextInt(vs.size()) : -1;
        return vs.get(i);
    }
}
```
