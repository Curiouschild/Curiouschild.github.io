---
title:  "449. Serialize and Deserialize BST"
date:   2019-4-3 16:38:00 +0930
categories: Leetcode
tags: DFS BFS Tree DataStructure
---

[{{page.title}}](https://leetcode.com/problems/serialize-and-deserialize-bst/){:target="_blank"}


    Serialization is the process of converting a data structure or object into a sequence of
    bits so that it can be stored in a file or memory buffer, or transmitted across a network
    connection link to be reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary search tree. There is no restriction
    on how your serialization/deserialization algorithm should work. You just need to ensure that 
    a binary search tree can be serialized to a string and this string can be deserialized to the
    original tree structure.

    The encoded string should be as compact as possible.

    Note: Do not use class member/global/static variables to store states. Your serialize and
    deserialize algorithms should be stateless.


* DFS

```java
public class Codec {
    public String serialize(TreeNode root) {
        if(root == null) return "null";
        return "" + root.val + "," + serialize(root.left) + "," + serialize(root.right);
    }
    public TreeNode deserialize(String data) {
        String[] arr = data.split(",");
        LinkedList<String> list = new LinkedList<>(Arrays.asList(arr));
        return dfs(list);
    }

    public TreeNode dfs(LinkedList<String> list) {
        String s = list.get(0);
        list.removeFirst();
        if(s.equals("null")) return null;
        TreeNode root = new TreeNode(Integer.valueOf(s));
        root.left = dfs(list);
        root.right = dfs(list);
        return root;
    }
  }
```

* BFS

```java
    public String serialize(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        String r  = "";
        while(q.size() != 0) {
            TreeNode curr = q.poll();
            r += (curr == null ? "null" : curr.val) + ",";
            if(curr == null) continue;
            q.offer(curr.left);
            q.offer(curr.right);
        }
        return r.substring(0, r.length()-1);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if(data.equals("null")) return null;
        // System.out.println("data=" + data);
        String[] arr = data.split(",");
        Queue<TreeNode> q = new LinkedList<>();
        int i = 0;
        TreeNode root = new TreeNode(Integer.valueOf(arr[i++]));
        q.offer(root);
        while(q.size() != 0) {
            TreeNode curr = q.poll();
            String l = arr[i++], r = arr[i++];
            // System.out.println("curr=" + curr.val + " l="+l + " r=" + r);
            if(!l.equals("null")) {
                curr.left = new TreeNode(Integer.valueOf(l));
                q.offer(curr.left);
            }
            if(!r.equals("null")) {
                curr.right = new TreeNode(Integer.valueOf(r));
                q.offer(curr.right);
            }
        }
        return root;
    }
```
