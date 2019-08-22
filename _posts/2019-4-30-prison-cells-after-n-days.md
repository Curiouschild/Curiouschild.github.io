---
title:  "957. Prison Cells After N Days"
date:   2019-4-30 13:43:00 +0930
categories: Leetcode
tags: Medium HashMap BitManiputlation
---

[{{page.title}}](https://leetcode.com/problems/prison-cells-after-n-days/){:target="_blank"}

    There are 8 prison cells in a row, and each cell is either occupied or vacant.

    Each day, whether the cell is occupied or vacant changes according to the following rules:

        If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes
        occupied.
        Otherwise, it becomes vacant.

    (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

    We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

    Given the initial state of the prison, return the state of the prison after N days (and N such changes
    described above.)



    Example 1:

    Input: cells = [0,1,0,1,1,0,0,1], N = 7
    Output: [0,0,1,1,0,0,0,0]
    Explanation:
    The following table summarizes the state of the prison on each day:
    Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
    Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
    Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
    Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
    Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
    Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
    Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
    Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

    Example 2:

    Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
    Output: [0,0,1,1,1,1,1,0]



    Note:

        cells.length == 8
        cells[i] is in {0, 1}
        1 <= N <= 10^9

* bit manipulation

```java
public int[] prisonAfterNDays(int[] cells, int N) {
    HashMap<Integer, Integer> map = new HashMap<>();
    ArrayList<Integer> arr = new ArrayList<>();
    int num = 0;
    for(int i = 0; i <= 7; i++) num ^= (cells[7-i] << i);
    for(int k = 0; k < N; k++) {
        int next = 0;
        for(int j = 1; j <= 6; j++) {
            int l = (num >> (j+1)) & 1, r = (num >> (j-1)) & 1;
            if((l ^ r) == 0)
                next |= (1 << j);
        }
        num = next;
        if(map.containsKey(num)) break;
        map.put(num, 0);
        arr.add(num);
    }
    System.out.println(arr.size());
    if(arr.size() < N)
        num = arr.get((N-1) % arr.size());

    int[] result = new int[8];
    for(int i = 7; i >= 0; i--) {
        if(((num >> i) & 1) == 1)
            result[7-i] = 1;
    }
    return result;

}
```

```java
public int[] prisonAfterNDays(int[] cells, int N) {
    HashMap<String, Integer> map = new HashMap<>();
    ArrayList<String> arr = new ArrayList<>();
    String key = null;
    for(int k = 0; k < N; k++) {
        int[] buffer = new int[cells.length];
        for(int i = 1; i < cells.length-1; i++) {
            int l = cells[i-1], r = cells[i+1];
            if(l == 0 && r == 0 || l == 1 && r == 1) buffer[i] = 1;
        }
        cells = buffer;
        key = toKey(cells);
        if(map.containsKey(key)) break;
        map.put(key, k);
        arr.add(key);
    }
    if(map.get(key) == arr.size()-1) return cells;
    int len = arr.size() - map.get(key); // why it is always 0??? why it is a perfect circle?
                                        // I can't prove but it passes all the cases
                                        // or to calculate the pre len before the circle
    int index = (N-1) % len;
    for(int i = 0; i < cells.length; i++)
        cells[i] = arr.get(index).charAt(i) - '0';
    return cells;
}
```
