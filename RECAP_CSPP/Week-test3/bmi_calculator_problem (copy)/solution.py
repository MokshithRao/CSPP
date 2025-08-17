def BMI_Calculator(weight, height):
    bmi = weight/(height**2)
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
    
print(BMI_Calculator(float(input()), float(input())))