---
title:  "353. Design Snake Game"
date:   2019-05-02 23:04:00 +0930
categories: Leetcode
tags: Medium Design Deque
---

[{{page.title}}](https://leetcode.com/problems/design-snake-game/){:target="_blank"}

    Given a non-empty array of integers, every element appears twice except for one. Find that single one.

    Note:

    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Example 1:

    Input: [2,2,1]
    Output: 1

    Example 2:

    Input: [4,1,2,1,2]
    Output: 4

* Double ended queue

I tried to use a hashset to record the body of the snake, but it is much slower than a leaner search
over the queue. why???

```java
class SnakeGame {
    ArrayDeque<Node> q = new ArrayDeque<>();
    int p;
    int score;
    int[][] food;
    int n, m;
    /** Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0]. */
    public SnakeGame(int w, int h, int[][] food) {
        q.offer(new Node(0, 0));
        this.food = food;
        n = h;
        m = w;
    }

    class Node {
        int i;
        int j;
        public Node(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }

    /** Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body. */
    public int move(String direction) {
        Node curr = q.peekLast(), tail = q.peekFirst();
        int ni = curr.i, nj = curr.j, ti = tail.i, tj = tail.j;
        switch(direction) {
            case "U" : ni--; break;
            case "D" : ni++; break;
            case "L" : nj--; break;
            case "R" : nj++;
        }
        if(ni < 0 || nj < 0 || ni >= n || nj >= m) return -1;
        if(p == food.length || !(ni == food[p][0] && nj == food[p][1])) { // not eat, give up the tail
            q.pollFirst();
        }  else {
            score++;
            p++;
        }
        for(Node n : q) {
            if(ni == n.i && nj == n.j) return -1;
        }

        Node nh = new Node(ni, nj);
        q.offerLast(nh);
        return p;
    }
}
```


* MLE failed on a 10000 * 10000 matrix input.

```java
class SnakeGame {
    int[][] matrix;
    int fp;
    int score;
    Node head, tail;
    HashMap<String, int[]> map = new HashMap<>();
    int[][] food;
    /** Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0]. */
    public SnakeGame(int width, int height, int[][] food) {
        this.food = food;
        matrix = new int[height][width];
        if(food.length > 0) matrix[food[fp][0]][food[fp++][1]] = 2;
        matrix[0][0] = 1;
        head = new Node(0, 0);
        tail = head;
        map.put("U", new int[]{-1,0});
        map.put("D", new int[]{1,0});
        map.put("L", new int[]{0,-1});
        map.put("R", new int[]{0,1});
    }

    class Node {
        int i;
        int j;
        Node next;
        public Node(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }

    /** Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body. */
    public int move(String direction) {
        int[] d = map.get(direction);
        int i = head.i + d[0], j = head.j + d[1];
        if(i < 0 || j < 0 || i >= matrix.length || j >= matrix[0].length) {
            return -1;
        }
        if(matrix[i][j] == 1 && !(i == tail.i && j == tail.j)) return -1;
        Node newHead = new Node(i, j);
        head.next = newHead;
        head = newHead;

        if(matrix[i][j] != 2) {
            matrix[tail.i][tail.j] = 0;
            Node newTail = tail.next;
            tail.next = null;
            tail = newTail;
        }
        if(matrix[i][j] == 2) { // food
            score++;
            if(fp < food.length)
                matrix[food[fp][0]][food[fp++][1]] = 2;
        }
        matrix[i][j] = 1;
        return score;
    }
```
