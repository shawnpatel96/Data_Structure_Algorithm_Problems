arr = [1,2,5,1,2,6,7,8,10]

def h(arr):
    #pointer 
    i = 0
    for j in range(len(arr)):
        # if even number is encounted
        if arr[j] % 2 == 0:
            # currently is set to arr[0]
            temp = arr[i]
            #swap even to front of array with element in the front
            arr[i] = arr[j]
            arr[j] = temp
            i+=1
    return arr

    
      
    
print(h(arr))