---
title:  "126. Word Ladder II"
date:   2019-4-1 23:03:00 +0930
categories: Leetcode
tags: BFS DFS Graph HashMap HashSet Hard
---

[{{page.title}}](https://leetcode.com/problems/word-ladder-ii/){:target="_blank"}

    Given two words (beginWord and endWord), and a dictionary's word list, find all shortest
    transformation sequence(s) from beginWord to endWord, such that:

        Only one letter can be changed at a time
        Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

    Note:

        Return an empty list if there is no such transformation sequence.
        All words have the same length.
        All words contain only lowercase alphabetic characters.
        You may assume no duplicates in the word list.
        You may assume beginWord and endWord are non-empty and are not the same.

    Example 1:

    Input:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]

    Output:
    [
      ["hit","hot","dot","dog","cog"],
      ["hit","hot","lot","log","cog"]
    ]




```java
HashMap<String, HashSet<String>> dict = new HashMap<>();
public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
    wordList.add(beginWord);
    for(String w : wordList) {
        StringBuilder sb = new StringBuilder(w);
        for(int i = 0; i < w.length(); i++) {
            sb.setCharAt(i, '*');
            String key = sb.toString();
            if(!dict.containsKey(key)) dict.put(key, new HashSet<String>());
            dict.get(key).add(w);
            sb.setCharAt(i, w.charAt(i));
        }
    }

    ArrayList<HashSet<String>> arr = new ArrayList<>();
    ArrayDeque<String> q = new ArrayDeque<>();
    q.offer(beginWord);
    HashSet<String> visited = new HashSet<>();
    visited.add(beginWord);
    boolean find = false;
    while(!q.isEmpty()) {
        HashSet<String> currLevel = new HashSet<String>();
        int size = q.size();
        for(int j = 0; j < size; j++) {
            String w = q.poll();
            visited.add(w);
            StringBuilder sb = new StringBuilder(w);
            for(int i = 0; i < w.length(); i++) {
                sb.setCharAt(i, '*');
                String key = sb.toString();
                if(dict.containsKey(key)) {
                    for(String next : dict.get(key)) {
                        if(next.equals(endWord)) find = true;
                        if(!visited.contains(next)) {
                            q.offer(next);
                            currLevel.add(next);
                        }
                    }
                }
                sb.setCharAt(i, w.charAt(i));
            }
        }
        if(find) break;
        arr.add(currLevel);
    }

    List<List<String>> result = new ArrayList<List<String>>();
    dfs(result, arr, new LinkedList<String>(), new HashSet<String>(), arr.size()-1, beginWord, endWord);
    return result;
}

public void dfs(List<List<String>> result, ArrayList<HashSet<String>> arr, LinkedList<String> temp, HashSet<String> visited, int level, String endWord, String w) {
        visited.add(w);
        temp.add(w);
        StringBuilder sb = new StringBuilder(w);
        for(int i = 0; i < w.length(); i++) {
            sb.setCharAt(i, '*');
            String key = sb.toString();

            if(dict.containsKey(key)) {
                for(String next : dict.get(key)) {
                    if(next.equals(endWord)) {
                        temp.add(endWord);
                        ArrayList<String> toAdd = new ArrayList<String>(temp);
                        Collections.reverse(toAdd);
                        result.add(toAdd);
                        temp.remove(temp.size()-1);
                    } else if(!visited.contains(next) && level >= 0 && arr.get(level).contains(next)) {

                        dfs(result, arr, temp, visited, level-1, endWord, next);
                    }
                }
            }
            sb.setCharAt(i, w.charAt(i));
        }
        temp.remove(temp.size()-1);
        visited.remove(w);
}
```
