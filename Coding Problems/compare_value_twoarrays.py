a = [10,6,0]
b = [10,5,5]
    #[1,1]
def compare(a,b):
    alice_count = 0
    bob_count = 0
    
    for i in range(3):
        if a[i] > b[i]:
            alice_count +=1
        elif b[i] > a[i]:
            bob_count +=1
    
    return [alice_count, bob_count]

print(compare(a,b))