arr = [1,2,3]

def findpairs(arr):
    cache = {}
    answer = []
    for i in range(len(arr)):
        if arr[i] not in cache:
            cache[arr[i]] = i
       
    print(cache)
    for x in cache:
        for j in cache:
            if cache[x] == cache[j]:
                 answer.append((cache[x],cache[j]))
    return answer

        
print(findpairs(arr))