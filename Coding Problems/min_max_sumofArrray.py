arr = [1,2,3,4,5]
        # output 10,14
    
def miniMaxSum(arr):
    min_sum = 0
    max_sum = 0

    for num in arr[1:]:
        max_sum += num

    for num in arr[:-1]:
        min_sum += num
    
    return min_sum,max_sum

print(miniMaxSum(arr))