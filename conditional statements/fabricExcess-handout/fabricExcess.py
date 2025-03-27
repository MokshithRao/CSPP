
def fabricExcess(inches):
	if inches == 0:
		return 0
	if inches%36 == 0:
		return 0
	else:
		return ((inches//36)+1)*36 - inches
print(fabricExcess(int(input())))

# def fabricExcess(inches):
#     yards=inches//36
#     if(inches%36!=0):
#         yards=yards+1
#         z=  yards*36-inches
#         return z
#     else:
#         return 0
    
# print(fabricExcess(int(input())))