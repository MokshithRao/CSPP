def robot():
    age=int(input())
    has_id=str(input())=="True"
    knows_password=str(input())=="True"
    return (age>=18 and has_id) or knows_password
print(robot())