def health_insurance(n,s):
    if n >= 0 and n <= 18 and s == 'False':
        return 100
    if n >= 0 and n <= 18 and s == 'True':
        return 100
    elif n >= 19 and n <= 35 and s == 'False':
        return 200
    elif n >= 19 and n <= 35 and s == 'True':
        return 200 + (200*0.05)
    elif n >= 36 and n <= 50 and s == 'False':
        return 300
    elif n >= 36 and n <= 50 and s == 'True':
        return 300 + (300*0.1)
    elif n >= 51 and n <= 65 and s == 'False':
        return 500
    elif n >= 51 and n <= 65 and s == 'True':
        return 500 + (500*0.15)
    elif n >= 66 and s == 'False':
        return 700
    elif n >= 66 and s == 'True':
        return 700 + (700*0.2)
    
print(health_insurance(int(input()), input()))

