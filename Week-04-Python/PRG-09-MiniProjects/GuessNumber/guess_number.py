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
