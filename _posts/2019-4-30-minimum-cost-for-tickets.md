---
title:  "983. Minimum Cost For Tickets"
date:   2019-4-30 19:14:00 +0930
categories: Leetcode
tags: Medium DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/minimum-cost-for-tickets/){:target="_blank"}

    In a country popular for train travel, you have planned some train travelling one year in advance.  The
    days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

    Train tickets are sold in 3 different ways:

        a 1-day pass is sold for costs[0] dollars;
        a 7-day pass is sold for costs[1] dollars;
        a 30-day pass is sold for costs[2] dollars.

    The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then
    we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

    Return the minimum number of dollars you need to travel every day in the given list of days.

    Example 1:

    Input: days = [1,4,6,7,8,20], costs = [2,7,15]
    Output: 11
    Explanation:
    For example, here is one way to buy passes that lets you travel your travel plan:
    On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
    On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
    On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
    In total you spent $11 and covered all the days of your travel.

    Example 2:

    Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
    Output: 17
    Explanation:
    For example, here is one way to buy passes that lets you travel your travel plan:
    On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
    On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
    In total you spent $17 and covered all the days of your travel.


* DP
dp(i) : total cast from today to the end of this year

if this is a travel day
  dp(i)=min(dp(j1)+costs[0],dp(j7)+costs[1],dp(j30)+costs[2])
else
 dp(i) = dp(i+1)

```java
public int mincostTickets(int[] days, int[] costs) {
    int[] dp = new int[366];
    HashSet<Integer> set = new HashSet<>();
    for(int i : days) set.add(i);
    for(int i = 365; i >= 1; i--) {
        if(set.contains(i)) {
            dp[i] = Math.min(costs[0] + (i+1 > 365 ? 0 : dp[i+1]), costs[1] + (i+7 > 365 ? 0 : dp[i+7]));
            dp[i] = Math.min(dp[i], costs[2] + (i+30 > 365 ? 0 : dp[i+30]));

        } else {
            dp[i] = i == 365 ? 0 : dp[i+1];
        }
    }
    return dp[1];
}
```

* Another version depends on days array

dp(i)=min(dp(j1)+costs[0],dp(j7)+costs[1],dp(j30)+costs[2])

```java
public int mincostTickets(int[] days, int[] costs) {
    int[] dp = new int[days.length], times = {1, 7, 30};
    Arrays.fill(dp, Integer.MAX_VALUE);
    for(int i = days.length-1; i >=0 ; i--) {
        int j = i;
        for(int k = 0; k < 3; k++) {
            while(j < days.length && days[j] < days[i] + times[k]) j++;
            dp[i] = Math.min(dp[i], (j >= days.length ? 0 : dp[j]) + costs[k]);
        }
    }
    return dp[0];
}
```
