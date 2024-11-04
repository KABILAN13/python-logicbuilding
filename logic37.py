a=input()
b=a.split()
c=100
for i in range(len(b)):
    x,y=b[i].split("@")
    y=float(y)
    if(y<c):
        c=y
        car=x
print(car)