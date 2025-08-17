def swap_elemenst(list):
    if not list:
        return list
    smallest = list.index(min(list))
    largest = list.index(max(list))

    list[smallest], list[largest] = list[largest], list[smallest]
    return list    


print(swap_elemenst(eval(input())))
            