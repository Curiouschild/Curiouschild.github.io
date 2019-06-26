---
title:  "332. Reconstruct Itinerary"
date:   2019-3-16 17:07:23 +0930
categories: Leetcode
tags:  Graph
---

[{{page.title}}](https://leetcode.com/problems/reconstruct-itinerary/){:target="_blank"}

    Given a list of airline tickets represented by pairs of departure and arrival
    airports [from, to], reconstruct the itinerary in order. All of the tickets
    belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

    Note:

        If there are multiple valid itineraries, you should return the itinerary that
        has the smallest lexical order when read as a single string. For example, the
        itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
        All airports are represented by three capital letters (IATA code).
        You may assume all tickets form at least one valid itinerary.

    Example 1:

    Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Euler path.
Another option to run faster but more space: HashMap<from, PriorityQueue<to1, to2...>>

```java
public List<String> findItinerary(List<List<String>> tickets) {
    Collections.sort(tickets, new Comparator<List<String>>() {
        public int compare(List<String> x, List<String> y) {
            return x.get(1).compareTo(y.get(1));
        }
    });
    LinkedList<String> result = new LinkedList<>();
    dfs(result, "JFK", tickets, new boolean[tickets.size()]);
    return result;

}

public void dfs(LinkedList<String> result, String curr, List<List<String>> tickets, boolean[] used) {
    for(int i = 0; i < tickets.size(); i++) {
        if(!used[i] && tickets.get(i).get(0).equals(curr)) {
            used[i] = true;
            dfs(result, tickets.get(i).get(1), tickets, used);
        }
    }
    result.addFirst(curr);
}
```
