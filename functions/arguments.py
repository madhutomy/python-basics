# In Python arguments can be passed as position arguments or keyword arguments

# position arguments
def describe_employee(name, age):
    print(f"Name: {name} and age is {age}")  # output => Name: Jon and age is 31


describe_employee("Jon", 31)
# This is throw an error - Missing 1 required positional argument 'age', as python expects first argument as the name
# so order is important for positional arguments
# describe_employee(31)

# keyword-arguments
# this is a key-value pair that you pass to a function. So this will free you from having to worry about
# correctly ordering the arguments for the function call.
describe_employee(name="James", age=44)  # output => Name: James and age is 44


# Default argument values
# Here is a function that accepts any cities in U.S.A
def display_city(city_name, country="U.S.A"):
    print(f"The city {city_name} is in {country}")


display_city("Houston", "U.S.A")
display_city("Dallas")


# Making arguments optional, to do that you can provide blank or default values and make it to the end of the
# parameter list
def get_full_name(first_name, last_name, middle_name=''):
    full_name = ""
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    return full_name


print(get_full_name("madhu", "tomy"))
print(get_full_name("JON", "stewart", "ezpinoza"))


# Passing an arbitrary number of arguments
def display_car_names(*names):
    print(names)


display_car_names("altima")
display_car_names("maxima", "rogue", "centra")

