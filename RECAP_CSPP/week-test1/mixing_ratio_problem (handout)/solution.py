c1=float(input())
c2=float(input())
t_c=float(input())
def calculate_mixing_ratio(c1, c2, t_c):
    mixing_ratio = (t_c - c2)/(c1 - t_c)
    return mixing_ratio
print(calculate_mixing_ratio(c1, c2, t_c))