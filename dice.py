import random

users_choice = input("enter a number -:")
random_number = int(random.random()*6)

if random_number > 50:
    c = "1"
    if random_number > 100:
    c = "2"
    if random_number > 150:
    c = "3"
    if random_number > 200:
    c = "4"
    if random_number > 300:
    c = "5"
    if random_number > 350:
    c= "6"
print(random_number)
if users_choice == c:
    print("you won")
else:
    print("better luck next time")
