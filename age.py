# Melane Minayo SCT211-0043/2022
name = input("Enter your name:")
print("Hello "+name)

from datetime import datetime

dob_input = input("Enter your date of birth (yyyy-mm-dd): ")


try:
    dob = datetime.strptime(dob_input, "%Y-%m-%d")
except ValueError:
    print("Your format is invalid .Kindly use the format yyyy-mm-dd.")
else:
    
    current_date = datetime.now()

    age = current_date.year - dob.year
    months = current_date.month - dob.month
    days = current_date.day - dob.day

    if current_date.month < dob.month or (current_date.month == dob.month and current_date.day < dob.day):
        age -= 1
        months = 12 - dob.month + current_date.month
        if current_date.day < dob.day:
            months -= 1
        days = (current_date - datetime(current_date.year, current_date.month - 1 if current_date.month > 1 else 12, dob.day)).days

   
    print(f"Your are {age} years {months} months and {days} days old")


num1= input("Input num1: ")
num2 = input("Input num2: ")

num1=int(num1)
num2=int(num2)

print("The sum of the two numbers is : ",num1 + num2)
