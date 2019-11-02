---
title:  "1244. Design A Leaderboard"
date:   2019-06-27 15:15:00 +0930
categories: Leetcode
tags: Medium Design TreeMap PriorityQueue
---

[{{page.title}}](https://leetcode.com/problems/design-a-leaderboard/){:target="_blank"}

    Design a Leaderboard class, which has 3 functions:

        addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
        top(K): Return the score sum of the top K players.
        reset(playerId): Reset the score of the player with the given id to 0. It is guaranteed that the player was added to the leaderboard before calling this function.

    Initially, the leaderboard is empty.



    Example 1:

    Input:
    ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
    [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
    Output:
    [null,null,null,null,null,null,73,null,null,null,141]

    Explanation:
    Leaderboard leaderboard = new Leaderboard ();
    leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
    leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
    leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
    leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
    leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
    leaderboard.top(1);           // returns 73;
    leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
    leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
    leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
    leaderboard.top(3);           // returns 141 = 51 + 51 + 39;

    Constraints:

        1 <= playerId, K <= 10000
        It's guaranteed that K is less than or equal to the current number of players.
        1 <= score <= 100
        There will be at most 1000 function calls.

* PriorityQueue
  - or treemap without enque and deque

```java

class Leaderboard {
    HashMap<Integer, Player> map = new HashMap<>();
    PriorityQueue<Player> q = new PriorityQueue<>();
    class Player implements Comparable<Player> {
        int id;
        int score;
        public Player(int id) {
            this.id = id;
        }
        public Player(int id, int score) {
            this(id);
            this.score = score;
        }
        public int compareTo(Player p) {
            return Integer.compare(p.score, this.score);
        }
    }
    public Leaderboard() {

    }

    public void addScore(int playerId, int score) {
        Player p = null;
        if(map.containsKey(playerId)) {
            p = map.get(playerId);
            q.remove(p);
            p.score += score;
        } else {
            p = new Player(playerId, score);
            map.put(playerId, p);
        }
        q.offer(p);
    }

    public int top(int K) {
        ArrayList<Player> temp = new ArrayList<>();
        int result = 0;
        for(int i = 0; i < K; i++) {
            Player p = q.poll();
            result += p.score;
            temp.add(p);
        }
        for(Player p : temp) q.offer(p);
        return result;
    }

    public void reset(int playerId) {
        Player p = map.get(playerId);
        q.remove(p);
        p.score = 0;
        q.offer(p);
    }
}
```
