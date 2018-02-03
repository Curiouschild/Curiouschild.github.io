---
title:  "Introduction to Algorithms"
date:   2017-12-20 14:26:01 +0930
categories: Algorithm
tags: Algorithm
---
Start to read _Introduction to Algorithms_ and watch open source videos.
<!-- more -->

Chapter 1 The Role of Algorithms in Computing
=====

1. Algorithm
	computational steps
	sorting & multithreading
2. Getting Started
	insertion sort: efficient for sorting a small number of elements
	worst case running time
	Order of growth
		consider only the leading term of a formula
		also ignore the leading term?s constant coefficient
	divide-and-conquer
		One advantage of divide-and-conquer algorithms is that their running times are often easily determined
3. Growth of function
	asymptotic notation
		upper bounds: O o
		lower bounds: ? ?
		both: ?

4. Divide and Conquer ???


Chapter 2 Sorting and Order Statistics
=====
6. Heapsort
heap
maximum binary heap
heap size
max-heapify
build-max-heap
heapsort
priority queue
	job scheduling or event-driven simulation

7. Quicksort

balanced and unbalanced
randomized quicksort
stack depth: tail recursion ???

median-of-3
fuzzy sort
	????????
killer adversary

8 Sorting in Linear Time
8.1 Counting Sort
Whey need stability?
satellite data are carried around with the element being sorted.
counting sort is often used as a subroutine in radix sort.
8.2 Radix Sort

Show how to sort n integers in the range 0 to n 3 ? 1 in O(n) time.
solution?
https://classes.soe.ucsc.edu/cmps101/Winter13/hw/hw3sol.pdf

in a general base-k number system, numbers in the range 0 to R ? 1 can be represented using d = logk (R) digits.

9 Median and Order Statistics

maximum and minimum
3/2n time


Chapter 3 Data Structure
=====

10. Fundamental data structures

1. Stack
push & pop

2. Queue
enqueue & dequeue
head & tail
use an array to implement a queue
use two queues to implement a stack
	one method push: O(1) pop: O(N)
use two stacks to implement a queue
	two methods, one is push efficient, another is pop efficient

3. Linked List
either singly linked or doubly linked, it may be sorted or not, and it may be circular or not.
reverse a singly linked list:
	iterative & recursive
	https://kwfeng.wordpress.com/2010/12/04/reverse-linked-list/

time complexity of list operations:
	https://ita.skanev.com/10/problems/01.html
O(1) : delete(L, x)

4. rooted tree
sibling?
11. HashTable
the basic dictionary operations require only O(1) time on the average.
11.1 Direct Address Table
worst O(1)
11.2 hash table
load factor: average elements in a chain
simple uniform hashing.
division method

A prime not too close to an exact power of 2 is often a good choice for m.
multiplication method

open addressing
linear probing ?primary clustering
quadratic probing: if two keys have the same initial probe position, then their probe sequences are the same. This property leads to a milder form of clustering, called secondary clustering.
double hashing:


12 Binary Search Tree
12.1
