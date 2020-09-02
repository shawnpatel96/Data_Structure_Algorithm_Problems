# brute force O(n^2)
string = 'abababababcdefg'
# def first(string):
#     for i in range(len(string)):
#         seen = False
#         for j in range(len(string)):
#             if string[i] == string[j] and i is not j:
#                 seen = True
#                 break
#         if seen is False:
#             return string[i]
#     return '_'

#hash map

cache = {}
for char in string:
    if char not in cache:
        cache[char] = 1
    else:
        cache[char] +=1
print(cache)
for key in cache:
    if cache[key] == 1:
        print(key)
