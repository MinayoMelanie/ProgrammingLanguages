# MELANE MINAYO SCT211-0043/2022
try:
    weight = float(input("Enter your weight (in kilograms): "))
    height = float(input("Enter your height (in meters): "))
except ValueError:
    print("Invalid input. Please enter valid numbers for weight and height.")
else:
 
    bmi = weight / (height ** 2)

    
    if bmi < 18:
        category = "Underweight"
    elif 18 <= bmi <= 25:
        category = "Normal weight"
    else:
        category = "Overweight"

    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")
