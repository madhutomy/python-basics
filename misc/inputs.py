# while using "input" python pauses and waits for the user input and assigns the value to a variable
name = input("Enter your name: ")
print(f"Hello {name}")

# How to get numerical inputs
age = input("Enter your age: ")
age = int(age)
if age > 18:
    print("You are an Adult")
else:
    print("You are a Minor")