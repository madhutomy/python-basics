# Organizing the lists
cars = ["Ford", "Chevy", "Toyota"]
# sort() - This method will alphabetically sort the list. But it will permanently change the order of elements in the
# list
cars.sort()
print(cars)
# in reverse-alphabetically order
cars.sort(reverse=True)
print(cars)
# Sorted() will not permanently change the order of elements in the list
print(sorted(cars))
print(cars)