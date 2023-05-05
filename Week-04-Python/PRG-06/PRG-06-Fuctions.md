#  Python Functions
A function is a block of code written with the intention of performing a certain task. It avoids repetition of code being written for different inputs and enhances code reusability following the principle of DRY(Don't Repeat Yourself.). As a complex task is broken into smaller steps, it supports modularity making it easier to maintain,manage and correct the code.

## Key terminologies
function definition - A function has to be defined before calling it.
It consists of the lines of code describing what it is going to do.

parameters - the variables listed inside the parenthesis of the function definition. 

arguments - It is the data which we pass when calling the function so that it can be converted to an output.The arguments can be positional arguments(the values are assigned based on the order in which they are passed), default arguments(arguments defined in the function definition.If no value is passed for the argument, it takes the default value), keyword arguments(during function call, value is assigned to the arguments by the key word).


## Exercise
1. Create a new script. Import the random package. Print 5 random integers with a value between 0 and 100.

2. Create a new script. Write a custom function myfunction() that prints “Hello, world!” to the terminal. Call myfunction.	Rewrite your function so that it takes a string as an argument. Then, it should print “Hello, <string>!”.

3. Create a new script. Copy the code below into your script. 
def avg():
x = 128
y = 255
z = avg(x,y)
print ("The average of",x,"and", y, "is", z)
Write the custom function avg() so that it returns the average of the given parameters.

### Sources
https://www.w3schools.com/python/python_functions.asp

https://www.geeksforgeeks.org/python-functions/

https://realpython.com/defining-your-own-python-function/

https://pynative.com/python-function-arguments/



### Overcome challenges
Looked up on how to use the random module to specify a range of values. had to check the syntax of function definition in python and how to pass the arguments to a function.

### Results
1) Imported the random module to use it's randint function which can be used to specify the range of integers. Here the lower limit was specified as zero and upper limit as 100. A for loop was used with range function (range of 5) to print random integer 5 times. 

##### ![PRG-06-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-06/fnctn-random.PNG)

2) A function was first defined which does not take any parameters.The objective was to print the 'hello world' message and on calling that function name the message was printed on to the terminal. A second function was defined which takes an argument and the message with greeting and the parameter was typed.

##### ![PRG-06-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-06/fnctn-str.PNG)


3) A function which takes 2 arguments was defined to calculate the average of 2 numbers and it returned the same. The function was called and the returned value stored in another variable. Finally the average value was printed.

##### ![PRG-06-03](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-06/fnctn-avg.PNG)

















