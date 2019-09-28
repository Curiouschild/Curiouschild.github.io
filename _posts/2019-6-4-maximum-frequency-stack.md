---
title:  "895. Maximum Frequency Stack"
date:   2019-06-03 12:31:00 +0930
categories: Leetcode
tags: Hard DataStructure
---

[{{page.title}}](https://leetcode.com/problems/maximum-frequency-stack/){:target="_blank"}

    Implement FreqStack, a class which simulates the operation of a stack-like data structure.

    FreqStack has two functions:

        push(int x), which pushes an integer x onto the stack.
        pop(), which removes and returns the most frequent element in the stack.
            If there is a tie for most frequent element, the element closest to the top of the stack is
            removed and returned.


    Example 1:

    Input:
    ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
    [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
    Output: [null,null,null,null,null,null,null,5,7,5,4]
    Explanation:
    After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

    pop() -> returns 5, as 5 is the most frequent.
    The stack becomes [5,7,5,7,4].

    pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
    The stack becomes [5,7,5,4].

    pop() -> returns 5.
    The stack becomes [5,7,4].

    pop() -> returns 4.
    The stack becomes [5,7].



    Note:

        Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
        It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
        The total number of FreqStack.push calls will not exceed 10000 in a single test case.
        The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
        The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.


* O(N)
  - duplicate at each freqency
  - When increase freqency for an element:
    - do not remove the element in the current stack;
    - keep it and add another copy to the next stack
    - by doing this we can keep the relative adding order of the elements

```java

class FreqStack {
    int high;
    HashMap<Integer, Stack<Integer>> f2k;
    HashMap<Integer, Integer> k2f;
    public FreqStack() {
        f2k = new HashMap<>();
        k2f = new HashMap<>();
        high = 0;
    }

    public void push(int x) {
        int f = k2f.getOrDefault(x, 0);
        k2f.put(x, ++f);
        Stack<Integer> s = f2k.getOrDefault(f, new Stack<>());
        s.push(x);
        f2k.put(f, s);
        high = Math.max(high, f);
    }

    public int pop() {
        int result = f2k.get(high).pop();

        if(k2f.get(result) == 1) k2f.remove(result);
        else k2f.put(result, k2f.get(result)-1);

        if(f2k.get(high).isEmpty()) {
            f2k.remove(high);
            high--;
        }
        return result;
    }
}

```


* Pass on first submit
  - similar to LFC & All in One data structure

```java

class FreqStack {
    int timestamp = 0;
    int high = 0;
    HashMap<Integer, PriorityQueue<Node>> f2k = new HashMap<>(); // freqency -> keys
    HashMap<Integer, Node> map = new HashMap<>();
    public FreqStack() {

    }

    public void push(int x) {
        Node n = map.getOrDefault(x, new Node(x, timestamp++));
        if(map.containsKey(x)) n.add(timestamp++);
        map.put(x, n);
        f2k.getOrDefault(n.size()-1, new PriorityQueue<>()).remove(n);
        PriorityQueue<Node> q = f2k.getOrDefault(n.size(), new PriorityQueue<>());
        q.offer(n);
        f2k.put(n.size(), q);
        high = Math.max(high, n.size());
    }

    public int pop() {
        PriorityQueue<Node> q = f2k.get(high);
        Node n = q.poll();
        if(q.isEmpty()) {
            f2k.remove(high);
            high--;
        }
        int result = n.key;

        n.reduce();
        if(n.isEmpty()) map.remove(n.key);
        else {
            PriorityQueue<Node> lowQ = f2k.getOrDefault(n.size(), new PriorityQueue<>());
            lowQ.offer(n);
            f2k.put(n.size(), lowQ);
        }
        return result;
    }

    class Node implements Comparable<Node>{
        int key;
        ArrayList<Integer> times = new ArrayList<>();
        public Node(int k, int t) {
            key = k;
            times.add(t);
        }
        public void add(int t) {
            times.add(t);
        }
        public void reduce() {
            times.remove(times.size()-1);
        }
        public int size() {
            return times.size();
        }
        public boolean isEmpty() {
            return times.isEmpty();
        }
        private int getLatest() {
            return times.get(times.size()-1);
        }
        @Override
        public int compareTo(Node n) {
            return n.getLatest() - this.getLatest();
        }
        public String toString() {
            return "" + key + "->" + times;
        }
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 */
```
