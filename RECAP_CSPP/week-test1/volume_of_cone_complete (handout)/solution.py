# Write your solution here
def vol_of_cone(r,h):
    pi = 3.14159
    volume = 1/3 * pi * (r**2) * h
    return round(volume,2)
print(vol_of_cone(float(input()), float(input())))