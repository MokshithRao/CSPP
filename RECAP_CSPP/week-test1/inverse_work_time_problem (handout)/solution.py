workers_i = int(input())
time_i = float(input())
workers_final = int(input())

def calculate_time(workers_i, time_i, workers_final):
    Time_final = (workers_i * time_i)/workers_final
    return Time_final
print(calculate_time(workers_i, time_i, workers_final))