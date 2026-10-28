counts=[0,4,2,5]
selected=0
total=0

for i in counts:
    if i>=3:
        selected+=1
        total+=i
print(selected, total)
        