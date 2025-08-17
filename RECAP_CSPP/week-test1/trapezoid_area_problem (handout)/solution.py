def cal_trapezoid_area(b1, b2, h):
    area = 0.5 * (b1 + b2) * h
    return round(area,2)
print(cal_trapezoid_area(float(input()), float(input()), float(input())))