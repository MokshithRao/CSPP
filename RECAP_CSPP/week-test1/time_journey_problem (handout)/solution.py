def calculate_time(speed, distsnce):
    if speed == 0:
        return "float('inf')"
    else:
        return round((distsnce/speed),2)
    
print(calculate_time(float(input()), float(input())))