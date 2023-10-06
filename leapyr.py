
try:
    year = int(input("Enter a year: "))
except ValueError:
    print("Invalid input. Please enter a valid year.")
else:
  
    if (year % 4 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

