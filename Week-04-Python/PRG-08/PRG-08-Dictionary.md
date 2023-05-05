#  Python Dictionary
A dictionary in python is a mutable collection of objects organized as key value pair. The elements of a dictionary are accessed via its keys and not by using index positions as in the case of lists. 

## Key terminologies
key - the key in a dictionary should be unique. If not it will keep the last value.

value - the value can be repetitive.it is accessed using the key eg my_dict[k] where my_dict is the dictionary with a key k.

items()- a built in python function which helps to loop over the dictionary and print the key and value together.

DictWriter - a method in csv module to write dictionary to the csv file. writeheader() and writerow() writes the header and the data respectively. 

## Exercise
1. Create a new script. Create a dictionary with the following keys and values:
Key	         Value
First name	Casper
Last name	Velzen
Job title	Lead Learning Coach
Company	TechGrounds
Loop over the dictionary and print every key-value pair in the terminal.

2. Create a new script. Use user input to ask for their information (first name, last name, job title, company). Store the information in a dictionary. Write the information to a csv file (comma-separated values). The data should not be overwritten when you run the script multiple times.

### Sources
https://www.w3schools.com/python/python_dictionaries.asp

https://realpython.com/python-dicts/

https://www.tutorialspoint.com/python/python_dictionary.htm

https://developers.google.com/edu/python/dict-files

### Overcome challenges
Had to see how to print both key and value pairs of a dictionary simultaneously. Understood it on implementing the items() function of the dictionary. Another challenge was how to write a dictionary to a csv file. Understood it when DictWriter function was used. Another challenge was how to avoid multiple headers being written to a csv file.Used an if clause to check the existence of the file and if it does not exist, both headers and data was written to the csv. Else the condition was specified to write the details alone to the csv file in the append mode. 
### Results
1) The key value pair was printed inside a for loop using the items function and without using the items function.

##### ![PRG-08-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-08/dict-01.PNG)


2)The details of the user were collected as input and the same was assigned as values to the dictionary. Using an if condition, the existence of the file was checked. If it exists, both the headers and data were written to the csv file. If not, the data alone was written to avoid multiple repetition of the same headers. When the program was re run, it took the input from the users a second time and the values of the dictionary was modified and the new values were written to the csv with out the headers. To avoid running the program manually, a while loop with break condition to exit out of the loop can implemented if the user opts for quit.

##### ![PRG-08-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-08/dict-02a.PNG)

##### ![PRG-08-03](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-08/dict-02b.PNG)

##### ![PRG-08-03](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-08/dict-02c.PNG)












