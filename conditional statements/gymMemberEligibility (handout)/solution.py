def gym(age,bmi,health_condition):
    if (age>=18 and age<=60 and bmi>=18.5 and bmi<=24.9 and not(health_condition)) or (age<18 and (bmi>=18.5 and bmi<24.9)) or (age>=60 and bmi>=18.5 and bmi<=24.9 and not(health_condition)):
        return True
    else:
        return False
print(gym(int(input()), float(input()), str(input())=="True"))
