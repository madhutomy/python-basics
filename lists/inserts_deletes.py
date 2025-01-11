# Inserts and Appends
cars = ["Ford", "Chevy", "Toyota"]
cars.append("Subaru")
print(cars)  # Output => ['Ford', 'Chevy', 'Toyota', 'Subaru']
cars.insert(1, "Buick")
print(cars)  # Output => ['Ford', 'Buick', 'Chevy', 'Toyota', 'Subaru']
cars.insert(-1, "Nissan")
print(cars)  # Output => ['Ford', 'Buick', 'Chevy', 'Toyota', 'Nissan', 'Subaru']
cars.append("Hyundai")
print(cars)  # Output => ['Ford', 'Buick', 'Chevy', 'Toyota', 'Nissan', 'Subaru', 'Hyundai']

# del, pop, remove
# If you know the position, use del()
del cars[0]
print(cars)  # Output => ['Buick', 'Chevy', 'Toyota', 'Nissan', 'Subaru', 'Hyundai']
# pop() - removes the last element of the list by default.
# the main use case of pop in comparison with del is that if you want to use an item as we remove it
car_value_popped = cars.pop()
print(car_value_popped)  # Output => Hyundai
print(cars)  # Output => ['Buick', 'Chevy', 'Toyota', 'Nissan', 'Subaru']
# If you provide the index, then it will remove it
cars.pop(0)
print(cars)  # Output => ['Chevy', 'Toyota', 'Nissan', 'Subaru']
# remove() - It is used if you want to remove an item by value. If there are multiple instances of the same
# value them remove("value") removes the first occurance of that value.
# cars.remove("Buick") # Output => ValueError: list.remove(x): x not in list
cars.remove("Nissan")  # Output => ['Chevy', 'Toyota', 'Nissan', 'Subaru']
