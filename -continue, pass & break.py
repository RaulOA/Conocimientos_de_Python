import os
os.system("cls")

i=0
while i<10:
    i+=1
    if i==7:
        continue
    print(i)
print("-----------------")
i=0
while i<10:
    i+=1
    if i==7:
        pass
    print(i)
print("-----------------")
i=0
while i<10:
    i+=1
    if i==7:
        break
    print(i)