Java FX

Inner class
	
	An anonymous inner class must implement all the abstract methods in the superclass or in the interface. 


Lambda

	https://www.javatpoint.com/java-lambda-expressions
	





		 ArrayList: get method return Object -->> need explicit down casting


	volatile & sychoronized
	t1.interrupt() & Thread.interrupted() 
	interrupt during sleep: InterruptedException


	java.util.Comparator: used to order the objects of user-defined class
		public int compare(Object element1, Object element2)
		
	Iterator & ListIterator
		hasNext() --> next() --> remove()
	
I/O text file
	
	Stream Example????
			  while ((read = fr.read(c)) != -1) {

		BufferedReader bufInput = new BufferedReader(new FileReader(args[0]));
		
	Serialization (theoretical understanding is sufficient)
		only the fields of the object are preserved.
		writeObject & readObject
		ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("f"));
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









		Random r = new Random(); int num = r.nextInt(24) + 1;
		
	Set & Map's key can have null value 
	
	Warning!: see if it is a constructor or a common method!!!!
	
	Warning: to implement a method of an interface, it must be public
		
	
		
	