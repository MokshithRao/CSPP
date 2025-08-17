def main(n):
    for i in n:
        r = sum(i)
        return r

def is_Magic_Square(matrix):
    d = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                d += matrix[i][j]
    if d == main(matrix):
        return True
    return False
    
print(is_Magic_Square(eval(input())))








