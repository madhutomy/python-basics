import random
# Given a list of names , pick a random person
names_string = input("Enter the guests: ")
names = names_string.split(", ")

random = random.randint(0, len(names))
selected_person = names[random]
print(f"{selected_person} is going to buy the meal today!")