b_speed = float(input())
s_speed = float(input())
distance = float(input())

def time_to_travel_downstream(b_speed, s_speed, distance):
    Time = distance/(b_speed + s_speed)
    return round(Time, 2)
print(time_to_travel_downstream(b_speed, s_speed, distance))
