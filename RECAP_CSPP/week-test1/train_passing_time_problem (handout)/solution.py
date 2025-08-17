t_speed = float(input())
t_length = float(input())
p_length = float(input())

def train_passing_speed(t_speed, t_length, p_length):
    time = (t_length + p_length)/t_speed * (3600/1000)
    return round(time,2)
print(train_passing_speed(t_speed, t_length, p_length))
