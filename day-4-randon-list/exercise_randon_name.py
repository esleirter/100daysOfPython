names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

import random

radom_value = random.randint(1, len(names)) - 1

choose_person = names[radom_value]

print(f"{choose_person} is going to buy the meal today!")