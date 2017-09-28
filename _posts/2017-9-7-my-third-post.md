---
title:  "Java OOP Midterm Review"
date:   2017-09-07 14:26:01 +0930
categories: foo
tags: java 
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



+ I wanted to read the java source code in Eclipse, but failed to install Apple java package in my Mac. Finally I downloaded the linux JDK package at Oracle's website in which there is a src.zip file that contains source code.

***

Use Array.copyOf() to copy array.
		
	public String(char value[]) {
        this.value = Arrays.copyOf(value, value.length);
    }
    
   + subsequent modification of
     the character array does not affect the newly created string.
***

First specify method(int arg1,int arg2)

then call it in method() { method(1, 0) }

rather than conversing this order.


***

Calculate square root.

```
float square = 4;    // number to find sq root of   float squareRoot = square;    // first guess   while (squareRoot * squareRoot - square > 0.001) { // How accurate?       squareRoot = (squareRoot + square/squareRoot)/2;       System.out.println("Next try will be " + squareRoot);   }```
***
Use static methods and variables without writing class name and dot notation before them. 
eg. Controller.turnLeft --> turnLeft
	static import packagename.Controller.*;
***

```
Object o1 = null;
Object o2 = null;
System.out.println(o1==o2);//true
o1.equals(o2);//false
```
***
Note that it is generally necessary to override the hashCode method whenever this method is overridden, so as to maintain the general contract for the hashCode method, which states that equal objects must have equal hash codes.

***
A good practice is to design and write methods that take the most generic form of your object as possible.***
