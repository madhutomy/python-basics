# range() method is to generate a series of numbers
result = []
for number in range(1, 5):
    result.append(number)
print(result)

# Generate Even numbers between 1, 20
result = []
for num in range(2, 21, 2):
    result.append(num)
print(result)


# Generate squares of all numbers between 1, 20
result = []
for num in range(2, 21):
    result.append(num*num)
print(result)
