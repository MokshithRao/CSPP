# def health_insurance(age, s):
#     if age >= 0 and age <= 18 and s == 'False':
#         print(100)
#     if age >= 0 and age <= 18 and s == 'True':
#         print(100)
#     elif age >= 19 and age <= 35 and s == 'False':
#         print(200)
#     elif age >= 19 and age <= 35 and s == 'True':
#         print(200+10.0)
#     elif age >= 36 and age <= 50 and s == 'False':
#         print(300)
#     elif age >= 36 and age <= 50 and s == 'True':
#         print(300+30.0)
#     elif age >= 51 and age<=65 and s == 'False':
#         print(500)
#     elif age >= 51 and age<=65 and s == 'True':
#         print(500+75.0)
#     elif age >= 66 and s == 'False':
#         print(700)
#     elif age >= 66 and s == 'True':
#         print(700 + 140.0)


# health_insurance(int(input()), input())



    




def health_insurance(age, s):
    if age >= 0 and age <= 18 and s == 'False':
        print(100)
    if age >= 0 and age <= 18 and s == 'True':
        print(100)
    elif age >= 19 and age <= 35 and s == 'False':
        print(200)
    elif age >= 19 and age <= 35 and s == 'True':
        print(200+ (200*5/100))
    elif age >= 36 and age <= 50 and s == 'False':
        print(300)
    elif age >= 36 and age <= 50 and s == 'True':
        print(300+ 300*10/100)
    elif age >= 51 and age<=65 and s == 'False':
        print(500)
    elif age >= 51 and age<=65 and s == 'True':
        print(500+ 500*15/100)
    elif age >= 66 and s == 'False':
        print(700)
    elif age >= 66 and s == 'True':
        print(700 + 700*20/100)


health_insurance(int(input()), input())



    