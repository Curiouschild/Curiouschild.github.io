---
title:  "212. Word Search II"
date:   2019-4-3 20:33:00 +0930
categories: Leetcode
tags: Backtracking Tier
---

[{{page.title}}](https://leetcode.com/problems/word-search-ii/){:target="_blank"}



    Given a 2D board and a list of words from the dictionary, find all words in the board.

    Each word must be constructed from letters of sequentially adjacent cell, where "adjacent"
    cells are those horizontally or vertically neighboring. The same letter cell may not be used
    more than once in a word.

    Example:

    Input:
    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]

    Output: ["eat","oath"]


* Tier

```java
int[] xs = {0,0,1,-1}, ys = {1,-1,0,0};
public List<String> findWords(char[][] board, String[] words) {
    Node root = new Node(); // root represents empty string ""
    for(String w : words) {
        Node curr = root;
        for(int i = 0; i < w.length(); i++) {
            if(curr.arr[w.charAt(i)-'a'] == null)
                curr.arr[w.charAt(i)-'a'] = new Node();
            curr = curr.arr[w.charAt(i)-'a'];
        }
        curr.w = w;
    }
    List<String> result = new ArrayList<>();
    for(int i = 0; i < board.length; i++) {
        for(int j = 0; j < board[0].length; j++) {
            backtrack(result, board, i, j, root);
        }
    }
    return result;
}

public void backtrack(List<String> result, char[][] board, int i, int j, Node curr) {
    char c = board[i][j];
    if(curr.arr[c-'a'] == null) return;
    if(curr.arr[c-'a'].w != null) {
        result.add(curr.arr[c-'a'].w);
        curr.arr[c-'a'].w = null;
    }

    board[i][j] = '*';
    for(int k = 0; k < 4; k++) {
        int x = i + xs[k], y = j + ys[k];
        if(x >= 0 && y >= 0 && x < board.length && y < board[0].length && board[x][y] != '*')
            backtrack(result, board, x, y, curr.arr[c-'a']);
    }
    board[i][j] = c;
}

class Node {
    Node[] arr = new Node[26];
    String w;
}
```
