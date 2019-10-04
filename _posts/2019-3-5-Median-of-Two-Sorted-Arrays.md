---
title:  "4. Median of Two Sorted Arrays"
date:   2019-3-5 18:35:33 +0930
categories: Leetcode
tags: BinarySearch
---

[4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/){:target="_blank"}

    There are two sorted arrays nums1 and nums2 of size m and n respectively.

    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

    You may assume nums1 and nums2 cannot be both empty.


```java
public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    int[] la = nums1.length >= nums2.length ? nums1 : nums2;
    int[] sa = la == nums2 ? nums1 : nums2;
    if(la.length == sa.length) { // check if the answer only includes all elements from the shorter arr
        if(sa[la.length-1] <= la[0]) return (double)(sa[la.length-1] + la[0])/2;
    }
    int half = (la.length + sa.length + 1) / 2; // 6->3 ; 5->3
    int left = 0, right = la.length-1;
    while(left <= right) {
        int i1 = (right + left) / 2; // i1 means the smaller half includes the elements from index i1 to 0 in the longer arr
        int len1 = i1 + 1;
        int len2 = half - len1;
        int i2 = len2 - 1; // the same as i2
        int ll = getArrValue(i1, la); // array index bound checking
        int lr = getArrValue(i1+1, la);
        int sl = getArrValue(i2, sa);
        int sr = getArrValue(i2+1, sa);

        if(ll <= sr && lr >= sl) { // binary search
            if(total % 2 == 0) return (Math.max(ll, sl) + Math.min(lr, sr)) / (double)2;
            else return (double)Math.max(ll, sl);
        } else if(ll > sr) {
            right = i1 - 1;
        } else if(lr < sl) {
            left = i1 + 1;
        }
    }
    return 0;
}

public int getArrValue(int index, int[] arr) {
    return index >= arr.length ? Integer.MAX_VALUE : index >= 0 ? arr[index] : Integer.MIN_VALUE;
}
```

* Conscise

```java

public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    if(nums1.length > nums2.length) {
        int[] temp = nums1;
        nums1 = nums2;
        nums2 = temp;
    }
    int n = nums1.length, m = nums2.length;
    int l = 0, r = n;
    boolean odd = ((n + m) & 1) == 1;
    double result = 0.0;
    int half = (m + n +1) / 2;
    while(l <= r) {
        int mid = l + (r-l) / 2;
        int inN = mid;
        int inM = half - inN;
        int i = inN-1, j = inM - 1;
        int nl = i < 0 ? Integer.MIN_VALUE : nums1[i];
        int nr = i == n-1 ? Integer.MAX_VALUE : nums1[i+1];
        int ml = j < 0 ? Integer.MIN_VALUE : nums2[j];
        int mr = j == m-1 ? Integer.MAX_VALUE : nums2[j+1];
        if(nl <= mr && ml <= nr) {
            if(odd) {
                return (double) Math.max(nl, ml);
            } else {
                return (Math.max(nl, ml) + Math.min(nr, mr)) / 2.0;
            }
        } else if(nl > mr) {
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    return 0.0;
}
```
