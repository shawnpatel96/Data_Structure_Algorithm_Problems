
array = [8,1,2,2,3]
#output [4,0,1,1,3]

def smallerNumbersThanCurrent(array):
        # return value of each number less than current number
        cache = {}
        sorted_list = sorted(array)
        
        for i,n in enumerate(sorted_list):
            if n not in cache:
                cache[n] = i

        return [cache[n] for n in array]






print(smallerNumbersThanCurrent(array))