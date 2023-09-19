import random
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
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice=int(input("Enter your input: "))
choice_list=[rock,paper,scissors]
user_choice=choice_list[choice]
print(f"You chose :\n {user_choice}")
computer_choice=choice_list[random.randint(0,2)]
print(f"Computer chose :\n {computer_choice}")
if user_choice == computer_choice :
  print("Its a draw")
else:
  if computer_choice == rock:
    if user_choice == scissors:
      print("Computer wins.")
    else:
      print("User wins.")
  elif computer_choice == paper:
    if user_choice == rock:
      print("Computer wins.")
    else:
      print("User wins.")
  elif computer_choice == scissors:
    if user_choice == paper:
      print("Computer wins.")
    else:
      print("User wins.")  
