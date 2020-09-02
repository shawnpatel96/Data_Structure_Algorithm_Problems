
def findMaxConsecutiveOnes(nums):
    #Keep track of current consecutive seen and max consecutive seen.
    cur = 0
    mx = 0
        
    for num in nums:
        if nums == 1:
            cur += 1
            mx = max(mx,cur)
        else:
            cur = 0
    return mx
numss= [1,1,1,0,1,1,1,1,1]
print(findMaxConsecutiveOnes(numss))

