print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

nameTogether = (name1 + name2).lower()
firstNumber = 0
firstNumber += nameTogether.count("t")
firstNumber += nameTogether.count("r")
firstNumber += nameTogether.count("u")
firstNumber += nameTogether.count("e")

secondNumber = 0
secondNumber += nameTogether.count("l")
secondNumber += nameTogether.count("o")
secondNumber += nameTogether.count("v")
secondNumber += nameTogether.count("e")

loveScore  = int(str(firstNumber) + str(secondNumber))

if loveScore < 10 or loveScore > 90:
  print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore > 40 and loveScore < 50:
  print(f"Your score is {loveScore}, you are alright together.")
else:
  print(f"Your score is {loveScore}.")



