---
title:  "713. Subarray Product Less Than K"
date:   2019-05-27 12:05:00 +0930
categories: Leetcode
tags: Medium Array
---

[{{page.title}}](https://leetcode.com/problems/subarray-product-less-than-k/){:target="_blank"}

    Your are given an array of positive integers nums.

    Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray
    is less than k.

    Example 1:

    Input: nums = [10, 5, 2, 6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2],
    [2, 6], [5, 2, 6].
    Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

    Note:
    0 < nums.length <= 50000.
    0 < nums[i] < 1000.
    0 <= k < 10^6.

* sliding window

Consider sliding window greedy first when the sum/product is ordered.
                        binary Search         arr            ordered
                        dp                    problem has    overlapped sub problems

```java
public int numSubarrayProductLessThanK(int[] nums, int k) {
    int result = 0;
    int j = 0, i = 0;
    int product = 1;
    while(i < nums.length) {
        product *= nums[i];
        while(j <= i && product >= k) {
            product /= nums[j++];
        }
        int n = i-j+1;
        result += n;
        i++;
    }
    return result;
}
```

* A failed binary search on prefix product array

A feasible way is to change the prefix product of origin array into a prefix log sum array

```java

public int numSubarrayProductLessThanK(int[] nums, int k) {
     int result = 0;
     double[] arr = new double[nums.length];
     arr[0] = nums[0];
     for(int i = 1; i < arr.length; i++) {
         arr[i] = arr[i-1] * nums[i];
     }
     for(int i = 0; i < nums.length; i++) {
         int l = 0, r = i;
         while(l <= r) {
             int mid = l + (r-l) / 2;
             double product = arr[i] / arr[mid] * nums[mid];
             if(product >= k) {
                 l = mid + 1;
             } else {
                 if(l == r) break;
                 r = mid;
             }
         }
         int cnt = i - l + 1;
         result += cnt;
     }
     return result;
 }
```

* log sum; for reference

```java
class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k == 0) return 0;
        double logk = Math.log(k);
        double[] prefix = new double[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            prefix[i+1] = prefix[i] + Math.log(nums[i]);
        }

        int ans = 0;
        for (int i = 0; i < prefix.length; i++) {
            int lo = i + 1, hi = prefix.length;
            while (lo < hi) {
                int mi = lo + (hi - lo) / 2;
                if (prefix[mi] < prefix[i] + logk - 1e-9) lo = mi + 1;
                else hi = mi;
            }
            ans += lo - i - 1;
        }
        return ans;
    }
}
```
