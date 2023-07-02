"""This is a very popular yet simple game name Rock Paper and Scissors"""

# Rock Paper Scissors ASCII Art

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:

    # User's Response
    userResponse = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.  "))

    if userResponse == 0:
        print(f"You choose Rock {Rock}")
    elif userResponse == 1:
        print(f"You choose Paper  {Paper}")
    elif userResponse == 2:
        print(f"You choose Scissors {Scissors}")
    else:
        print("Invalid Input,Please type between 0,1, and 2 ")

    # Computer's logic
    import random

    compResponse = random.randint(0, 2)

    if compResponse == 0:
        print("Computer's Choice is Rock " + Rock)
    elif compResponse == 1:
        print("Computer's Choice is Paper " + Paper)
    else:
        print("Computer's Choice is Scissors " + Scissors)

    # Logical operations of the game

    if userResponse == 0:
        if compResponse == 1:
            print("Computer Wins! ")
        elif compResponse == 2:
            print("You Win! ")
        else:
            print("It is a draw! ")
    elif userResponse == 1:
        if compResponse == 0:
            print("You Win! ")
        elif compResponse == 2:
            print("Computer Wins! ")
        else:
            print("It is a Draw! ")
    elif userResponse == 2:
        if compResponse == 0:
            print("Computer Wins! ")
        elif compResponse == 1:
            print("You Win! ")
        else:
            print("It is a draw! ")
    else:
        print("Invalid Input, Please type between 0, 1, and 2 ")
