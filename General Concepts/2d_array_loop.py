arr = [ [1,1,1,2,2,2],
        [0,1,0,0,2,0],
        [1,1,1,2,2,2],
        [0,0,0,2,2,2],
        [0,0,0,0,2,0],
        [0,0,0,2,2,3]]


def h(arr):
    max_val = 0
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            current_hourglass_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            max_val = max(max_val, current_hourglass_sum)
    return max_val

print(h(arr))




