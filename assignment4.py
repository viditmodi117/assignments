"""Q.1 What is File fuction in python ? What is keywords to create and write file?
Ans--> A file object allows us to use, access and manipulate all the user accessible files. One can read and write any such files. When a file operation fails for an I/O-related reason, the exception IOError is raised.
Create() : use the open() function with one of the following options  "x" or "w"  to create a new file: "x" Create: this command will create a new file if and only if there is no file already in existence with that name or else it will return an error.
write() : This function writes a fixed sequence of characters to a file. writelines() : This function writes a list of string
"""

"""Q.2 Write a Python program to read an entire text file.
Ans-->a=str(input("Enter the name of the file: "))
file1 = open(a,'r')
line = file1.readline()
while(line!=""):
    print(line)
    line = file1.readline()
file1.close()"""

"""Q.3 Write a Python program to append text to a file and display the text.
Ans--> fname = input("Enter file name: ")
file3=open(fname,"a")
c=input("Enter string to append: \n");
file3.write("\n")
file3.write(c)
file3.close()
print("Contents of appended file:");
file4=open(fname,'r')
line1=file4.readline()
while(line1!=""):
    print(line1)
    line1=file4.readline()    
file4.close()"""

"""Q.4 Write a Python program to read first n lines of a file.
Ans--> def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('abc.txt',2)"""

"""Q.5 Write a Python program to read last n lines of a file.
Ans-->def LastNlines(fname, N):
    with open(fname) as file:
        for line in (file.readlines() [-N:]):
            print(line, end ='')
if __name__ == '__main__':
    fname = 'File1.txt'
    N = 3
    try:
        LastNlines(fname, N)
    except:
        print('File not found')"""
        
"""Q.6  Write a Python program to read a file line by line and store it into a list.
Ans-->  def file_read(fname):
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                content_list = f.readlines()
                print(content_list)

file_read('abc.txt')"""

"""Q.7 Write a Python program to read a file line by line store it into a variable.
Ans--> def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('abc.txt')"""

"""Q.8 Write a python program to find the longest words. 
Ans--> sentence = input("Enter sentence: ")
longest = max(sentence.split(), key=len)
print("Longest word is: ", longest)
print("And its length is: ", len(longest))"""

"""Q.9 Write a Python program to count the number of lines in a text file.
Ans-->fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)"""

"""Q.10 Write a Python program to count the frequency of words in a file. 
Ans--> fname = input('Enter the file name: ')
try:
    fhand = open(fname)
    counts = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    print(counts)
except:
    print('File cannot be opened:', fname)"""
    
"""Q.11 Write a Python program to write a list to a file. 
Ans--> color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('module.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())  """


"""Q.12 Write a Python program to copy the contents of a file to another file.
Ans-->import shutil
shutil.copyfile('first.txt','second.txt')"""

"""Q.13 Explain Exception handling? What is an Error in Python?
 Ans-->
 - Exception handling allows you to separate error-handling code from normal code. An exception is a Python object which represents an error. As with code comments, exceptions helps you to remind yourself of what the program expects. It clarifies the code and enhances readability.
 - There are mainly two types of errors in python programming namely - Syntax errors and Logical Errors or Exceptions. Whenever we do not write the proper syntax of the python programming language (or any other language) then the python interpreter throws an error known as syntax error"""

"""Q.14 How many except statements can a try-except block have? Name Some built-in exception classes:
 - There has to be at least one except statement."""

"""Q.15 When will the else part of try-except-else be executed?
 Ans-->The else part is executed when no exception occurs."""

"""Q.16 Can one block of except statements handle multiple exception?
 Ans-->-  try-except blocks can be used to catch and respond to one or multiple exceptions. 
 - In cases where a process raises more than one possible exception, they can all be handled using a single except clause.

"""Q.17 When is the finally block executed?"""
Ans-->The finally block will be executed no matter if the try block raises an error or not. 
This can be useful to close objects and clean up resources."""

"""Q.18 What happens when „1‟== 1 is executed?
Ans-->it simply evaluates to false and does not raise any exception."""

