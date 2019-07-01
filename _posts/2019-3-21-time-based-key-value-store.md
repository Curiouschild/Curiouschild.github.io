---
title:  "981. Time Based Key-Value Store"
date:   2019-3-20 16:40:00 +0930
categories: Leetcode
tags: DataStructure TreeMap BinarySearch HashMap
---

[{{page.title}}](https://leetcode.com/problems/time-based-key-value-store/){:target="_blank"}

    Create a timebased key-value store class TimeMap, that supports two operations.

    1. set(string key, string value, int timestamp)

        Stores the key and value, along with the given timestamp.

    2. get(string key, int timestamp)

        Returns a value such that set(key, value, timestamp_prev) was called previously,
        with timestamp_prev <= timestamp.
        If there are multiple such values, it returns the one with the largest timestamp_prev.
        If there are no values, it returns the empty string ("").


* BinarySearch

```java

HashMap<String, ArrayList<Node>> map;
/** Initialize your data structure here. */
public TimeMap() {
    map = new HashMap<>();
}

public void set(String key, String value, int timestamp) {
    ArrayList<Node> arr = map.getOrDefault(key, new ArrayList<>());
    arr.add(new Node(timestamp, value));
    map.put(key, arr);
}

public String get(String key, int timestamp) {
    if(!map.containsKey(key)) return "";
    return binarySearch(map.get(key), timestamp);
}

// find the first element less than or equal to target
// convert to find the first element greater than the target, then minus one from the index
public String binarySearch(ArrayList<Node> arr, int target) {
    int l = 0, r = arr.size();
    while(l < r) {
        int mid = (l+r) / 2;
        if(arr.get(mid).k <= target) l = mid + 1;
        else r = mid;
    }
    r--;
    if(r == -1) return "";
    return arr.get(r).v;
}


class Node {
    int k;
    String v;
    public Node(int k, String v) {
        this.k = k; this.v = v;
    }
}
```

* TreeMap

```java

class TimeMap {
    HashMap<String, TreeMap<Integer, String>> map;
    public TimeMap() {
        map = new HashMap<>();
    }
    public String get(String key, int timestamp) {
        if(!map.containsKey(key)) return "";
        else {
            TreeMap<Integer, String> tree = map.get(key);
            Map.Entry<Integer, String> e = tree.floorEntry(timestamp);
            return e == null ? "" : e.getValue();
        }
    }

    public void set(String key, String value, int timestamp) {
        TreeMap<Integer, String> tree = map.getOrDefault(key, new TreeMap<>());
        tree.put(timestamp, value);
        map.put(key, tree);
    }
  }
```
