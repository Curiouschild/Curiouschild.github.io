---
title:  "1157. Online Majority Element In Subarray"
date:   2019-06-25 23:36:00 +0930
categories: Leetcode
tags: Hard BinarySearch
---

[{{page.title}}](https://leetcode.com/problems/online-majority-element-in-subarray/){:target="_blank"}

    Implementing the class MajorityChecker, which has the following API:

        MajorityChecker(int[] arr) constructs an instance of MajorityChecker with the given array arr;
        int query(int left, int right, int threshold) has arguments such that:
            0 <= left <= right < arr.length representing a subarray of arr;
            2 * threshold > right - left + 1, ie. the threshold is always a strict majority of the length of
            the subarray

    Each query(...) returns the element in arr[left], arr[left+1], ..., arr[right] that occurs at least
    threshold times, or -1 if no such element exists.

    Example:

    MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
    majorityChecker.query(0,5,4); // returns 1
    majorityChecker.query(0,3,3); // returns -1
    majorityChecker.query(2,3,2); // returns 2

    Constraints:

        1 <= arr.length <= 20000
        1 <= arr[i] <= 20000
        For each query, 0 <= left <= right < len(arr)
        For each query, 2 * threshold > right - left + 1
        The number of queries is at most 10000


* Randomness and binarySearch

```java

class MajorityChecker {
    HashMap<Integer, ArrayList<Integer>> map;
    Random r = new Random();
    int[] arr;
    public MajorityChecker(int[] arr) {
        this.arr = arr;
        this.map = new HashMap<>();
        for(int i = 0; i < arr.length; i++) {
            ArrayList<Integer> temp = map.getOrDefault(arr[i], new ArrayList<>());
            temp.add(i);
            map.put(arr[i], temp);
        }
    }

    public int check(int left, int right, int threshold) {
        int index = left + this.r.nextInt(right-left+1);
        ArrayList<Integer> temp = map.get(arr[index]);
        int l = Collections.binarySearch(temp, left);
        int r = Collections.binarySearch(temp, right);
        if(l < 0) l = -l-1;
        if(r < 0) r = -r-2;
        if(r-l+1 < threshold) return -1;
        return arr[index];
    }

    public int query(int left, int right, int threshold) {
        for(int i = 0; i < 30; i++) {
            int result = check(left, right, threshold);
            if(result != -1) return result;
        }
        return -1;
    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * MajorityChecker obj = new MajorityChecker(arr);
 * int param_1 = obj.query(left,right,threshold);
 */
```
