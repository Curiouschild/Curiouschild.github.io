---
title:  "1206. Design Skiplist"
date:   2019-06-11 22:25:00 +0930
categories: Leetcode
tags: Hard DataStructure
---

[{{page.title}}](https://leetcode.com/problems/design-skiplist/){:target="_blank"}

    Design a Skiplist without using any built-in libraries.

    A Skiplist is a data structure that takes O(log(n)) time to add, erase and search. Comparing with treap
    and red-black tree which has the same function and performance, the code length of Skiplist can be
    comparatively short and the idea behind Skiplists are just simple linked lists.

    For example: we have a Skiplist containing [30,40,50,60,70,90] and we want to add 80 and 45 into it. The
    Skiplist works this way:


    Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

    You can see there are many layers in the Skiplist. Each layer is a sorted linked list. With the help of
    the top layers, add , erase and search can be faster than O(n). It can be proven that the average time
    complexity for each operation is O(log(n)) and space complexity is O(n).

    To be specific, your design should include these functions:

        bool search(int target) : Return whether the target exists in the Skiplist or not.
        void add(int num): Insert a value into the SkipList.
        bool erase(int num): Remove a value in the Skiplist. If num does not exist in the Skiplist, do nothing
        and return false. If there exists multiple num values, removing any one of them is fine.

    See more about Skiplist : https://en.wikipedia.org/wiki/Skip_list

    Note that duplicates may exist in the Skiplist, your code needs to handle this situation.

    Example:

    Skiplist skiplist = new Skiplist();

    skiplist.add(1);
    skiplist.add(2);
    skiplist.add(3);
    skiplist.search(0);   // return false.
    skiplist.add(4);
    skiplist.search(1);   // return true.
    skiplist.erase(0);    // return false, 0 is not in skiplist.
    skiplist.erase(1);    // return true.
    skiplist.search(1);   // return false, 1 has already been erased.

    Constraints:

        0 <= num, target <= 20000
        At most 50000 calls will be made to search, add, and erase.



* Naive design
  - make sure the first layer is empty before adding; that is to keep at least two layers anytime
  - use stack to trace the position to add or remove nodes

```java

class Skiplist {
    Node root;
    Random r = new Random();
    public Skiplist() {
        root = new Node(-1);
        root.low = new Node(-1);
    }

    public boolean search(int target) {
        Node prev = root, curr = root.next;
        while(true) {
            if(curr == null || curr.val >= target) {
                if(curr != null && curr.val == target) return true;
                if(prev.low == null) return false;
                prev = prev.low;
                if(prev.val == -1) curr = prev.next;
                else curr = prev;
            } else if(curr.val < target) {
                prev = curr;
                curr = curr.next;
            }
        }
    }

    public boolean flipCoin() {
        int i = r.nextInt(2);
        return i == 1;
    }

    public void add(int num) {
        if(root.next != null) {
            Node nr = new Node(-1);
            nr.low = root;
            root = nr;
        }
        Stack<Node> stack = new Stack<>();
        Node curr = root.next, prev = root;
        while(true) {
            if(curr == null || curr.val >= num) {
                if(prev.low == null) break;
                stack.push(prev);
                prev = prev.low;
                if(prev.val == -1) {
                    curr = prev.next;
                } else {
                    curr = prev;
                }
            } else {
                prev = curr;
                curr = curr.next;
            }
        }
        Node n = new Node(num);
        n.next = curr;
        prev.next = n;
        Node low = n;
        while(!stack.isEmpty()) {
            if(flipCoin()) {
                prev = stack.pop();
                n = new Node(num);
                n.next = prev.next;
                prev.next = n;
                n.low = low;
                low = n;
            } else {
                break;
            }
        }

        //     print();
        // System.out.println("_________above Add " + num + " ___________");
    }

    public void print() {
        Node head = root;
        while(head != null) {
            Node curr = head;
            while(curr != null) {
                System.out.print(curr.val + "->");
                curr = curr.next;
            }
            System.out.println();
            head = head.low;
        }

    }

    public boolean erase(int num) {

        Stack<Node> stack = new Stack<>();
        Node prev = root, curr = root.next;
        while(true) {
            if(curr == null || curr.val >= num) {
                if(prev.low == null) break;
                stack.push(prev);
                prev = prev.low;
                if(prev.val == -1) curr = prev.next;
                else curr = prev;
            } else if(curr.val < num) {
                prev = curr;
                curr = curr.next;
            }
        }
        if(curr == null || curr.val != num) return false;
        prev.next = curr.next;
        while(!stack.isEmpty()) {
            prev = stack.pop();
            curr = prev.next;
            // System.out.println(prev.val);
            if(curr == null || curr.val != num) break;
            prev.next = curr.next;
        }
        while(root.next == null && root.low.next == null && root.low.low != null) {
            root = root.low;
        }

        //     print();
        // System.out.println("_________above Erase " + num + " ___________");
        return true;
    }

    class Node {
        int val;
        Node next;
        Node low;
        public Node(int val) {
            this.val = val;
        }
        public String toString() {
            return "" + val;
        }
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist obj = new Skiplist();
 * boolean param_1 = obj.search(target);
 * obj.add(num);
 * boolean param_3 = obj.erase(num);
 */
```
