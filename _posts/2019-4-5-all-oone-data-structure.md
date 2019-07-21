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

* HashMap + DoublyLinkedList

```java

class AllOne {
    HashMap<String, Integer> map = new HashMap<>();
    HashMap<Integer, Node> v2k = new HashMap<>();
    Node head, tail;
    public AllOne() {}

    public void inc(String key) {
        // System.out.println("++" + key);
        if(!map.containsKey(key)) {
            Node nh = v2k.getOrDefault(1, new Node(1));
            v2k.put(1, nh);
            nh.keys.add(key);
            if(head == null) {
                head = nh;
                tail = head;
            } else if(head != nh) {
                nh.next = head;
                head.prev = nh;
                head = nh;
            }
        } else {
            int v = map.get(key);
            Node curr = v2k.get(v), nn = v2k.getOrDefault(v+1, new Node(v+1));
            v2k.put(v+1, nn);
            nn.keys.add(key);
            curr.keys.remove(key);
            if(nn != curr.next) {
                nn.next = curr.next;
                if(curr.next != null) curr.next.prev = nn;
                curr.next = nn;
                nn.prev = curr;
            }
            if(curr == tail) tail = nn;
            if(curr.keys.isEmpty()) {
                v2k.remove(curr.v);
                if(curr == head) {
                    head = nn;
                    nn.prev = null;
                } else {
                    curr.prev.next = nn;
                    nn.prev = curr.prev;
                }
                curr.next = null;
                curr.prev = null;
            }
        }
        map.put(key, map.getOrDefault(key, 0)+1);
        // print();
    }

    public void dec(String key) {
        if(!map.containsKey(key)) return;
        // System.out.println("--" + key);
        int v = map.get(key);
        Node curr = v2k.get(v);
        curr.keys.remove(key);
        if(v == 1) {
            map.remove(key);
            if(curr.keys.isEmpty()) {
                v2k.remove(v);
                head = curr.next;
                if(curr == tail) tail = null;
                curr.prev = null;
                curr.next = null;
            }
        } else {
            map.put(key, v-1);
            Node np = v2k.getOrDefault(v-1, new Node(v-1));
            v2k.put(v-1, np);
            np.keys.add(key);

            np.next = curr;
            if(curr == head) {
                head = np;
            } else if(np != curr.prev) {
                curr.prev.next = np;
                np.prev = curr.prev;
            }
            curr.prev = np;

            if(curr.keys.isEmpty()) {
                v2k.remove(v);
                if(curr == head) {
                    head = np;
                }
                if(curr == tail) {
                    tail = np;
                } else {
                    np.next = curr.next;
                    curr.next.prev = np;
                }

                curr.next = null;
                curr.prev = null;
            }
        }
        // print();

    }
    public String getMinKey() {
        if(head == null) return "";
        return head.keys.iterator().next();
    }
    public String getMaxKey() {
        if(tail == null) return "";
        return tail.keys.iterator().next();
    }


    class Node {
        Node prev;
        Node next;
        int v;
        HashSet<String> keys = new HashSet<String>();
        public Node(int v) {
            this.v = v;
        }
        public String toString() {
            return keys.toString();
        }
    }

    public void print() {
        Node curr = head;
        System.out.println("v2k" + v2k);
         System.out.println("h=" + (curr == null ? "null" : head.keys) + " t=" + (tail == null ? "null" : tail.keys));
        while(curr != null) {
            System.out.println(curr.v + " ->" + curr.keys);
            curr = curr.next;
        }
        System.out.println();
    }
}

```


* TreeMap nlogn

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
