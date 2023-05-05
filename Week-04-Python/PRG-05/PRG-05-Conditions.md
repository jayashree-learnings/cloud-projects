#  Python Conditions
Conditional statements are needed to make decision based on a certain criteria. It thus helps to execute a certain code block if the condition is satisfied and another if the condition is not satisfied. The conditional statements make use of an  if clause, an elif clause or an else clause and depending on the requirement these clauses can be nested inside another.

## Key terminologies
if-elif-else block - In this case, if the if condition is true, it gets executed. If it is false, it goes to the subsequent elif block which wil be executed if it is true. If false, the else block will be executed. It is possible to have nested if/else blocks depending on the requirement.

break - The break statement helps to break out of a loop

continue - The continue statement takes the flow to the beginning of the loop. 

random - The built in module of python which helps to make use of random numbers.randint is a function in the same module which helps to generate an integer in the specified range which includes the lower and upper limit.

## Exercise
1. Create a new script. Use the input() function to ask the user of your script for their name. If the name they input is your name, print a personalized welcome message. If not, print a different personalized message.
2. Create a new script. Ask the user of your script for a number. Give them a response based on whether the number is higher than, lower than, or equal to 100. Make the game repeat until the user inputs 100.
 

### Sources
https://www.w3schools.com/python/python_conditions.asp

https://realpython.com/python-conditional-statements/

https://www.softwaretestinghelp.com/python/python-conditional-statements/

https://www.programiz.com/python-programming/break-continue#:~:text=What%20is%20the%20use%20of,loop%20without%20checking%20test%20expression.

https://www.geeksforgeeks.org/break-continue-and-pass-in-python/

https://www.w3schools.com/python/module_random.asp



### Overcome challenges
Looked up on how to use if-elif-else block. Another challenge was on how to use continue or break statements inside a while loop.Understood it on implementing the same in the number guessing script.

### Results
1) A variable was created to which my name was assigned. Using the input function, a name was taken from the user which was then checked with the name variable. If equal, the greeting message was printed.When a different name was input, it asked the user to leave. 

##### ![PRG-05-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-05/condition-01.PNG)

2) while condition was used for the number guessing. Initially, True was used with while to start the loop. This is an infinite loop which keeps on iterating unless it is stopped explicitly with a break statement. A number was taken as a user input and it was checked with 100. If it is 100, break statement was used to quit the loop and if it is less than or greater than 100, appropriate messages were used along with continue statement. The continue statement will take the control to the beginning of the while loop and thus prompts the user to enter the value till he enters 100.

##### ![PRG-05-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-05/condition-02.PNG)















