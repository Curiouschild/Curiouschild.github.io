---
title:  "670. Maximum Swap"
date:   2019-05-04 11:12:00 +0930
categories: Leetcode
tags: Medium Math
---

[{{page.title}}](https://leetcode.com/problems/maximum-swap/){:target="_blank"}

    Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

    Example 1:

    Input: 2736
    Output: 7236
    Explanation: Swap the number 2 and the number 7.

    Example 2:

    Input: 9973
    Output: 9973
    Explanation: No swap.

    Note:

        The given number is in the range [0, 108]

* Build a right max number array

```java
class Solution {
    public int maximumSwap(int num) {
        int len = 0;
        int n = num;
        while(n > 0) {
            len++;
            n /= 10;
        }
        int[] rightMax = new int[len], arr = new int[len];
        n = num;

        for(int i = len-1; i >= 0; i--) {
            arr[i] = n % 10;
            n /= 10;
            rightMax[i] = (i+1 <= len-1) ? Math.max(rightMax[i+1], arr[i+1]) : -1;
        }

        for(int i = 0; i < len; i++) {
            if(rightMax[i] > arr[i]) {
                int max = i, j = i+1;
                for(; j < len; j++) {
                    max = arr[max] <= arr[j] ? j : max;
                }
                int temp = arr[max];
                arr[max] = arr[i];
                arr[i] = temp;
                break;
            }
        }
        int result = 0;
        for(int i : arr) result = result * 10 + i;
        return result;
    }
```

* Sorting Very Slow

```java
class Solution {
    public int maximumSwap(int num) {
        ArrayList<int[]> arr = new ArrayList<>();
        int n = num;
        while(n > 0) {
            arr.add(new int[] {arr.size(), n % 10});
            n = n / 10;
        }
        ArrayList<int[]> origin = new ArrayList<>(arr);
        Collections.reverse(origin);
        Collections.sort(arr, (a,b)->(a[1]-b[1]==0? a[0]-b[0] : b[1]-a[1]));
        for(int i = 0; i < arr.size(); i++) {
            if(arr.get(i)[1] == origin.get(i)[1]) continue;
            int j = i;
            while(j-1 >= 0 && arr.get(j)[1] == arr.get(j-1)[1]) {
                j--;
            }
            int oi = arr.size()-1-arr.get(j)[0];
            int[] temp = origin.get(oi);
            origin.set(oi, origin.get(i));
            origin.set(i, temp);
            break;
        }

        int result = 0;
        for(int i = 0; i < origin.size(); i++) {
            result = result * 10 + origin.get(i)[1];
        }
        return result;
    }
```
