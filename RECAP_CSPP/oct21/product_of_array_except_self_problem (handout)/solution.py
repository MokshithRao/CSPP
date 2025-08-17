def product_except_self(arr):
    prod=[]

    for i in range (len(arr)):
        p=1
        for j in range (len(arr)):
            if i!=j:
                p*=arr[j]
                
        prod.append(p)
    return prod
        

print(product_except_self(eval(input())))