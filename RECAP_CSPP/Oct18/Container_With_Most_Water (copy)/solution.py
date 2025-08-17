def Container_with_most_water(h):
    max_area = 0
    length = len(h)
    for i in range(length):
        for j in range(i + 1, length):
            height = min(h[i], h[j])
            width = j - i
            area = height * width
            max_area = max(max_area, area)

    return max_area


print(Container_with_most_water(eval(input())))