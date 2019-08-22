---
title:  "721. Accounts Merge"
date:   2019-4-30 12:08:00 +0930
categories: Leetcode
tags: Medium BFS
---

[{{page.title}}](https://leetcode.com/problems/accounts-merge/){:target="_blank"}

    Given a list accounts, each element accounts[i] is a list of strings, where the first element
    accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

    Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is
    some email that is common to both accounts. Note that even if two accounts have the same name, they may
    belong to different people as people could have the same name. A person can have any number of accounts
    initially, but all of their accounts definitely have the same name.

    After merging the accounts, return the accounts in the following format: the first element of each account
    is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be
    returned in any order.

    Example 1:

    Input:
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John",
    "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John",
    "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
    Explanation:
    The first and third John's are the same person as they have the common email "johnsmith@mail.com".
    The second John and Mary are different people as none of their email addresses are used by other accounts.
    We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John',
    'johnnybravo@mail.com'],
    ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

    Note:
    The length of accounts will be in the range [1, 1000].
    The length of accounts[i] will be in the range [1, 10].
    The length of accounts[i][j] will be in the range [1, 30].


* BFS build a graph

```java

public List<List<String>> accountsMerge(List<List<String>> account) {
    HashMap<String, HashSet<Integer>> map = new HashMap<>();
    boolean[] visited = new boolean[account.size()];
    for(int i = 0; i < account.size(); i++) {
        List<String> l = account.get(i);
        String name = l.get(0);
        for(int j = 1; j < l.size(); j++) {
            String email = l.get(j);
            HashSet<Integer> set = map.getOrDefault(email, new HashSet<>());
            set.add(i);
            map.put(email, set);
        }
    }

    List<List<String>> result = new ArrayList<>();
    for(int i = 0; i < account.size(); i++) {
        if(visited[i]) continue;
        visited[i] = true;
        HashSet<String> temp = new HashSet<>();
        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.offer(i);
        while(!q.isEmpty()) {
            int j = q.poll();
            for(int k = 1; k < account.get(j).size(); k++) {
                String email = account.get(j).get(k);
                temp.add(email);
                for(int n : map.get(email)) {
                    if(!visited[n]) {
                        visited[n] = true;
                        q.offer(n);
                    }
                }
            }
        }
        LinkedList<String> sub = new LinkedList<>(temp);
        Collections.sort(sub);
        sub.addFirst(account.get(i).get(0));
        result.add(sub);
    }
    return result;
}
```
