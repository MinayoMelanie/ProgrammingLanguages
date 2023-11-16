# MELANE MINAYO SCT211-0043/2022
try:
    total_bill = float(input("Enter the total bill amount: $"))
    tip_percentage = int(input("Enter the tip percentage (10, 12, or 15): "))
    num_people = int(input("Enter the number of people splitting the bill: "))
except ValueError:
    print("Invalid input.")
else:
    
    if tip_percentage not in [10, 12, 15]:
        print("Invalid tip percentage.Choose from 10, 12, or 15.")
    elif num_people <= 0:
        print("Invalid number of people.Enter a positive number.")
    else:
        
        tip_amount = total_bill * (tip_percentage / 100)

      
        total_amount = total_bill + tip_amount

       
        amount_per_person = total_amount / num_people

        
        print(f"Each person should pay: ${amount_per_person:.2f}")
