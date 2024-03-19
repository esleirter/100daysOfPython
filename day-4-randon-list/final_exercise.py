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

#Write your code below this line 👇

user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

alternatives = [rock,paper,scissors]

print(alternatives[user_choose])

print("Computer choose:")
computer_choose = random.randint(1,3) - 1
print(alternatives[computer_choose])

if user_choose >= 3 or user_choose < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choose == 0 and computer_choose == 2:
  print("You win!")
elif computer_choose == 0 and user_choose == 2:
  print("You lose")
elif computer_choose > user_choose:
  print("You lose")
elif user_choose > computer_choose:
  print("You win!")
elif computer_choose == user_choose:
  print("It's a draw")

