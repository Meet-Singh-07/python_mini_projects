import random 


num = random.randint(1,100)
print(f"The number is {num}")
while True: 
    try:
        input_num = int(input("Guess the number between (1-100): "))   
        if input_num == num:
            print(f"Congratulations!! \n You guessed the number correctly!! \n The Number is {num}")
            break
        elif input_num > num:
            print("You guessed number is greater. \n Try again!!")
        elif input_num < num:
            print("You guessed number is smaller. \n Try again!!")
        else:
            print("Invalid Input!")
    except ValueError: 
        print("Please enter a valid Number")
    
    