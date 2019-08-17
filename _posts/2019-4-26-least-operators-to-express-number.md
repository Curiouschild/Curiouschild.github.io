---
title:  "964. Least Operators to Express Number"
date:   2019-4-26 13:49:00 +0930
categories: Leetcode
tags: DFS DynamicProgramming Hard
---

[{{page.title}}](https://leetcode.com/problems/least-operators-to-express-number/){:target="_blank"}

    Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ...
    where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *,
    or /).  For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.

    When writing such an expression, we adhere to the following conventions:

        The division operator (/) returns rational numbers.
        There are no parentheses placed anywhere.
        We use the usual order of operations: multiplication and division happens before addition and
        subtraction.
        It's not allowed to use the unary negation operator (-).  For example, "x - x" is a valid expression as
        it only uses subtraction, but "-x + x" is not because it uses negation.

    We would like to write an expression with the least number of operators such that the expression equals the
    given target.  Return the least number of operators used.

    Example 1:

    Input: x = 3, target = 19
    Output: 5
    Explanation: 3 * 3 + 3 * 3 + 3 / 3.  The expression contains 5 operations.

    Example 2:

    Input: x = 5, target = 501
    Output: 8
    Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.  The expression contains 8 operations.

* Dijkstra

```java
public int leastOpsExpressTarget(int x, int target) {
    PriorityQueue<int[]> q = new PriorityQueue<>((a,b)->(a[0]-b[0]));
    HashSet<Integer> visited = new HashSet<>();
    q.offer(new int[]{0,target});
    while(!q.isEmpty()) {
        int[] arr = q.poll();
        int cost = arr[0], remain = arr[1];
        if(visited.contains(remain)) continue;
        visited.add(remain);
        if(remain == 0) return cost-1;
        int k = (int)Math.floor(Math.log(remain) / Math.log(x));
        int xk = (int)Math.pow(x, k);
        q.offer(new int[]{cost+(k==0 ? 2:k), remain-xk});
        q.offer(new int[]{cost+k+1, Math.abs(remain-xk*x)});
    }
    return -1;
}
```

* Top Down DP

```java

HashMap<Integer, Integer> map = new HashMap<>();
public int leastOpsExpressTarget(int x, int target) {
    return dp(x, target)-1;
}
public int dp(int x, int t) {
    if(map.containsKey(t)) return map.get(t);
    if(t == 0) return 0;
    if(t < x) return Math.min(2*t, 2*(x-t)+1);
    int k = (int)Math.floor(Math.log(t) / Math.log(x));
    int xk = (int)Math.pow(x, k);
    int t1 = t - xk, t2 = Math.abs(xk * x - t);
    int result = dp(x, t1)+k;
    if(t2 < t) result = Math.min(result, dp(x, t2)+k+1);
    map.put(t, result);
    return result;
}
```
