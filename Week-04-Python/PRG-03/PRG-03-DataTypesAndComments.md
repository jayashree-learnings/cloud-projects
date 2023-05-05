# Data types and comments
Python supports many data types. A variable can be of any data type and it is important to know the data type of the variable before performing any operations on it so as to avoid unexpected errors.
Comments in python increases code readability making it easier for others to understand your code. The line starting with '#' symbol is a comment which wont be executed.

## Key terminologies
int - Indicates that the numeric value is a whole number

float - A numeric data type with decimal portion.

complex - Complex number consisting of a real part and an imaginary portion

str - String data type. Uses a single quote, double quote. For multi line strings, usually a triple quotes is used.

bool - Denoted by a True or False. Usually used in checking some conditions.

Lists - Mutable collection of elements allowing repetitive elements in a sequential manner

Dictionary - A value is always mapped to the key.

Tuple - Immutable but allows repetition of elements

Sets - Unordered collection of elements which does not allow duplicate values.


## Exercise
1. Create a new script. Copy the code below into your script.
a = 'int'
b = 7
c = False
d = "18.5"
Determine the data types of all four variables (a, b, c, d) using a built in function.Make a new variable x and give it the value b + d. Print the value of x. This will raise an error. Fix it so that print(x) prints a float. Write a comment above every line of code that tells the reader what is going on in your script.

2. Create a new script. Use the input() function to get input from the user. Store that input in a variable. Find out what data type the output of input() is. See if it is different for different kinds of input (numbers, words, etc.)

### Sources
https://www.w3schools.com/python/python_datatypes.asp

https://realpython.com/python-data-types/

https://docs.python.org/3/library/stdtypes.html

https://www.simplilearn.com/tutorials/python-tutorial/comments-in-python#:~:text=Comments%20in%20Python%20are%20identified,a%20multi%2Dline%20comment%20block.


### Overcome challenges

Had to see how to convert the string data type to float. Understood that it can be done using float function. 

### Results
1) Created 4 variables and assigned 4 different data types to them. Found the data type of each variable using built in type function. 

When tried to add b (int type) with d (str type), it threw an error because both cannot be added together(like numbers) nor can they be concatenated together (like strings).

To get the output as float the variable d(str type) was converted to float and added to b (int data type). When an int is added to a float, the result will be float. 

##### ![PRG-03-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-03/datatype-01.PNG)

Error when data types are of different types

##### ![PRG-03-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-03/datatype-02.PNG)

2) Using input function, different types of data like name, age, an integer value, a float value and a boolean value was taken from the user and assigned to variables. The data type of each of these values was checked and found that the input function always stores the value as str type.

##### ![PRG-03-03](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-03/input-fn.PNG)













