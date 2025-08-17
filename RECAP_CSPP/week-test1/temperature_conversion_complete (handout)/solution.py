# Write your solution here
def convert_temperature(f):
    c = (5/9) * (f-32)
    return round(c,2)
print(convert_temperature(float(input())))