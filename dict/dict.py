# In Python dictionary is a collection of key-value pairs
car = {"brand": "Toyota", "model": "camry", "style": "sedan", "trim": "LE"}
print(car["brand"])  # output => Toyota
# adding elements to the dictionary
car["gear"] = "automatic"
print(car)  # output => {'brand': 'Toyota', 'model': 'camry', 'style': 'sedan', 'trim': 'LE', 'gear': 'automatic'}
# modifying a dictionary
car["model"] = "corolla"
print(car)  # output => {'brand': 'Toyota', 'model': 'corolla', 'style': 'sedan', 'trim': 'LE', 'gear': 'automatic'}
# removing elements from a dictionary
del car["gear"]
print(car)  # output => {'brand': 'Toyota', 'model': 'corolla', 'style': 'sedan', 'trim': 'LE'}
gear_value = car.get("gear", "No gear value found")
print(gear_value)
for key, value in car.items():
    print("Key :" + key)

for value in car.keys():
    print("value :" + key)

# looping through the sorted values
for value in sorted(car.values()):
    print(value)

# a list of dictionaries
person_1 = {"name": "Jon", "age": 21, "country": "U.S.A"}
person_2 = {"name": "Madhu", "age": 25, "country": "India"}
person_3 = {"name": "Ming", "age": 33, "country": "China"}

people = [person_1, person_2, person_3]
print(people)

# dict containing list
developer_1 = {"name": "Jon", "languages": ["C++", "Java"]}

for key, info in developer_1.items():
    for language in info:
        print(language)

# a dict in a dict
employees = {"aa": {"name": "A", "position": "developer"}, "bb": {"name": "B", "position": "manager"}}
for index, employee in employees.items():
    print(f" Name : {employee['name']} , position: {employee['position']}")
