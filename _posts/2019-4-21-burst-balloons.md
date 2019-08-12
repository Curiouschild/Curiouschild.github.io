---
title:  "312. Burst Balloons"
date:   2019-4-20 12:00:00 +0930
categories: Leetcode
tags: DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/burst-balloons/){:target="_blank"}



    Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array
    nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i]
    * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right
    * then becomes adjacent.

    Find the maximum coins you can collect by bursting the balloons wisely.

    Note:

        You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
        0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

    Example:

    Input: [3,1,5,8]
    Output: 167
    Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
                 coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


* Bottom UP DP

```java
public int maxCoins(int[] arr) {
    int[] nums = new int[arr.length+2];
    nums[0] = 1;
    nums[nums.length-1] = 1;
    System.arraycopy(arr, 0, nums, 1, arr.length);
    int[][] dp = new int[nums.length][nums.length];
    for(int window = 3; window <= nums.length; window++) {
        for(int l = 0; l+window-1 < nums.length; l++) {
            int r = l + window - 1;
            for(int i = l + 1; i < r; i++)
                dp[l][r] = Math.max(dp[l][r], nums[i]*nums[l]*nums[r] + dp[l][i] + dp[i][r]);
        }
    }
    return dp[0][nums.length-1];
}
```

* Recursive MEMO

```java
public int maxCoins(int[] arr) {
    int[][] dp = new int[arr.length+2][arr.length+2];
    int result = backtrack(arr, -1, arr.length, dp);
    return result;
}

public int backtrack(int[] arr, int l, int r, int[][] dp) {
    int result = 0;
    if(dp[l+1][r+1] > 0) return dp[l+1][r+1];
    if(l + 1 == r) return 0;
    for(int i = l + 1; i < r; i++) {
        int center = arr[i] * (l >= 0 ? arr[l] : 1) * (r < arr.length ? arr[r] : 1);
        int left = backtrack(arr, l, i, dp), right = backtrack(arr, i, r, dp);
        result = Math.max(center + left + right, result);
    }
    dp[l+1][r+1] = result;
    return result;
}
```

* Brutal force (TLE)

```java
class Solution {
    HashMap<String, Integer> map = new HashMap<>();
    HashSet<Integer> visited = new HashSet<>();
    public int maxCoins(int[] arr) {
        return go(arr);
    }

    public int go(int[] arr) {
        String key = encode(arr);
        if(map.containsKey(key)) return map.get(key);
        int money = 0;
        for(int index = 0; index < arr.length; index++) {
            if(visited.contains(index)) continue;
            visited.add(index);
            int result = arr[index];
            int left = index-1;
            while(visited.contains(left)) left--;
            int leftValue = left == -1 ? 1 : arr[left];
            int right = index+1;
            while(visited.contains(right)) right++;
            int rightValue = right == arr.length ? 1 : arr[right];
            result *= leftValue * rightValue;
            money = Math.max(money, go(arr) + result);
            visited.remove(index);
        }
        map.put(key, money);
        return money;

    }

    public String encode(int[] arr) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < arr.length; i++) {
            if(!visited.contains(i))
                sb.append(i).append('*');
        }
        return sb.toString();
    }
}
```
