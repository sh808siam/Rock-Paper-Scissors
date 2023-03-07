rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
user_input = int(input("What do you choose?\nType 0 --> Rock\nType 1 --> Paper\nType 2 --> Scissors.\nLess than 0 or more than 3 will result a defeat. "))
comp_input = random.randint(0,2)

if user_input == 0 :
    print("You:\n",rock)
elif user_input == 1 :
    print("You:\n",paper)
elif user_input == 2 :
    print("You:\n",scissors)
if comp_input == 0 :
    print("Computer:\n",rock)
elif comp_input == 1 :
    print("Computer:\n",paper)
elif comp_input == 2 :
    print("Computer:\n",scissors)

if user_input >= 3 or user_input < 0 :
    print(f"You typed {user_input} which is an invalid number, so you lose by default!")
elif user_input == comp_input :
    print("It's a DRAW...")
elif user_input == 0 and comp_input == 1 :
    print("You LOOSE !!!")
elif user_input == 0 and comp_input == 2 :
    print("You WiN !!!")
elif user_input == 1 and comp_input == 0 :
    print("You WiN !!!")
elif user_input == 1 and comp_input == 2 :
    print("You LOOSE !!!")
elif user_input == 2 and comp_input == 0 :
    print("You LOOSE !!!")
elif user_input == 2 and comp_input == 1 :
    print("You WiN !!!")