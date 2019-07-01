---
title:  "Java Fianl Review"
date:   2017-11-20 14:26:01 +0930
categories: CMU
tags: JavaOOP
---

Inner class

	An anonymous inner class must implement all the abstract methods in the superclass or in the interface.
	An anonymous inner class is compiled into a class named OuterClassName$n.class
	An anonymous inner class always uses the no-arg constructor from its superclass

<!-- more -->

Lambda

	https://www.javatpoint.com/java-lambda-expressions

Generic

	parameterize types

	a generic class is shared by all its instances regardless of its actual generic type. Although
	 GenericStack<String> and GenericStack<Integer> are two types, but there is only one
	 class GenericStack loaded into the JVM.

	benifit:
		detectable at compile time
		No Casting Needed for primitive type

	see: public class Box<T> {}
		 public static <E> void print(E[] list){}

		 ArrayList<String>: get method return String
		 ArrayList: get method return Object -->> need explicit down casting

	restrictions:

		 1: Cannot Create an Instance of a Generic Type. (i.e., new E()).

		 2: Generic Array Creation is Not Allowed. (i.e., new E[100]).

		 3: A Generic Type Parameter of a Class Is Not Allowed in a Static Context.

		 4: Exception Classes Cannot be Generic

Thread
```java

	volatile & sychoronized
	t1.interrupt() & Thread.interrupted()
	interrupt during sleep: InterruptedException
	synchronized methods use the monitor for the this object.
	synchronized blocks can be nested.
	Deadlock & livelock & starvation
```
Collections
```java

	java.util.Comparator: used to order the objects of user-defined class
		public int compare(Object element1, Object element2)
		public boolean equals(Object element)

	Iterator & ListIterator
		hasNext() --> next() --> remove()
```
I/O text file
```java

	Stream Example????
			  while ((read = fr.read(c)) != -1) {
                 if (read < cLen) fw.write(c, 0, read);
                 else fw.write(c);
                 count += read;
             }

    BufferedReader
		BufferedReader bufInput = new BufferedReader(new FileReader(args[0]));

	Serialization (theoretical understanding is sufficient)
		only the fields of the object are preserved.
		writeObject & readObject
		ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("f"));
```
Exception

	unchecked: RuntimeException & Error
	checked: other
		Checked exceptions are checked at compile-time

	throws & throw

	try-with-resoruces
		The try-with-resources statement can eliminate the need for a lengthy finally block. Any class that implements the java.lang.AutoCloseable can be used as a resource. If a resource should be autoclosed, its reference must be declared within the try statement’s parentheses.Multiple resources can be opened if they are separated by semicolons. If you open multiple resources, they will be closed in the opposite order in which you opened them.
		If an exception occurs while creating the AutoCloseable resource, control will immediately jump to a catch block. If an exception occurs in the body of the try block, all resources will be closed before the catch block runs. If an exception is generated while closing the resources, it will be suppressed. If the try block executes with no exceptions, but an exception is generated during the closing of a resource, control will jump to a catch block.

	Catching Multiple Exceptions
		Overridden methods may declare the same exceptions, fewer exceptions, or more specific exceptions, but not additional or more generic exceptions. A method may declare multiple exceptions with a comma-separated list.

		catch (ClassNotFoundException | IOException e)
		Avoid to catch a generic exception: The type alternatives that are separated with vertical bars cannot have an inheritance relationship. You may not list both a FileNotFoundException and an IOException in a multi-catch clause.


Exercise
```java


	true: If two strings are equal, the two strings have the same hashCodes.

	list: capacity never reduces.

	false: Generics can make programs run faster.

	false: Comparable<Object> c = new Date();

	set: override equals as well as hashcode

	Collection.sort(list): elements of the list must implements Comparable<E>

	Collection.sort(list, comparator) comparator is an instance of Comparator<E>

	Random number between 1 and 25: Math.round((Math.random() * 25));
		Random r = new Random(); int num = r.nextInt(24) + 1;
```
	Set & Map's key can have null value

	Warning!: see if it is a constructor or a common method!!!!

	Warning: to implement a method of an interface, it must be public
