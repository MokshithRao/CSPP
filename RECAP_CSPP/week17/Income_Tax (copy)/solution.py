# def deducton(income):
#     if income > 20000:
#         return income - 5000



# def income_tax_calculator(s):
#     s=s.split()
#     income = int(s[-1])

#     if income <= 10000:
#         return 0.0
#     elif income > 10000 and income <= 40000:
#         if income > 20000:
#             income = deducton(income)
#             a =  0 + income - (income * 0.10) + 1000
#             return income - a
#         else:
#             return income - (income * 0.10)
    

# print(income_tax_calculator(input()))




# s=input().split(" ")
# income=int(s[-1])
# def income_tax(income):
#     if income>20000:
#         income=income-5000
#     if income<=10000:
#         return 0.0
   
#     elif 10000<=income<=40000:
#         a=income-10000
#         per= (a/100)*10
#         return per
#     elif 40000<=income<=80000:
#          a=income-10000
#          b=a-30000
#          per=(b/100)*20
#          return 0+3000+per
#     elif income>=80000:
#          a=income-10000
#          b=a-30000
#          c=b-40000
#          per=(c/100)*30
#          return 0+3000+8000+per


# print(income_tax(income))






def income(k):
    s=k.split()
    l=int(s[4])
    fee=0
    if l > 20000:
        c = l - 5000
    else:
        c = l
    if c<= 10000:
        fee = 0
    elif c>10000 and c<=40000:
        fee = (10000*0)+((c-10000)*0.1)
    elif c> 40000 and c<= 80000:
        fee = (10000*0)+(30000*0.10)+((c-40000)*0.20)
    elif c> 80000:
        fee = (10000*0)+(30000*0.10)+(40000*0.20)+((c-80000)*0.3)
    return round(float(fee),2)
print(income(input()))