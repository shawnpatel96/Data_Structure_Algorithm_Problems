arr = [3,3,4,3,4,3,0,3,3,2]


def h(arr):
    max_num = None
    second_max = None
    third_max = None

    for num in arr:
        if num == max_num or num == second_max or num == third_max:
            continue
        if max_num == None or num > max_num:
            third_max = second_max
            second_max = max_num
            max_num = num
        elif second_max == None or num > second_max:
            third_max = second_max
            second_max = num
        elif third_max == None or num > third_max:
            third_max = num
    if third_max == None:
        return max_num
    else:
        return third_max
        


print(h(arr))


