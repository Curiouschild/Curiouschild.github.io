---
title:  "871. Minimum Number of Refueling Stops"
date:   2019-06-04 18:45:00 +0930
categories: Leetcode
tags: Hard Greedy DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/minimum-number-of-refueling-stops/){:target="_blank"}

    A car travels from a starting position to a destination which is target miles east of the starting position.

    Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0]
    miles east of the starting position, and has station[i][1] liters of gas.

    The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1
    liter of gas per 1 mile that it drives.

    When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into
    the car.

    What is the least number of refueling stops the car must make in order to reach its destination?  If it
    cannot reach the destination, return -1.

    Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car
    reaches the destination with 0 fuel left, it is still considered to have arrived.



    Example 1:

    Input: target = 1, startFuel = 1, stations = []
    Output: 0
    Explanation: We can reach the target without refueling.

    Example 2:

    Input: target = 100, startFuel = 1, stations = [[10,100]]
    Output: -1
    Explanation: We can't reach the target (or even the first gas station).

    Example 3:

    Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
    Output: 2
    Explanation:
    We start with 10 liters of fuel.
    We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
    Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
    and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
    We made 2 refueling stops along the way, so we return 2.



    Note:

        1 <= target, startFuel, stations[i][1] <= 10^9
        0 <= stations.length <= 500
        0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target

* PriorityQueue greedy

```java

public int minRefuelStops(int target, int startFuel, int[][] stations) {
    if(stations.length == 0) return startFuel >= target ? 0 : -1;
    PriorityQueue<Integer> q = new PriorityQueue<>((a,b)->(b-a));
    int result = 0, fuel = startFuel;
    for(int i = 0; i < stations.length; i++) {
        fuel -= stations[i][0] - (i-1 >= 0 ? stations[i-1][0] : 0);
        while(fuel < 0) {
            if(q.isEmpty()) return -1;
            fuel += q.poll();
            result++;
        }
        q.offer(stations[i][1]);
    }
    fuel -= target - stations[stations.length-1][0];
    while(fuel < 0) {
        if(q.isEmpty()) return -1;
        fuel += q.poll();
        result++;
    }
    return result;
}
```
