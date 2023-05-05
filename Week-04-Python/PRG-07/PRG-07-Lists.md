#  Python lists
A list is a mutable collection of elements which can be of any data type. The elements ina list maintain a sequence and can be repetitive as well. 

## Key terminologies
index of a list - It indicates the position of each element in the list and starts at zero. the first element is located at zeroth position.

len - a built in function in python which return the total elements in a list.

mutability of a list - lists are mutable in the sense that we can insert, update or delete an element in the list.

in - the key word used to check the existence of an element. It returns a boolean value.eg - "apples" in fruits_list

## Exercise
1. Create a new script. Create a variable that contains a list of five names. Loop over the list using a for loop. Print every individual name in the list on a new line.
2. Create a new script. Create a list of five integers. Use a for loop to do the following for every item in the list:Print the value of that item added to the value of the next item in the list. If it is the last item, add it to the value of the first item instead (since there is no next item).

### Sources
https://www.w3schools.com/python/python_lists.asp

https://developers.google.com/edu/python/lists

https://docs.python.org/3/tutorial/datastructures.html


### Overcome challenges
Had to see how to get the length of a list. Understood it on implementing len function. 

### Results
1) A list of 5 names were created. A for loop was used to loop over each item in the list and they were printed.

##### ![PRG-07-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-07/lists-01.PNG)

2) A list of 5 numbers were created.  A for loop was used with range function over the length of the list using a variable i. For each iteration,  the value of i is checked against (length of list) -1. If so, it means the last element and hence the element at that position is added to the first element. Else the element is added to the next element. In either case, the sum is appended to a new list which was initialized as an empty list first. The elements were then printed.

##### ![PRG-07-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-07/lists-02.PNG)




