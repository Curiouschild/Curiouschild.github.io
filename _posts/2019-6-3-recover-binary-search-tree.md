---
title:  "99. Recover Binary Search Tree"
date:   2019-06-03 12:22:00 +0930
categories: Leetcode
tags: Hard Tree
---

[{{page.title}}](https://leetcode.com/problems/recover-binary-search-tree/){:target="_blank"}

      Two elements of a binary search tree (BST) are swapped by mistake.

      Recover the tree without changing its structure.

      Example 1:

      Input: [1,3,null,null,2]

       1
      /
    3
      \
       2

      Output: [3,1,null,null,2]

       3
      /
    1
      \
       2

      Example 2:

      Input: [3,1,4,null,null,2]

       3
      / \
     1   4
        /
       2

      Output: [2,1,4,null,null,3]

       2
      / \
     1   4
        /
       3

      Follow up:

        A solution using O(n) space is pretty straight forward.
        Could you devise a constant space solution?

* O(1) Space
  - inorder traverse twice(l-root-r && r-root-l) to find x and y
  - correct the swaped elements

```java

class Solution {
    TreeNode pre;
    Integer x, y;
    boolean hasX, hasY;
    public void recoverTree(TreeNode root) {
        ascending(root);
        pre = null;
        descending(root);
        traverse(root, x, y);
    }

    public void descending(TreeNode root) {
        if(y != null) return;
        if(root == null) return;
        descending(root.right);
        if(pre != null && pre.val < root.val) {
            y = pre.val;
            return;
        }
        pre = root;
        descending(root.left);
    }
    public void ascending(TreeNode root) {
        if(x != null) return;
        if(root == null) return;
        ascending(root.left);
        if(pre != null && pre.val > root.val) {
            x = pre.val;
            return;
        }
        pre = root;
        ascending(root.right);
    }

    public void traverse(TreeNode root, int x, int y) {
        if(hasX && hasY) return;
        if(root == null) return;
        if(root.val == x) {
            root.val = y;
            hasX = true;
        }
        else if(root.val == y) {
            root.val = x;
            hasY = true;
        }
        traverse(root.left, x, y);
        traverse(root.right, x, y);
    }
}
```

* Naive O(N)
  - inorder traverse the tree
  - find two swaped elements in the array
  - correct the swaped elements

```java

public void recoverTree(TreeNode root) {
       ArrayList<Integer> arr = new ArrayList<>();
       traverse(root, arr);
       int x = 0, y = 0; // two misplaced elements
       for(int i = 0; i < arr.size(); i++) {
           if(i+1 < arr.size() && arr.get(i) > arr.get(i+1)) {
               x = arr.get(i);
               break;
           }
       }
       for(int i = arr.size()-1; i >= 0; i--) {
           if(i-1 >= 0 && arr.get(i) < arr.get(i-1)) {
               y = arr.get(i);
               break;
           }
       }
       traverse(root, x, y);
   }
   public void traverse(TreeNode root, int x, int y) {
       if(root == null) return;
       if(root.val == x) root.val = y;
       else if(root.val == y) root.val = x;
       traverse(root.left, x, y);
       traverse(root.right, x, y);
   }
   public void traverse(TreeNode root, ArrayList<Integer> arr) {
       if(root == null) return;
       traverse(root.left, arr);
       arr.add(root.val);
       traverse(root.right, arr);
   }
```
