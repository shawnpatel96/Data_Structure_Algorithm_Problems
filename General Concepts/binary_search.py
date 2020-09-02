def search(arr,target):
        if len(arr) == 0:
            return -1
        else:
            left = 0
            right = len(arr) -1
            
            while left <= right:
                midpoint = (right + left) // 2
                
                if arr[midpoint] == target:
                    return midpoint
                elif arr[midpoint] > target:
                    right = midpoint - 1
                elif arr[midpoint] < target:
                    left = midpoint + 1
            return -1

arr = [1,2,3,4,5,8,9,11,22,101,2548]
print(search(arr,99))