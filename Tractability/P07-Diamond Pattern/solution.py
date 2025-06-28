num=int(input())
def Diamond_pattern(num):
    for i in range(1,num,2):
        print(" " * ((num-i)//2)+"*" * i)
    for i in range(num,0,-2):
        print(" " * ((num-i)//2)+"*" * i)
    
Diamond_pattern(num)