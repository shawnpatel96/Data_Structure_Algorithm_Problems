"""Return if the amount of digits in the number is even"""
nums = [123,23,2323]  # should print 2
even = []
for num in nums:
    string = str(num)
    print(len(string))
    if (len(string)) % 2 == 0:
        even.append(string)

print(len(even))
