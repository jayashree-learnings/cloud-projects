
while True:
    my_num = int(input("enter an integer value: "))
    if my_num < 100:
       print("Its a very small number..pls enter a high value")
       continue
    elif my_num > 100:
       print("Its a very high number..pls enter a low value")
       continue
    else: 
       print('U entered 100..Correct guess !! U r quitting from the guess game')
       break