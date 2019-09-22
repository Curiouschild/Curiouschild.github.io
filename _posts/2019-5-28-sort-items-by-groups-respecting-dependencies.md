---
title:  "1203. Sort Items by Groups Respecting Dependencies"
date:   2019-05-28 23:53:00 +0930
categories: Leetcode
tags: Hard Graph TopologicalSort
---

[{{page.title}}](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/){:target="_blank"}

    There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item
    belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero
    indexed. A group can have no item belonging to it.

    Return a sorted list of the items such that:

        The items that belong to the same group are next to each other in the sorted list.
        There are some relations between these items where beforeItems[i] is a list containing all the items
        that should come before the i-th item in the sorted array (to the left of the i-th item).

    Return any solution if there is more than one solution and return an empty list if there is no solution.



    Example 1:

    Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
    Output: [6,3,4,1,5,2,0,7]

    Example 2:

    Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
    Output: []
    Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.



    Constraints:

        1 <= m <= n <= 3*10^4
        group.length == beforeItems.length == n
        -1 <= group[i] <= m-1
        0 <= beforeItems[i].length <= n-1
        0 <= beforeItems[i][j] <= n-1
        i != beforeItems[i][j]
        beforeItems[i] does not contain duplicates elements.


* two level topological sort on groups and items


```java

public int[] sortItems(int n, int m, int[] group, List<List<Integer>> beforeItems) {
    for(int i = 0; i < group.length; i++)
        if(group[i] == -1)
            group[i] = m++; // assign none-group elements a group

    int[] inG = new int[m]; // indegree of groups
    int[] inI = new int[n]; // indegree of items
    ArrayList<Integer>[] graphI = new ArrayList[n]; // graph of groups: before group -> after groups
    ArrayList<Integer>[] graphG = new ArrayList[m]; // graph of items: before item -> after items
    ArrayList<Integer>[] g2i = new ArrayList[m]; // group index -> item indexes
    for(int i = 0; i < m; i++) g2i[i] = new ArrayList<>();
    for(int i = 0; i < n; i++) graphI[i] = new ArrayList<>();
    for(int i = 0; i < m; i++) graphG[i] = new ArrayList<>();

    for(int i = 0; i < group.length; i++) g2i[group[i]].add(i);
    for(int i = 0; i < beforeItems.size(); i++) {
        List<Integer> l = beforeItems.get(i);
        for(int b : l) {
            if(group[i] != group[b]) { // order between differnt groups
                graphG[group[b]].add(group[i]);
                inG[group[i]]++;
            } else { // order between items within a group
                inI[i]++;
                graphI[b].add(i);
            }
        }
    }
    // Level1: the code below is a topological sort on the groups
    PriorityQueue<Integer> q = new PriorityQueue<>();
    for(int i = 0; i < m; i++) {
        if(inG[i] == 0) q.offer(i);
    }
    ArrayList<ArrayList<Integer>> orderG = new ArrayList<>();
    while(!q.isEmpty()) {
        int b = q.poll(); // current group with indgree equals 0


        // Level 2: the code below is a topological sort on items within a group
        ArrayList<Integer> temp = new ArrayList<>();
        PriorityQueue<Integer> iq = new PriorityQueue<>();
        for(int i : g2i[b]) {
            if(inI[i] == 0) iq.offer(i);
        }
        while(!iq.isEmpty()) {
            int ib = iq.poll();
            temp.add(ib);
            for(int ia : graphI[ib]) {
                inI[ia]--;
                if(inI[ia] == 0) {
                    iq.offer(ia);
                }
            }
        }
        if(temp.size() != g2i[b].size()) return new int[]{}; // invalid result
        orderG.add(temp); // add the sorted group items into result
        // END inner sort


        for(int after : graphG[b]) { // add new groups with indgree equals 0 into the queue
            inG[after]--;
            if(inG[after] == 0) {
                q.offer(after);
            }
        }
    }
    if(orderG.size() != m) return new int[] {};
    // END outer sort

    int[] result = new int[n];
    int cnt = 0;
    for(ArrayList<Integer> l : orderG) {
        for(int i : l) result[cnt++] = i;
    }
    return result;
}
```
