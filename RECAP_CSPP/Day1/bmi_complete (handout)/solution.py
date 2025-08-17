# Write your solution here
def BMI_calculator(weight, height):
    bmi = weight / height**2
    return round(bmi,2)
print(BMI_calculator(float(input()), float(input())))
