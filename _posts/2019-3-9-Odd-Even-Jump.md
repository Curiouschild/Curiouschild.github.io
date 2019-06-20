---
title:  "560. Subarray Sum Equals K"
date:   2019-3-9 21:06:33 +0930
categories: Leetcode
tags: MonotonicStack TreeMap DynamicProgramming DynamicMap
---

[{{page.title}}](https://leetcode.com/problems/odd-even-jump/){:target="_blank"}

    You are given an integer array A.  From some starting index, you can make a series of jumps.
    The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps, and the (2nd, 4th,
     6th, ...) jumps in the series are called even numbered jumps.

    You may from index i jump forward to index j (with i < j) in the following way:

        During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that
        A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such
        indexes j, you can only jump to the smallest such index j.
        During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that
         A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j,
         you can only jump to the smallest such index j.
        (It may be the case that for some index i, there are no legal jumps.)

    A starting index is good if, starting from that index, you can reach the end of the array
    (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)

    Return the number of good starting indexes.



    Example 1:

    Input: [10,13,12,14,15]
    Output: 2
    Explanation:
    From starting index i = 0, we can jump to i = 2 (since A[2] is the smallest among
    A[1], A[2], A[3], A[4] that is greater or equal to A[0]), then we can't jump any more.
    From starting index i = 1 and i = 2, we can jump to i = 3, then we can't jump any more.
    From starting index i = 3, we can jump to i = 4, so we've reached the end.
    From starting index i = 4, we've reached the end already.
    In total, there are 2 different starting indexes (i = 3, i = 4) where we can reach the
    end with some number of jumps.



* Dynamic TreeMap

The key is that at each i, all elements currently in the TreeMap have indexes greater than i.


```java
public int oddEvenJumps(int[] A) {
    TreeMap<Integer, Integer> map = new TreeMap<>();
    boolean[][] dp = new boolean[A.length][2];
    Arrays.fill(dp[A.length - 1], true);
    for(int i = A.length - 1; i >= 0; i--) {
        Map.Entry<Integer, Integer> greater = map.ceilingEntry(A[i]), less = map.floorEntry(A[i]);
        if(greater != null) dp[i][0] = dp[greater.getValue()][1];
        if(less != null) dp[i][1] = dp[less.getValue()][0];
        map.put(A[i], i);
    }
    int result = 0;
    for(boolean[] b : dp) result += b[0] ? 1 : 0;
    return result;
}
```

* MonotonicStack

```java
public int oddEvenJumps(int[] A) {
    ArrayList<Node> arr = new ArrayList<>();
    for(int i = 0; i < A.length; i++) arr.add(new Node(A[i], i));

    Collections.sort(arr, new Comparator<Node>() {
        public int compare(Node x, Node y) {
            int r = Integer.compare(x.k, y.k);
            return r == 0 ? Integer.compare(x.v, y.v) : r;
        }
    }); // small to large by value

    Stack<Node> stack = new Stack<>();
    int[] firstLarger = new int[A.length]; // the smallest greater elements with greater index
    Arrays.fill(firstLarger, -1);
    for(Node n : arr) {
        while(!stack.isEmpty() && n.v > stack.peek().v)
            firstLarger[stack.pop().v] = n.v;
        stack.push(n);
    }

    Collections.sort(arr, new Comparator<Node>() {
        public int compare(Node x, Node y) {
            int r = Integer.compare(y.k, x.k);
            return r == 0 ? Integer.compare(x.v, y.v) : r;
        }
    }); // large to small by value

    stack = new Stack<>();
    int[] firstSmaller = new int[A.length]; // the largest smaller elements with greater index
    Arrays.fill(firstSmaller, -1);
    for(Node n : arr) {
        while(!stack.isEmpty() && n.v > stack.peek().v)
            firstSmaller[stack.pop().v] = n.v;
        stack.push(n);
    }

    // dynamic programming in reverse order
    boolean[][] dp = new boolean[A.length][2];
    Arrays.fill(dp[A.length - 1], true);
    for(int i = A.length - 2; i >= 0; i--) {
        dp[i][0] = firstLarger[i] != -1 && dp[firstLarger[i]][1];
        dp[i][1] = firstSmaller[i] != -1 && dp[firstSmaller[i]][0];
    }
    int result = 0;
    for(boolean[] b : dp) result += b[0] ? 1 : 0;
    return result;
}

class Node {
    int v;
    int k;
    public Node(int k, int v) { this.v = v; this.k = k;}
}
 ```
