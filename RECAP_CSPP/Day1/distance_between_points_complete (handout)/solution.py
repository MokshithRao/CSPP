# Write your solution here
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
def Distance_bw_Points(x1,x2,y1,y2):
    Distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return round(Distance, 2)
print(Distance_bw_Points(x1,x2,y1,y2))