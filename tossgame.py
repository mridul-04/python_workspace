import random

users_choice = input("Choose Head or Tail -:")
random_number = int(random.random()*100)

if random_number > 50:
    c = "head"
else:
    c = "tail"
print(random_number)
if users_choice == c:
    print("you won")
else:
    print("better luck next time")