#  Python loops
Loops helps to perform repetitive tasks  in a convenient manner by avoiding the repetition of a code block multiple lines. For eg- to print a simple hello message 5 times, you can write the print statement 5 times or write it once and put it inside a loop which gives a cleaner code. Python supports 2 basic loop types for loop and while loop. 

## Key terminologies
for loop - Usually used when the number of iterations is known beforehand. The loop is iterated over till it reaches the end of a sequence like lists, strings etc. range function can be with for loop to specify a certain number of iterations.

while loop - Used when the number of iterations are unknown. The control enters the while loop if the expression is true. It keeps on iterating till the condition evaluates to false. Without any criteria to make the expression false, it will become an infinite loop. 

range - a default built in function to specify a range of numeric values.It includes lower limit, but excludes the upper limit and the default step size is 1. 

## Exercise
1. 	Create a new script. Create a variable x and give it the value 0. Use a while loop to print the value of x in every iteration of the loop. After printing, the value of x should increase by 1. The loop should run as long as x is smaller than or equal to 10.
2. Create a new script. Copy the code below into your script.
 for i in range(10):
     do something here
Print the value of i in the for loop. You did not manually assign a value to i. Figure out how its value is determined. Add a variable x with value 5 at the top of your script.
Using the for loop, print the value of x multiplied by the value of i, for up to 50 iterations.
3. Create a new script. Copy the array below into your script. arr = ["Coen", "Casper", "Joshua", "Abdessamad", "Saskia"]. Use a for loop to loop over the array. Print every name individually.

### Sources
https://www.w3schools.com/python/python_for_loops.asp

https://www.learnpython.org/en/Loops

https://www.programiz.com/python-programming/while-loop

https://www.w3schools.com/python/python_while_loops.asp



### Overcome challenges
Had to look up on the syntax for iteration using for loop and while loop.

### Results
1) Created a variable x to which was initialized to zero. while loop starts if condtion is true and the iteration continues till the condition is false. Here the given condition of x<=10 was true for the first iteration. Hence it printed the initial value of x which is zero and then x was incremented by 1. The loop kept on iterating till the condition became false (i.e, when x became 11)

##### ![PRG-04-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-04/while-loop.PNG)

2) range is an in built function in python which generates values including the lower limit and excluding the upper limit for a default increment of 1. First for a range of 10, using for loop the values from 0 to 9 were printed. 10 was not printed. 

For the multiplication  variable x was initialized to 5 in the beginning. Using for loop for an iteration of 50 times, the range function was used. Each value of i was multiplied with 5 and the result was displayed.

##### ![PRG-04-02a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-04/for-loop-multiply-a.PNG)

##### ![PRG-04-02a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-04/for-loop-multiply-b.PNG)


3) A list of names was created. The for loop was used to iterate over each element of the list and they were printed.
##### ![PRG-04-03](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-04/for-loop-listnames.PNG)













