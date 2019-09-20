N=100
doors=[]
open_doors=[]
for i in range(100):
    doors.append("|")

k=1
for i in range(100):
    for j in range(100):
        if i+(j*k)>99:
            break
        if doors[i+(j*k)]=="X":
            doors[i+(j*k)]="|"
        else:
            doors[i+(j*k)]="X"
    k+=1
print("The following doors are open: ",end="")
for i in range(100):
    if doors[i]=="X":
        open_doors.append(i+1)

for i in range(len(open_doors)-1):
    print(open_doors[i],end=", ")
print(open_doors[i+1])
