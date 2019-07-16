---
title:  "843. Guess the Word"
date:   2019-4-2 16:13:00 +0930
categories: Leetcode
tags: BFS DFS Graph HashMap HashSet Hard
---

[{{page.title}}](https://leetcode.com/problems/guess-the-word/){:target="_blank"}

    This problem is an interactive problem new to the LeetCode platform.

    We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as secret.

    You may call master.guess(word) to guess a word.  The guessed word should have type string and must be from the original list with 6 lowercase letters.

    This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word.  Also, if your guess is not in the given wordlist, it will return -1 instead.

    For each test case, you have 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or less calls to master.guess and at least one of these guesses was the secret, you pass the testcase.

    Besides the example test case below, there will be 5 additional test cases, each with 100 words in the word list.  The letters of each word in those testcases were chosen independently at random from 'a' to 'z', such that every word in the given word lists is unique.

    Example 1:
    Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

    Explanation:

    master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
    master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
    master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
    master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
    master.guess("abcczz") returns 4, because "abcczz" has 4 matches.

    We made 5 calls to master.guess and one of them was the secret, so we pass the test case.


Random guess (Pass)

```java
  public void findSecretWord(String[] wordlist, Master master) {
      int n = Math.min(10, wordlist.length);
      int[] result = new int[n];
      String[] candidates = new String[n];
      int i = 0;
      int p = 0;
      boolean[] visited = new boolean[wordlist.length];
      Random r = new Random();

      while(true) {
          i = r.nextInt(wordlist.length);
          if(visited[i]) continue;
          visited[i] = true;
          if(!isCandidate(wordlist[i], result, candidates)) {
              continue;
          }
          int guess = master.guess(wordlist[i]);
          if(guess == 6) break;
          if(guess > 0) {
              candidates[p] = wordlist[i];
              result[p++] = guess;
          }
      }
  }

  public boolean isCandidate(String s, int[] result, String[] candidates) {
      for(int i = 0; i < result.length; i++) {
          if(candidates[i] == null) break;
          if(countMatch(candidates[i], s) != result[i]) return false;
      }
      return true;
  }

  public int countMatch(String x, String y) {
      int cnt = 0;
      for(int i = 0; i < x.length(); i++) {
          if(x.charAt(i) == y.charAt(i)) cnt++;
      }
      return cnt;
  }
}
```
A better minmax solution.

```java
class Solution {
    int N = 6;

    public void findSecretWord(String[] words, Master master) {
        Set<Integer> options = new HashSet<>();
        for (int i = 0; i < words.length; i++) options.add(i);
        while (options.size() > 0) {
            int min = Integer.MAX_VALUE;
            int minIdx = -1;
            for (int i : options) {
                int max = maxLoss(i, words, options);
                System.out.println(words[i] + " " + max);
                if (max < min) {
                    min = max;
                    minIdx = i;
                }
            }
            int match = master.guess(words[minIdx]);
            //made the correct guess, return
            if (match == N) return;
            Set<Integer> next = new HashSet<>();
            for (int i : options) {
                if (similarity(words[minIdx], words[i]) == match) {
                    next.add(i);
                }
            }
            options = next;
        }
    }

    private int maxLoss(int wordIdx, String[] words, Set<Integer> options) {
        int[] bucket = new int[N];
        int maxLoss = 0;
        for (int i : options) {
            if (!words[wordIdx].equals(words[i])) {
                int sim = similarity(words[wordIdx], words[i]);
                bucket[sim]++;
                maxLoss = Math.max(maxLoss, bucket[sim]);
            }
        }
        return maxLoss;
    }

    private int similarity(String s1, String s2) {
        int match = 0;
        for (int i = 0; i < N; i++) {
            match += s1.charAt(i) == s2.charAt(i) ? 1 : 0;
        }
        return match;
    }
  }
```
