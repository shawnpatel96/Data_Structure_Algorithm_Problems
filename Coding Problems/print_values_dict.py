# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:

# Your algorithm should return 41, the sum of the values 23 and 18.

myobject = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
count = 0
for i in myobject.values():
    print(i)
    
    if isinstance(i, int):
        count += i
    
        
print(count)