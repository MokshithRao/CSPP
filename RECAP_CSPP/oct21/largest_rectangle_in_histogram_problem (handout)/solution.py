def largest_rectangle_area(heights):
    heights.append(0)
    l = []
    max_area = 0
    
    for i in range(len(heights)):
        while l and heights[i] < heights[l[-1]]:
            h = heights[l.pop()]
            if l:
                w = i - l[-1] - 1
            else:
                w = i
            max_area = max(max_area, h * w)
        l.append(i)
    heights.pop()
    return max_area

print(largest_rectangle_area(eval(input())))
