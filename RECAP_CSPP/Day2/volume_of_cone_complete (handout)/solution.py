# Write your solution here
def Calculate_vol_cone(radius, height):
    Volume = 1/3 * 3.14159 * radius**2 * height
    return round(Volume,2)
print(Calculate_vol_cone(float(input()), float(input())))