"""Q.19 How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.
Ans-->
- To handle the exception, we have put the code, result = numerator/denominator inside the try block. Now when an exception occurs, the rest of the code inside the try block is skipped. The except block catches the exception and statements inside the except block are executed.
- Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause.
- A code Snippet is a programming term that refers to a small portion of re-usable source code, machine code, or text. Snippets help programmers reduce the time it takes to type in repetitive information while coding. Code Snippets are a feature on most text editors, code editors, and IDEs.
[ ]
"""

"""Q.20 Write python program that user to enter only odd numbers, else will raise an exception
Ans-->
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")"""

"""Q.21 What are oops concepts? Is multiple inheritance supported in java.
Ans-->
- Inheritance is one of the core concepts of Object-Oriented Programming. Multiple Inheritance is the process in which a subclass inherits more than one superclass. Java does not support Multiple Inheritance; however, Java interfaces help us achieve Multiple Inheritance of type in Java.
- Multiple inheritance in java is the capability of creating a single class with multiple superclasses. Unlike some other popular object oriented programming languages like C++, java doesnot provide support for multiple inheritance in classes."""""


"""Q.22 How to Define a Class in Python? What Is Self? Give An Example Of A Python Class?
Ans--> A class in Python can be defined using the class keyword. As per the syntax above, a class is defined using the class keyword followed by the class name and : operator after the class name, which allows you to continue in the next indented line to define class members."""

- The self keyword is used to represent an instance (object) of the given class.

- Example:- suppose Bike is a class then we can create objects like bike1 , bike2 , etc from the class. Here's the syntax to create an object. Here, bike1 is the object of the class."""

"""Q.23 Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle?
Ans-->
- In Euclidean plane geometry, a rectangle is a quadrilateral with four right angles.
- To find the area of a rectangle, multiply the length by the width. A rectangle with four sides of equal length is a square.


class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(10, 15)
print(newRectangle.rectangle_area())"""

"""Q.24,25  Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle 
Ans-->class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(9)
print(NewCircle.area())
print(NewCircle.perimeter())"""

"""Q.26 Explain Inheritance in Python with an example?What is init? Or What Is A Constructor In Python?
Ans-->
- Inheritance relationship defines the classes that inherit from other classes as derived, subclass, or sub-type classes. Base class remains to be the source from which a subclass inherits. For example, you have a Base class of “Animal,” and a “Lion” is a Derived class. The inheritance will be Lion is an Animal.
- The init method is the Python equivalent of the C++ constructor in an object-oriented approach. The init function is called every time an object is created from a class. The init method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.
- Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created.In Python the init() method is called the constructor and is always called when an object is created."""

"""Q.27 What is Instantiation in terms of OOP terminology?

- Instantiation The creation of an instance of a class. 
   - Method A special kind of function that is defined in a class definition.   
   - Object A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods."""

"""Q.28 What is used to check whether an object o is an instance of class A?
Ans-->
- The isinstance() function returns True if the specified object is of the specified type, otherwise False . If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple."""

"""Q.29 What relationship is appropriate for Course and Faculty?
Ans--> - "Composition(Has-A Relation)" relationship between course and faculty class."""

"""Q.30 What relationship is appropriate for Student and Person?
Ans-->
- So, simply we can say that it establishes an “is-a” or “kind of” relationship between Student and Person class.


class Person:
    def __init__(self, fname, lname, address):
        self.fname = fname
        self.lname = lname
        self.address = address
        
    def display(self):
        print("First Name: ", self.fname)
        print("Last Name: ", self.lname)
        print("Address: ", self.address)
        
class Student(Person):
    def __init__(self, fname, lname, address, age, gradYear):
        super().__init__(fname, lname, address)
        self.age = age
        self.gradYear = gradYear
        
    def display(self):
        super().display()
        print("Age: ", self.age)
        print("Graduation Year: ", self.gradYear)

# person object
per = Person("Grishma", "Sapariya", "Karjan") 
per.display()
print("===========================================")
std = Student("Rutik", "Sapariya", "Karjan", 21, 2001)
std.display()"""