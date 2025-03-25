def Garden():
    soil_dry=str(input())=="True"
    raining=str(input())=="True"
    day_time=str(input())=="True"
    temperature=int(input())
    return soil_dry and not(raining) and day_time and temperature>10
print(Garden())