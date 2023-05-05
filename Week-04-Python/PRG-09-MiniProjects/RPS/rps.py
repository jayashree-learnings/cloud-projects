import random
user_score = 0
computer_score = 0
rounds = 0
valid_choices = ["rock", "paper", "scissors"]

# function which returns user choice and computer choice
def choice_selection():    
    computer_choice = random.choice(valid_choices)
    user_choice = input("pls enter a valid choice  rock, paper, scissors or quit to quit the game: ").lower()
    return user_choice, computer_choice

# function to validate the user choice
def choice_validation(user_choice):
    if(user_choice =="quit"):
       return -1
    elif user_choice not in valid_choices:
       return False
    else:
       return True

# function to see if u win .U win if  u & computer chooses the following options respectively. r-s, s-p, p-r
def you_win(user_choice,computer_choice):
    choice_tuple = (user_choice,computer_choice)
    win_list = [("rock","scissors"), ("scissors","paper"),("paper","rock")] 
    result = True if choice_tuple in win_list else False
    return result

# function to check who wins the current round 
def who_wins(user_choice, computer_choice):
    if (user_choice == computer_choice):
        print(f"U & computer have chosen the same option of {user_choice}...Its a tie")
        return "tie"
    elif (you_win(user_choice,computer_choice)):
        print(f"U chose {user_choice} & computer chose {computer_choice}...U won")
        return "you won"
    else: 
        print(f"U chose {user_choice} & computer chose {computer_choice}...U lost")
        return "you lost"

# function to find the score of the current round    
def score_track():
    user_wins = 0
    computer_wins = 0
    result_status = who_wins(user_selection,computer_selection)
    if result_status == "you won":
        user_wins = user_wins + 1
    elif result_status == "you lost":
        computer_wins = computer_wins + 1
    return user_wins, computer_wins

#Playing 5 rounds
while rounds<=4:
# step1-selection
    user_selection, computer_selection = choice_selection()
    print (f"U chose {user_selection} and the system chose {computer_selection}")

# step2 -validation of choices, if valid it calculates score
    valid_choice = choice_validation(user_selection)
    if valid_choice == -1:
        print(f"U chose to quit!!! bye bye")
        break
    elif valid_choice == False:
      print("The game wont quit till u enter  a proper choice")
      continue
    elif valid_choice == True:
        rounds += 1
        user_win, computer_win = score_track()
        if user_win == 1:
            user_score = user_score + 1
        elif computer_win == 1:
            computer_score = computer_score + 1
        print (f'In this round u scored {user_win} and system scored {computer_win}')
        print (f'So far in {rounds} rounds u have scored {user_score} and system scored {computer_score}')

# deciding who is the winner after 5 rounds
if computer_score < user_score:
    print("Ur score is higher than computer...U won")
else:
    print("Ur score is less than computer...U lost")
       








        

    

    
    



