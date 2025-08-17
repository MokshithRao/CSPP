def zigzag(n):
    pattern = []
    for i in range(n):
        row = [' '] * n
        if i % 2 == 0:
            for j in range(0, n, 2):
                row[j] = '*'
        else:
            for j in range(1, n, 2):
                row[j] = '*'
                
        pattern.append(''.join(row))
    return pattern
print(zigzag(int(input())))