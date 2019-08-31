---
title:  "975. Odd Even Jump"
date:   2019-05-07 18:18:00 +0930
categories: Leetcode
tags: Hard TreeMap MonotonicStack
---

[{{page.title}}](https://leetcode.com/problems/odd-even-jump/){:target="_blank"}

    You are given an integer array A.  From some starting index, you can make a series of jumps.  The (1st,
    3rd, 5th, ...) jumps in the series are called odd numbered jumps, and the (2nd, 4th, 6th, ...) jumps in
    the series are called even numbered jumps.

    You may from index i jump forward to index j (with i < j) in the following way:

        During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and
        A[j] is the smallest possible value.  If there are multiple such indexes j, you can only jump to the
        smallest such index j.
        During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j]
        and A[j] is the largest possible value.  If there are multiple such indexes j, you can only jump to
        the smallest such index j.
        (It may be the case that for some index i, there are no legal jumps.)

    A starting index is good if, starting from that index, you can reach the end of the array (index A.length
    - 1) by jumping some number of times (possibly 0 or more than once.)

    Return the number of good starting indexes.



    Example 1:

    Input: [10,13,12,14,15]
    Output: 2
    Explanation:
    From starting index i = 0, we can jump to i = 2 (since A[2] is the smallest among A[1], A[2], A[3], A[4]
    that is greater or equal to A[0]), then we can't jump any more.
    From starting index i = 1 and i = 2, we can jump to i = 3, then we can't jump any more.
    From starting index i = 3, we can jump to i = 4, so we've reached the end.
    From starting index i = 4, we've reached the end already.
    In total, there are 2 different starting indexes (i = 3, i = 4) where we can reach the end with some
    number of jumps.

    Example 2:

    Input: [2,3,1,1,4]
    Output: 3
    Explanation:
    From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:

    During our 1st jump (odd numbered), we first jump to i = 1 because A[1] is the smallest value in (A[1],
    A[2], A[3], A[4]) that is greater than or equal to A[0].

    During our 2nd jump (even numbered), we jump from i = 1 to i = 2 because A[2] is the largest value in
    (A[2], A[3], A[4]) that is less than or equal to A[1].  A[3] is also the largest value, but 2 is a smaller
    index, so we can only jump to i = 2 and not i = 3.

    During our 3rd jump (odd numbered), we jump from i = 2 to i = 3 because A[3] is the smallest value in
    (A[3], A[4]) that is greater than or equal to A[2].

    We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.

    In a similar manner, we can deduce that:
    From starting index i = 1, we jump to i = 4, so we reach the end.
    From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
    From starting index i = 3, we jump to i = 4, so we reach the end.
    From starting index i = 4, we are already at the end.
    In total, there are 3 different starting indexes (i = 1, i = 3, i = 4) where we can reach the end with
    some number of jumps.

    Example 3:

    Input: [5,1,3,4,2]
    Output: 3
    Explanation:
    We can reach the end from starting indexes 1, 2, and 4.

    Note:

        1 <= A.length <= 20000
        0 <= A[i] < 100000


The key is to build the two arrays whose value is the next jumpable index of the input array

To build them, use either TreeMap (build as grow) and Monotonic Stacks (Sort by value)

* TreeMap

```java
public int oddEvenJumps(int[] arr) {
    TreeMap<Integer, Integer> map = new TreeMap<>();
    int[] odd = new int[arr.length], even = new int[arr.length];
    for(int i = arr.length-1; i >= 0; i--) {
        Integer up = map.ceilingKey(arr[i]), down = map.floorKey(arr[i]);
        even[i] = down == null ? -1 : map.get(down);
        odd[i] = up == null ? -1 : map.get(up);
        map.put(arr[i], i);
    }

    boolean[][] dp = new boolean[2][arr.length];
    dp[0][arr.length-1] = true;
    dp[1][arr.length-1] = true;
    int cnt = 1;
    for(int i = arr.length-2; i >= 0; i--) {
        dp[0][i] = odd[i] == -1 ? false : dp[1][odd[i]];
        dp[1][i] = even[i] == -1 ? false : dp[0][even[i]];
        if(dp[0][i]) cnt++;
    }
    return cnt;
}

```

* Monotonic Stack

```java
public int oddEvenJumps(int[] arr) {
        int[] odd = build(arr, true);
        int[] even = build(arr, false);
        boolean[][] dp = new boolean[2][arr.length];
        dp[0][arr.length-1] = true; // odd
        dp[1][arr.length-1] = true; // even
        int result = 1;
        for(int i = arr.length-2; i >= 0; i--) {
            dp[0][i] = (odd[i] == -1) ? false : dp[1][odd[i]];
            dp[1][i] = (even[i] == -1) ? false : dp[0][even[i]];
            result += (dp[0][i] ? 1 : 0);
        }
        return result;
    }

    public int[] build(int[] arr, boolean odd) {
        Integer[] index = new Integer[arr.length];
        for(int i = 0; i < arr.length; i++) index[i] = i;
        Arrays.sort(index, (i,j)->(arr[i] == arr[j] ? i-j : (odd ? arr[i]-arr[j] : arr[j]-arr[i])));
        int[] result = new int[arr.length];
        Arrays.fill(result, -1);
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < index.length; i++) {
            while(!stack.isEmpty() && index[i] > stack.peek()) {
                result[stack.pop()] = index[i];
            }
            stack.push(index[i]);
        }
        return result;
    }
```
