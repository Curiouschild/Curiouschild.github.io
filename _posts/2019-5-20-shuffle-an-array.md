---
title:  "384. Shuffle an Array"
date:   2019-05-20 09:41:00 +0930
categories: Leetcode
tags: Medium String Backtrack
---

[{{page.title}}](https://leetcode.com/problems/shuffle-an-array/){:target="_blank"}

    Shuffle a set of numbers without duplicates.

    Example:

    // Init an array with set 1, 2, and 3.
    int[] nums = {1,2,3};
    Solution solution = new Solution(nums);

    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be
    returned.
    solution.shuffle();

    // Resets the array back to its original configuration [1,2,3].
    solution.reset();

    // Returns the random shuffling of array [1,2,3].
    solution.shuffle();


* O(N)

```java

class Solution {
    int[] original;
    int[] shuffle;
    public Solution(int[] nums) {
        original = nums;
        shuffle = nums.clone();
    }

    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return original;
    }

    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        Random r = new Random();
        for(int i = 0; i < shuffle.length; i++) { // make sure that i th element is randomly picked
            int index = i + r.nextInt(shuffle.length-i);
            int temp = shuffle[i];
            shuffle[i] = shuffle[index];
            shuffle[index] = temp;
        }
        return shuffle;
    }
}

```

* O(N^2)

```java

class Solution {
    int[] original;
    public Solution(int[] nums) {
        original = nums;
    }

    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return original;
    }

    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        int len = original.length;
        // index: 0 -> len-1
        Random r = new Random();
        int[] shuffle = new int[len];
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i : original) arr.add(i);
        int i = 0;
        while(arr.size() > 0) {
            int index = r.nextInt(arr.size());
            shuffle[i++] = arr.remove(index);
        }
        return shuffle;
    }
}
```
