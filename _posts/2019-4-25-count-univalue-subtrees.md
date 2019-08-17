---
title:  "250. Count Univalue Subtrees"
date:   2019-4-25 21:03:00 +0930
categories: Leetcode
tags: Tree Medium
---

[{{page.title}}](https://leetcode.com/problems/count-univalue-subtrees/){:target="_blank"}

    Given a binary tree, count the number of uni-value subtrees.

    A Uni-value subtree means all nodes of the subtree have the same value.

    Example :

    Input:  root = [5,1,5,5,5,null,5]

                  5
                 / \
                1   5
               / \   \
              5   5   5

    Output: 4

* Integer null indicates a sub tree with different values

```java

class Solution {
    int cnt;
    public int countUnivalSubtrees(TreeNode root) {
        if(root == null) return 0;
        traverse(root);
        return cnt;
    }

    public Integer traverse(TreeNode root) {
        if(root.left == null && root.right == null) {
            cnt++;
            return root.val;
        }
        if(root.left == null || root.right == null) {
            TreeNode child = root.left == null ? root.right : root.left;
            Integer sub = traverse(child);
            if(sub != null && sub == root.val) {
                cnt++;
                return root.val;
            }
        } else {
            Integer left = traverse(root.left), right = traverse(root.right);
            if(left != null && right != null && left == right && left == root.val) {
                cnt++;
                return root.val;
            }
        }
        return null;
    }
}
```

* Result class

```java
    int ans = 0;
    public int countUnivalSubtrees1(TreeNode root) {
        dfs(root);
        return ans;
    }

    public Result dfs(TreeNode root) {
        if(root == null) return null;
        Result l = dfs(root.left);
        Result r = dfs(root.right);
        int cnt = 1;
        if(l != null && (l.flag == 0 || l.val != root.val)) cnt = 0;
        if(r != null && (r.flag == 0 || r.val != root.val)) cnt = 0;
        ans += cnt;
        return new Result(root.val, cnt);
    }

    class Result {
        int val;
        int flag;
        public Result(int val, int flag) {
            this.val = val;
            this.flag = flag;
        }
    }
```
