# Python program to determine if a given year is a leap year

year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is a Leap year")
    elif year % 400 == 0:
        print(f"{year} is a Leap year")
    else:
        print(f"{year} is NOT a Leap year")
else:
    print(f"{year} is NOT a Leap year")