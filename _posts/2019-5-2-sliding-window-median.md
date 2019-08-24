---
title:  "480. Sliding Window Median"
date:   2019-05-02 12:46:00 +0930
categories: Leetcode
tags: Hard PriorityQueue
---

[{{page.title}}](https://leetcode.com/problems/sliding-window-median/){:target="_blank"}

    Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
    Examples:

    [2,3,4] , the median is 3

    [2,3], the median is (2 + 3) / 2 = 2.5

    Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

    For example,
    Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

    Window position                Median
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       1
     1 [3  -1  -3] 5  3  6  7       -1
     1  3 [-1  -3  5] 3  6  7       -1
     1  3  -1 [-3  5  3] 6  7       3
     1  3  -1  -3 [5  3  6] 7       5
     1  3  -1  -3  5 [3  6  7]      6

    Therefore, return the median sliding window as [1,-1,-1,3,5,6].

    Note:
    You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.


* Two heaps is a good friend of median of streaming data

```java
class Solution {
    PriorityQueue<Integer> min = new PriorityQueue<>(); // minheap stores large values
    PriorityQueue<Integer> max = new PriorityQueue<>(Collections.reverseOrder());
    public double[] medianSlidingWindow(int[] nums, int k) {
        for(int i = 0; i < k; i++) enque(nums[i]);
        double[] result = new double[nums.length-k+1];
        result[0] = getMedian();
        int j = 1;
        for(int i = 0; i < nums.length-k; i++) {
            int o = nums[i], v = nums[i+k];
            if(o >= min.peek()) min.remove(o);
            else max.remove(o);
            enque(v);
            result[j++] = getMedian();
        }
        return result;
    }
    public void enque(int v) {
        min.offer(v);
        max.offer(min.poll());
        if(max.size() > min.size())
            min.offer(max.poll());
    }
    public double getMedian() {
        if(min.size() == max.size()) return (min.peek() + (double)max.peek()) / 2;
        return (double)min.peek();
    }
```

* A Failed 1.5 hours try on doubly linked list. i shi le zhi le....

A right direcion at the very beginning is more important than fast coding T_T
The two heap solution just takes 10 minutes

```java
public double[] medianSlidingWindow(int[] nums, int k) {
     int[] original = new int[k];
     System.arraycopy(nums, 0, original, 0, k);
     MyList l = new MyList(original);
     l.print();
     for(int i = 0; i < nums.length - k; i++) {
         l.move(nums[i], nums[i+k]);
         double median = l.getMedian();
     }
     return null;
 }

 class MyList {
     TreeMap<Integer, LinkedList<Node>> map = new TreeMap<>();
     Node head;
     Node tail;
     Node mid;
     boolean isOdd;
     public MyList(int[] arr) {
         Arrays.sort(arr);
         isOdd = arr.length % 2 == 1;
         head = new Node(Integer.MIN_VALUE);
         tail = new Node(Integer.MAX_VALUE);
         head.next = tail;
         tail.prev = head;
         Node p = head;
         for(int v : arr) {
             Node curr = new Node(v);
             p.next.prev = curr;
             curr.next = p.next;
             p.next = curr;
             curr.prev = p;
             p = curr;

             LinkedList<Node> sub = map.getOrDefault(v, new LinkedList<Node>());
             sub.add(curr);
             map.put(v, sub);
         }
         Node fast = head.next, slow = head.next;
          while(fast != tail && fast.next != tail) {
             fast = fast.next.next;
             slow = slow.next;
         }
         mid = slow;
         if(arr.length % 2 == 0) mid = mid.prev;

         System.out.println("init map=" + map);
     }

     public void move(int o, int n) {
         System.out.println("replace " + o + " -> " + n);
         if(o == n) return;
         LinkedList<Node> arr = map.get(o);
         Node moved = arr.removeLast();
         if(arr.size()==0) map.remove(o);

         moved.val = n;
         arr = map.getOrDefault(n, new LinkedList<Node>());
         arr.add(moved);
         map.put(n, arr);

         if(moved == mid) {
             if(n > o) mid = mid.next;
             else mid = mid.prev;
         }

         // Fail Reason: the position of mid throught the move...........
         if(moved.val <= moved.prev.val) {
             while(moved.val <= moved.prev.val) {
                 Node next = moved.next, t = moved.prev;
                 next.prev = t;
                 t.next = next;
                 moved.prev = t.prev;
                 t.prev.next = moved;
                 t.prev = moved;
                 moved.next = t;
             }
         }

         if(moved.val >= moved.next.val) {
             while(moved.val >= moved.next.val) {
                 // System.out.println("curr=" + moved.val + " next=" + moved.next.val);
                 Node p = moved.prev, t = moved.next;
                 p.next = t;
                 t.prev = p;
                 moved.next = t.next;
                 t.next.prev = moved;
                 t.next = moved;
                 moved.prev = t;
             }
         }

         this.print();
         System.out.println("median=" + mid.val);
     }

     public double getMedian() {
         if(isOdd) return (double)mid.val;
         return ((double)mid.val + mid.next.val) / 2;
     }

     public void print() {
         Node curr = head.next;
         System.out.print("L= ");
         while(curr != tail) {
             System.out.print(curr.val + " > ");
             curr = curr.next;
         }
         System.out.println();
     }

     class Node {
         Node prev;
         Node next;
         int val;
         public Node(int v) {val = v;}
         public String toString() {
             return "" + val;
         }
     }
 }
```
