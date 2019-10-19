---
title:  "1228. Missing Number In Arithmetic Progression"
date:   2019-06-21 15:14:00 +0930
categories: Leetcode
tags: Easy BinarySearch
---

[{{page.title}}](https://leetcode.com/problems/critical-connections-in-a-network/){:target="_blank"}

    In some array arr, the values were in arithmetic progression: the values arr[i+1] - arr[i] are all equal
    for every 0 <= i < arr.length - 1.

    Then, a value from arr was removed that was not the first or last value in the array.

    Return the removed value.

    Example 1:

    Input: arr = [5,7,11,13]
    Output: 9
    Explanation: The previous array was [5,7,9,11,13].

    Example 2:

    Input: arr = [15,13,12]
    Output: 14
    Explanation: The previous array was [15,14,13,12].

    Constraints:

      3 <= arr.length <= 1000
      0 <= arr[i] <= 10^5

```java

public int missingNumber(int[] arr) {
    int l = 0, r = arr.length-1;
    while(l < r) {
        int mid = l + (r-l) / 2;
        double left = (double)Math.abs((arr[mid]-arr[0])) / (mid+1);
        double right = (double)Math.abs((arr[arr.length-1]-arr[mid])) / (arr.length-mid);
        if(left <= right) {
            l = mid+1;
        } else {
            r = mid;
        }
    }
    return (arr[r]+arr[r-1]) / 2;
}
```
