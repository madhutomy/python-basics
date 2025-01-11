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
del cars[0]
print(cars)  # Output => ['Buick', 'Chevy', 'Toyota', 'Nissan', 'Subaru', 'Hyundai']
car_value_popped = cars.pop()
print(car_value_popped)  # Output => Hyundai
print(cars)  # Output => ['Buick', 'Chevy', 'Toyota', 'Nissan', 'Subaru']
cars.pop(0)
print(cars)  # Output => ['Chevy', 'Toyota', 'Nissan', 'Subaru']
# cars.remove("Buick") # Output => ValueError: list.remove(x): x not in list
cars.remove("Nissan")  # Output => ['Chevy', 'Toyota', 'Nissan', 'Subaru']
