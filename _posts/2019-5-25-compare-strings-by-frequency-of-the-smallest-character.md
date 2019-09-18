---
title:  "1170. Compare Strings by Frequency of the Smallest Character"
date:   2019-05-25 16:23:00 +0930
categories: Leetcode
tags: Easy Binary Search
---

[{{page.title}}](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/){:target="_blank"}

* Binary Search

```java

public int[] numSmallerByFrequency(String[] queries, String[] words) {
    int[] fw = new int[words.length];
    for(int i = 0; i < fw.length; i++)
        fw[i] = f(words[i]);
    Arrays.sort(fw);
    int[] result = new int[queries.length];
    for(int i = 0; i < result.length; i++) {
        result[i] = getCnt(fw, f(queries[i]));
    }
    return result;
}

// find the first index that arr[index] > target
public int getCnt(int[] arr, int target) {
    int l = 0, r = arr.length;
    while(l < r) {
        int mid = l + (r-l) / 2;
        if(arr[mid] <= target) l = mid+1;
        else r = mid;
    }
    return arr.length - l;
}

public int f(String s) {
    int[] arr = new int[26];
    for(char c : s.toCharArray())
        arr[c-'a']++;
    for(int i : arr)
        if(i > 0)
            return i;
    return 0;
}
```
