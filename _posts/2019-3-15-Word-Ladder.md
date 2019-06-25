---
title:  "127. Word Ladder"
date:   2019-3-15 18:11:22 +0930
categories: Leetcode
tags: BFS String Graph
---

[{{page.title}}](){:target="_blank"}


    Given two words (beginWord and endWord), and a dictionary's word list, find the
    length of shortest transformation sequence from beginWord to endWord, such that:

        Only one letter can be changed at a time.
        Each transformed word must exist in the word list. Note that beginWord is not a
        transformed word.

    Note:

        Return 0 if there is no such transformation sequence.
        All words have the same length.
        All words contain only lowercase alphabetic characters.
        You may assume no duplicates in the word list.
        You may assume beginWord and endWord are non-empty and are not the same.

    Example 1:

    Input:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]

    Output: 5

    Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.

"abc" -> "\*ab", "a\*c", "ab\*"

```java
public int ladderLength(String s, String e, List<String> ws) {
    HashMap<String, ArrayList<String>> map = new HashMap<>();
    for(String w : ws) {
        for(int i = 0; i < w.length(); i++) {
            char[] arr = w.toCharArray();
            char c = arr[i];
            arr[i] = '*';
            String starWord = new String(arr);
            ArrayList<String> nexts = map.getOrDefault(starWord, new ArrayList<String>());
            nexts.add(w);
            map.put(starWord, nexts);
            arr[i] = c;
        }
    }
    Queue<String> q = new ArrayDeque<String>();
    q.offer(s);
    int level = 0;
    int result = Integer.MAX_VALUE;
    HashSet<String> visited = new HashSet<>();
    while(!q.isEmpty()) {
        int size = q.size();
        level++;
        for(int k = 0; k < size; k++) {
            String w = q.poll();
            for(int i = 0; i < w.length(); i++) {
                char[] arr = w.toCharArray();
                char c = arr[i];
                arr[i] = '*';
                String starWord = new String(arr);
                if(!map.containsKey(starWord)) continue;
                ArrayList<String> nexts = map.get(starWord);
                for(String next : nexts) {
                    if(next.equals(e)) return level + 1;
                    if(!visited.contains(next)) {
                        visited.add(next);
                        q.offer(next);
                    }
                }
                arr[i] = c;
            }
        }
    }
    return 0;
}
```
