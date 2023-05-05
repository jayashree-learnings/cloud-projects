#  Number Guessing Game

●	Generate a random number between 1 and 100 (or any other range).

●	The player guesses a number. For every wrong answer the player receives a clue.

●	When the player guesses the right number, display a score.

### Sources
https://www.geeksforgeeks.org/number-guessing-game-in-python/

https://thecleverprogrammer.com/2022/06/29/number-guessing-game-using-python/#:~:text=So%20below%20is%20how%20you,%3A%20print(%22Too%20high!

### Results
An initial input for maximum value was taken from the user. The user was asked to guess a number. Both these were validated to see if they were digits and positive numbers. A random guess was assigned for the computer. Based on the guess the user made, a clue was given to guess below or above his previous guess. The number of times the user guessed was kept track of. Finally when the user-guess matched with the computer's random choice, the user was declared the winner.  

```python
import random
guess_count = 0

while True: 
    range_max = input ("Pls enter the maximum value in the range: ")
    if range_max.isdigit() and int(range_max)>0 :
        range_max = int(range_max)
        break  
    else:
        print("Wrong entry")
 
random_num = random.randint(0,range_max)
while True:
    user_random = input(f"Enter a positive digit less than range_max of {range_max} u entered:")
    if user_random.isdigit()==False or int(user_random) > range_max or int(user_random) < 0 :
        print("Pls enter appropriately. It keeps on asking till you enter correct number")
        continue
    else:
        guess_count += 1
        user_random = int(user_random)
        if user_random < random_num :
            print("U guessed low...Pls guess a high value")    
        elif user_random > random_num :
           print("U guessed high...Pls guess a low value")
        else :
           print(f"Ur guess is right !! U won. U guessed {guess_count}  times")
           break

```
 
##### ![PRG-09-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-04/PRG-09-MiniProjects/guess-number-01.PNG)


