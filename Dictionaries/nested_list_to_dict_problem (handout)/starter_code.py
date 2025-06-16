lst = eval(input())

def nested_list_to_dict(lst):
    def dict(lst):
        d = {}
        i = 0
        for element in lst:
            if type(element) == list:
                d[i] = dict(element)
            else:
                d[i] = element
            i += 1
        return d

    return dict(lst)

print(nested_list_to_dict(lst))