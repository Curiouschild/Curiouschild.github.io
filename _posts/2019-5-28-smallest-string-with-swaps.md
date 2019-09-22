---
title:  "1202. Smallest String With Swaps"
date:   2019-05-28 22:53:00 +0930
categories: Leetcode
tags: Medium Graph UnionFind
---

[{{page.title}}](https://leetcode.com/problems/smallest-string-with-swaps/){:target="_blank"}

    You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b]
    indicates 2 indices(0-indexed) of the string.

    You can swap the characters at any pair of indices in the given pairs any number of times.

    Return the lexicographically smallest string that s can be changed to after using the swaps.



    Example 1:

    Input: s = "dcab", pairs = [[0,3],[1,2]]
    Output: "bacd"
    Explaination:
    Swap s[0] and s[3], s = "bcad"
    Swap s[1] and s[2], s = "bacd"

    Example 2:

    Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
    Output: "abcd"
    Explaination:
    Swap s[0] and s[3], s = "bcad"
    Swap s[0] and s[2], s = "acbd"
    Swap s[1] and s[2], s = "abcd"

    Example 3:

    Input: s = "cba", pairs = [[0,1],[1,2]]
    Output: "abc"
    Explaination:
    Swap s[0] and s[1], s = "bca"
    Swap s[1] and s[2], s = "bac"
    Swap s[0] and s[1], s = "abc"



    Constraints:

        1 <= s.length <= 10^5
        0 <= pairs.length <= 10^5
        0 <= pairs[i][0], pairs[i][1] < s.length
        s only contains lower case English letters.





* UnionFind


```java

public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
    ArrayList<HashSet<Integer>> groups = new ArrayList<>();
    UnionFind uf = new UnionFind(s.length());
    for(List<Integer> l : pairs) {
        int x = l.get(0), y = l.get(1);
        uf.union(x, y);
    }
    HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
    for(int i = 0; i < s.length(); i++) {
        int root = uf.find(i);
        ArrayList<Integer> arr = map.getOrDefault(root, new ArrayList<>());
        arr.add(i);
        map.put(root, arr);
    }


    StringBuilder sb = new StringBuilder(s);
    for(Integer root : map.keySet()) {
        ArrayList<Integer> indexes = map.get(root);
        ArrayList<Character> arr = new ArrayList<>();
        for(int j : indexes) {
            arr.add(s.charAt(j));
        }
        Collections.sort(arr);
        Collections.sort(indexes);
        int k = 0;
        for(int j : indexes) {
            sb.setCharAt(j, arr.get(k++));
        }
    }
    return sb.toString();
}

class UnionFind {
    int[] arr;
    public UnionFind(int n) {
        arr = new int[n];
        for(int i = 0; i < n; i++) {
            arr[i] = i;
        }
    }

    public int find(int x) {
        if(arr[x] != x) arr[x] = find(arr[x]);
        return arr[x];
    }

    public void union(int x, int y) {
        int a = find(x), b = find(y);
        if(a != b) {
            arr[b] = a;
        }
    }
}
```
