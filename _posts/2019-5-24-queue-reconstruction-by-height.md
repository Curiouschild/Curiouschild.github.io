---
title:  "406. Queue Reconstruction by Height"
date:   2019-05-24 11:51:00 +0930
categories: Leetcode
tags: Medium DynamicProgramming
---

[{{page.title}}](https://leetcode.com/problems/queue-reconstruction-by-height/){:target="_blank"}

    Suppose you have a random list of people standing in a queue. Each person is described by a pair of
    integers (h, k), where h is the height of the person and k is the number of people in front of this person
    who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

    Note:
    The number of people is less than 1,100.


    Example

    Input:
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    Output:
    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


* O(N^2)

Process people from tall to short.
Insert the current person into its proper postion (k), and shit other people to the right.
Invariant: all people on the right side of the insertion position are taller than the current person, and on the left side there are k people taller than the current person.

```java

public int[][] reconstructQueueFromTalltoShort(int[][] people) {
    LinkedList<int[]> result = new LinkedList<>();
    Arrays.sort(people, (a,b)->(a[0]==b[0] ? a[1]-b[1] : b[0]-a[0]));
    for(int[] p : people)
        result.add(p[1], p);
    return result.toArray(new int[0][]);
                      // if the T[] arr is not enough to store the list, a new array will be returned
                      // this empty array here is just to indicate the type
}
```


Find the the person should be on position i for each pass.
This person has the smallest height among all people with zero k.
Update k through the iteration.

```java

public int[][] reconstructQueueFromKEqualsZero(int[][] people) {
    int[][] arr = new int[people.length][];
    for(int i = 0; i < arr.length; i++) arr[i] = people[i].clone();
    for(int i = 0; i < arr.length; i++) {
        int k = -1;
        for(int j = i; j < arr.length; j++) {
            if(arr[j][1] == 0) {
                if(k == -1 || arr[j][0] < arr[k][0])
                    k = j;
            }
        }
        swap(people, i, k);
        swap(arr, i, k);
        for(int j = i+1; j < arr.length; j++) {
            if(arr[j][0] <= arr[i][0])
                arr[j][1]--;
        }
    }
    return people;
}

public void swap(int[][] arr, int i, int j) {
    int[] temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
```
