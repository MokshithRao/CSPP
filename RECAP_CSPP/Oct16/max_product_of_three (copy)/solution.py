n = int(input())
l = list(map(int, input().split()))

def max_product_of_three(l, n):
    if len(l) < 3:
        return l[-1] * l[-2] * l[-3]

    max1 = max2 = max3 = float("-inf")
    min1 = min2 = float("inf")

    for num in l:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    product1 = max1 * max2 * max3
    product2 = max1 * min1 * min2

    return max(product1, product2)
print(max_product_of_three(l, n))