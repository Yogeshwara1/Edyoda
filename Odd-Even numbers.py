i=[1,2,3,4,5,6,7,8,9]
odd=0
even=0
for n in i:
    if not n % 2:
        even+=1
    else:
        odd+=1

print("odd",odd)
print("even",even)
