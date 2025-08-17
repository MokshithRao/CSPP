o_time=float(input())
o_efficiency = float(input())
n_efficiency = float(input())

def cal_time_saved(o_time, o_efficiency, n_efficiency):
    n_time = (o_time * o_efficiency)/n_efficiency
    time_saved = o_time - n_time
    return round(time_saved,2)

print(cal_time_saved(o_time, o_efficiency, n_efficiency))
