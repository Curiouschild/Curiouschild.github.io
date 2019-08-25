---
title:  "136. Single Number"
date:   2019-05-03 11:23:00 +0930
categories: Leetcode
tags: Medium Design
---

[{{page.title}}](https://leetcode.com/problems/design-phone-directory/){:target="_blank"}

    Design a Phone Directory which supports the following operations:

        get: Provide a number which is not assigned to anyone.
        check: Check if a number is available or not.
        release: Recycle or release a number.

    Example:

    // Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
    PhoneDirectory directory = new PhoneDirectory(3);

    // It can return any available phone number. Here we assume it returns 0.
    directory.get();

    // Assume it returns 1.
    directory.get();

    // The number 2 is available, so return true.
    directory.check(2);

    // It returns 2, the only number that is left.
    directory.get();

    // The number 2 is no longer available, so return false.
    directory.check(2);

    // Release number 2 back to the pool.
    directory.release(2);

    // Number 2 is available again, return true.
    directory.check(2);


* HashSet

```java
class PhoneDirectory {
    HashSet<Integer> set = new HashSet<>();
    /** Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    public PhoneDirectory(int maxNumbers) {
        for(int i = 0; i < maxNumbers; i++) set.add(i);
    }

    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    public int get() {
        if(set.isEmpty()) return -1;
        int n = set.iterator().next();
        set.remove(n);
        return n;
    }

    /** Check if a number is available or not. */
    public boolean check(int number) {
        return set.contains(number);
    }

    /** Recycle or release a number. */
    public void release(int number) {
        set.add(number);
    }
}
```

* A late adding version

```java
class PhoneDirectory {
    HashSet<Integer> released = new HashSet<>();
    int p;
    int max;
    /** Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    public PhoneDirectory(int maxNumbers) {
        max = maxNumbers;
    }

    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    public int get() {
        if(released.isEmpty() && p == max) return -1;
        if(released.isEmpty()) return p++;
        int v = released.iterator().next();
        released.remove(v);
        return v;
    }

    /** Check if a number is available or not. */
    public boolean check(int number) {
        return number >= p || released.contains(number);
    }

    /** Recycle or release a number. */
    public void release(int number) {
        if(number > p-1) return;
        released.add(number);
    }
}
```
