---
title:  "Scanner"
date:   2017-09-07 14:26:01 +0930
categories: foo
tags: java js
---
I have encountered two problems about scanner.

+ get stuck in a loop if an exception is caught

		Scanner sc = new Scanner(System.in);
		while (true) {
			System.out.println("I will stuck in the loop");
			try {
				sc.nextInt();
			} catch (InputMismatchException e) {
				continue;
			}
			System.out.println("I will no be diplayed");
		}
	Reason: This is becasue nextInt() does not comsume the invalid input. It is right there and will be received by the nextInt() the next iteration. So the exception will be caught each loop, and the loop always continue.
	
	How to solve: You can use a next() or nextLine() to clear the input stream.	
+ 