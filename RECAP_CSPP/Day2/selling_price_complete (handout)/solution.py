# Write your solution here
def Cal_selling_price(cp, pp):
    sp = cp + (pp/100*cp)
    return round(sp,2)
print(Cal_selling_price(float(input()), float(input())))